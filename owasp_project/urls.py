from django.contrib import admin
from django.urls import path
from vulnerable_app.views import message_view  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', message_view, name='home'),  # Use message_view for the root URL
    path('message/', message_view, name='message'),
]

