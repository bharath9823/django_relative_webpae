from django.urls import path
from urlapp import views

#Global inbuilt variable name
app_name='urlapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('relative/',views.relative,name='relative'),
    path('about/',views.about, name='about')
]