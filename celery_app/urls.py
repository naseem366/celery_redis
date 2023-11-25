from django.urls import path
from celery_app import views
from .views import *

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('result/<str:task_id>',views.check_result,name='check_result'),
    #path('add',AddDetails.as_view(),name='add')
]