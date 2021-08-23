from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from django.views import View
from .models import GitUser, Repository
from .forms import GitUserForm, RepositoryForm
from .logics import check_user_in_bd, get_data_and_create_instance, handler_logic
import json


def get_info_gituser(request):
    data = {}
    if request.POST:
        form = GitUserForm(request.POST)
        username = form.data["username"]
        data = handler_logic(username)
        print(data)
        return render(request, 'app/get_view.html', data)
    else:
        form = GitUserForm()
        data['form'] = form
        return render(request, 'app/get_info_gituser.html', data)


def get_view(request):
    context = {

    }
    return render(request, 'app/get_view.html', context)