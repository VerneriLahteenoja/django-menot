from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account, Document

@login_required
def frontpage(request):
    return render(request, "moneyflow/index.html")

@login_required
def accounts(request):
    accounts = Account.objects.filter(user=request.user)
    context = {
        "accounts": accounts
    }
    return render(request, "moneyflow/account.html", context)

@login_required
def documents(request):
    docs = Document.objects.filter(owner=request.user)
    context = {
        "documents": docs
    }
    return render(request, "moneyflow/documents.html", context)