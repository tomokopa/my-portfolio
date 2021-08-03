from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('works/portfolio/', views.works_portfolio, name='works_portfolio'),
    path('works/push_timer/', views.works_push_timer, name='works_push_timer'),
    path('works/laundry_weather/', views.works_laundry_weather, name='works_laundry_weather'),
    path('timer/push_timer/', views.push_timer, name='push_timer'),
    path('contact/', views.contact_form, name='contact_form'),
    path('contact/complete', views.contact_complete, name='contact_complete'),
]