from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    bank_account = models.CharField(max_length=20, null=True, blank=True)


class Document(models.Model):
    class Type(models.TextChoices):
        BILL = ("BILL", _("Lasku"))
        RECEIPT = ("RECEIPT", _("Kuitti"))
        CALCULATION = ("CALCULATION", _("Laskelma"))
        OTHER = ("OTHER", _("Muu"))

    created_at = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=20, choices=Type.choices)
    document_file = models.FileField(upload_to="docs/%Y-%m/")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", 
        blank=True, 
        related_name="children",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Transaction(models.Model):
    class Type(models.TextChoices):
        INCOME = ("IN", _("Tulo"))
        EXPENSE = ("EXP", _("Meno"))

    class State(models.TextChoices):
        PENDING = ("PENDING", _("Tuleva"))
        COMPLETE = ("COMPLETE", _("Tapahtunut"))
    
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=Type.choices)
    transaction_state = models.CharField(max_length=10, choices=State.choices)
    transaction_date = models.DateField()
    transaction_category = models.ForeignKey(
        Category, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
    )
    transaction_documents = models.ManyToManyField(
        Document, 
        related_name="transactions",
        blank=True,
    )
    

