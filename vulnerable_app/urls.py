from django.urls import path
from .views import message_view

urlpatterns = [
    # Existing path for message posting and viewing:
    path('message/', message_view, name='message'),
]