from django.contrib import admin
from django.urls import path
from main.views import main, set_recruit, questions, get_sith, get_recruits, view_recrut_details
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    path('set_recruit/', set_recruit, name='set_recruit'),
    path('questions/<int:id>/', questions, name='questions'),
    path('get_sith/', get_sith, name='get_sith'),
    path('get_recruits/<int:id>/', get_recruits, name='get_recruits'),
    path('get_recruits/<int:id>/<int:recid>', get_recruits, name='get_recruits'),
    path('view_recrut_details/<int:id>', view_recrut_details, name='view_recrut_details')
]
