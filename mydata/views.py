from django.shortcuts import render, redirect
from .forms import MessageForm
from django.core.mail import send_mail
from django.conf import settings
from Web_core.settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'home.html')



def portfolio(request):
    links=[
        {'id':'home', 'name':'Home'},
        {'id':'about', 'name':'About'},
        {'id':'skills', 'name':'Skills'},
        {'id':'contact', 'name':'Contact'}, 
    ]
    if request.method=="POST":
        contact_form=MessageForm(request.POST)
        name=request.POST.get("name")
        username=request.POST.get("username")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        
        sender = f'{name}<{username}>'
        send_mail(
            subject,
            message,
            from_email= sender,
            recipient_list=['r51appiah@gmail.com'],
            fail_silently=False,
        )
        success= name + "your message hass been sucessfully submitted."
        return HttpResponse(success)
        
    else:
        contact_form=MessageForm()
        
    logo ='DjangoStudio'
    context={'links':links,'logo':logo,'contact_form':contact_form}
    return render(request, 'portfolio.html',context)

