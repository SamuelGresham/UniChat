from django.contrib import admin
from Subjects.models import Subject, Chat, Request

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_name', 'chat_platform', 'chat_link', 'course', 'period', 'approved')
    list_filter = (
         "approved",
    )
    search_fields = (
        "course",
        "chat_name",
    )

# Register your models here.
admin .site.register(Subject)
admin.site.register(Request)
admin.site.register(Chat, ChatAdmin)

