from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

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

def show_code(request,code):
    return HttpResponseRedirect(f'https://http.cat/{code}')

def show_get_values(request):
    nome = request.GET.get('nome',None)
    if nome is None:
        html = '<h1>Bem Vindo anonimo</h1>'
    else:
        html = f'<h1>Bem vindo{nome}</h1>'
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ""
    if(request.method == "POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        head = f'<h1>Bem vindo {fname} {lname}</h1>'

    #import ipdb; ipdb.set_trace()
    html = """
        <form method=POST>
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="John"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Doe"><br><br>
        <input type="submit" value="Submit">
        </form> 
    """
    html_to_response = head + html
    return HttpResponse(html_to_response)