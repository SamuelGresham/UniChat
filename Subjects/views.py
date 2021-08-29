from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Subject, Chat, Request
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def index (request):
    return render(request, 'landing.html')

def findCourse (request):
    if request.method == "GET":
        return render(request, "find.html")
    elif request.method == "POST":
        chats = findChats(request.POST.get("course"), request.POST.get("period"))
        return render(request, "find.html", {'data': chats})

# Finds chats for a given course and period and returns them as JSON
def findChats (course, period):
    chats = Chat.objects.filter(course=course, period=period)

    if (not course or not period):
        return [{'name': "Missing data :( "}]

    chat_list = []

    for chat in chats:
        print(chat)
        if chat.approved:
            if chat.chat_platform == "Messenger":
                chat_list.append({
                    'name': chat.chat_name,
                    'platform': chat.chat_platform,
                    'url': "http://127.0.0.1:8000/request/" + str(chat.mess_id),
                    'url_text': "Request Access"
                })
            else:
                chat_list.append({
                    'name': chat.chat_name,
                    'platform': chat.chat_platform,
                    'url': chat.chat_link,
                    'url_text': "Join"
                })

    
    if not chat_list:
        chat_list.append({
            'name': "No chats found :( Be a hero and make one!"
        })
    # out = json.dumps(chat_list)

    return chat_list

def publish (request):
    return render(request, "publish.html")

def publish_messenger (request):
    return render(request, "messenger.html")

def process_messenger (request):
    course = request.POST.get("course")
    period = request.POST.get("period")
    name = request.POST.get("name")

    if (not name or not period or not course):
        return HttpResponseBadRequest()

    chat = Chat(chat_name=name, chat_platform="Messenger", chat_link="", course=course, period=period, approved=True)

    chat.save()

    chat.chat_link = "http://127.0.0.1:8000/request/" + str(course) + str(chat.pk)
    chat.mess_id = str(course) + str(chat.pk)

    chat.save()

    return render(request, "messenger_success.html", {'URL': chat.chat_link, 'id': chat.mess_id})

def dashboard (request, chat_id):

    if request.POST.get("data") and request.POST.get("id"):
        print("poopoo")
        obj = Request.objects.get(pk = request.POST.get("id"))
        obj.added = not obj.added
        obj.save()

    obj = Chat.objects.get(mess_id=chat_id)
    reqs = Request.objects.filter(mess_id=chat_id)
    requesters = []
    done = []

    for req in reqs:
        if not req.added:
            requesters.append({
                    'first': req.first_name,
                    'last': req.last_name,
                    'link': req.fb_link,
                    'id': req.pk
                })
        else:
            done.append({
                'first': req.first_name,
                'last': req.last_name,
                'link': req.fb_link,
                'id': req.pk
            })
        print(req.pk)

    chat_info = {
        'name': obj.chat_name,
        'course': obj.course,
        'period': obj.period
    }

    return render(request, "dashboard.html", {'info': chat_info, 'requesters': requesters, 'done': done})

def request (request, chat_id):
    return render(request, "request.html", {'chat_id': chat_id})

def request_submit (request): 
    first_name = request.POST.get("first")
    last_name = request.POST.get("last")
    mess_code = request.POST.get("chat_id")
    fb_url = request.POST.get("url")

    print(f'{first_name} {last_name} {mess_code} {fb_url}')

    req = Request(first_name=first_name, last_name=last_name, mess_id=mess_code, fb_link=fb_url, added=False)
    
    req.save()
    
    return render(request, "success.html")

def publish_other (request):
    return render(request, "other.html")

def process_other (request):
    course_code = request.POST.get("course")
    period = request.POST.get("period")
    name = request.POST.get("name")
    platform = request.POST.get("platform")
    url = request.POST.get("url")

    chat = Chat(chat_name=name, chat_platform=platform, chat_link=url, course=course_code, period=period, approved=False, mess_id="none")

    chat.save()

    context = {
        'name': name,
        'platform': platform,
        'url': url,
        'course': course_code,
        'period': period,
    }

    return render(request, "other_made.html", context)

@login_required
def init (request):
    f = open("Subjects/data.txt", "r")
    read = f.read()
    courses = json.loads(read)
    for course in courses:
        a = Subject(subject_code = course)
        a.save()
    
    return HttpResponse("Data updated from local file. Cowabunga!")

