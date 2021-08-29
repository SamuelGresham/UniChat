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
    path('dashboard/<str:chat_id>', views.dashboard, name='dashboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
