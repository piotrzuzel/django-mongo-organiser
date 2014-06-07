from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ProcessFormView, FormMixin, CreateView, ModelFormMixin
from django.forms import models as model_forms

from organiser_app.forms import ProfileForm

from organiser_app.models import User, Note


def index(request):
    if request.user.is_authenticated():
        return dashboard_view(request)
    else:
        return render(request, "index.html")


def logout(request):
    auth_logout()
    return index(request)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm(request.POST)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


@login_required()
def dashboard_view(request):
    user = User.objects.get(pk=request.user.id)
    notes = Note.objects.filter(author=user)

    return render(request, "dashboard.html", {"notes": notes})


@login_required
def calendar_view(request):
    pass


@login_required()
def event_view(request):
    pass


@login_required()
def contacts_view(request):
    pass


@login_required()
def contact_view(request):
    pass


@login_required()
def notes_view(request):
    pass


@login_required()
def note_view(requst):
    pass


@login_required()
def myprofile_view(request):
    form = ProfileForm(instance=request.user)
    return render(request, 'myprofile.html', {"form": form})


class RegisterView(TemplateResponseMixin, ModelFormMixin, ProcessFormView):
    form_class = UserCreationForm
    model = User
    success_url = '/login'
    object = User()
    template_name = 'register.html'