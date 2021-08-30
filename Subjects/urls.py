from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('find/', views.findCourse, name='find'),
    path('init/', views.init, name='init'), #REMOVE IN PROD!!
    path('publish/', views.publish, name='publish'),
    path('publish/messenger/', views.publish_messenger, name='publish messenger'),
    path('publish/messenger/makemessenger', views.process_messenger, name='prcss'),
    path('dashboard/<str:chat_id>', views.dashboard, name='dashboard'),
    path('request/submit', views.request_submit, name='request'),
    path('request/<str:chat_id>', views.request, name='request'),
    path('publish/other', views.publish_other, name='pubother'),
    path('publish/makeother', views.process_other, name='pubother'),
    path('help', views.help, name='help'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
