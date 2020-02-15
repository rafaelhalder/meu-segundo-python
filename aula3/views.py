from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

def index(request):
    html = 'Bem vindo'
    response = HttpResponse(html,status=404)
    response['ultimo'] =  timezone.localtime(timezone.now())
    return response

def setacookie(request):
    response = HttpResponse()
    response.set_cookie('my_name',value='Rafael')
    return response

def redireciona(request):
    return HttpResponseRedirect('https://google.com.br')