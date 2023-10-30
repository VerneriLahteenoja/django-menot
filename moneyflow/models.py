from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class OwnedModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    class Meta:
        abstract = True


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    bank_account = models.CharField(max_length=20, null=True, blank=True)


class Document(TimestampModel, OwnedModel):
    class Type(models.TextChoices):
        BILL = ("BILL", _("Lasku"))
        RECEIPT = ("RECEIPT", _("Kuitti"))
        CALCULATION = ("CALCULATION", _("Laskelma"))
        OTHER = ("OTHER", _("Muu"))

    document_type = models.CharField(max_length=20, choices=Type.choices)
    document_file = models.FileField(upload_to="docs/%Y-%m/")



class Category(OwnedModel):
    category_name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", 
        blank=True, 
        related_name="children",
        on_delete=models.CASCADE,
    )


class Transaction(TimestampModel):
    class Type(models.TextChoices):
        INCOME = ("IN", _("Tulo"))
        EXPENSE = ("EXP", _("Meno"))

    class State(models.TextChoices):
        PENDING = ("PENDING", _("Tuleva"))
        COMPLETE = ("COMPLETE", _("Tapahtunut"))
    
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
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
    

