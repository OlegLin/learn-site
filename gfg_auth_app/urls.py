from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.home, name='new'),
    path('google/login/', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('google/emails/', views.fetch_emails, name='fetch_emails'),
]