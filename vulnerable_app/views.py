from django.shortcuts import render
from .models import Message

# Ensure you have the csrf_exempt decorator if you're intentionally introducing the vulnerability
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for educational purposes due to the assignment's requirements
def message_view(request):
    if request.method == "POST":
        message_content = request.POST.get('content', '')
        Message.objects.create(content=message_content)

    messages = Message.objects.all()
    return render(request, 'vulnerable_app/message_form.html', {'messages': messages})