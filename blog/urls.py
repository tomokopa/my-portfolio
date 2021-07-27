from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('timer/push_timer/', views.push_timer, name='push_timer'),
    path('contact/', views.contact_form, name='contact_form'),
    path('contact/complete', views.contact_complete, name='contact_complete'),
]