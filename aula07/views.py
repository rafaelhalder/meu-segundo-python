from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse, reverse_lazy

@permission_required('view_carrinho', login_url=reverse_lazy("/login"))
def permission_view(request):
    return HttpResponse("view com permissao")

def index(request):
    next = request.GET.get('next', reverse("login"))
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            next = request.POST.get('next', reverse("login"))
            return HttpResponseRedirect(next)
    contexto = {
        "form": form,
        "next": next,
    }
    return render(request, "aula07/index7.html", context=contexto)


login_required()
def restrita(request):
    return HttpResponse("View Restrita")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

