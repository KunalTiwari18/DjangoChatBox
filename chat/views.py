from django.shortcuts import render, redirect
from .models import Message

def chat_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        Message.objects.create(name=name, content=content)
        return redirect('chat')

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat.html', {'messages': messages})