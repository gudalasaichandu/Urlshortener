from django.urls import path
from . import views

urlpatterns=[
    path('',views.posturl),
    path('a/',views.geturl),
    path('history/',views.history),

]