from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account

@login_required
def frontpage(request):
    
    accounts = Account.objects.filter(user=request.user)
    context = {
        "accounts": accounts
    }

    return render(request, "moneyflow/index.html", context)