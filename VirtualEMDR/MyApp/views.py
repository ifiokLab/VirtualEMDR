from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request,'MyApp/index.html')


def Chat(request):
    return render(request,'MyApp/chat.html')