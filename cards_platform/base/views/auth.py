from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.models import User
from ..forms import CreateUserForm, UpdateUserForm


def sign_in(request):
    page_type = 'Sign In'
    
    # if request.method == 'POST':
    
    context = {
        'page_type': page_type,
    }
    return render(request, 'base/auth.html',context)
