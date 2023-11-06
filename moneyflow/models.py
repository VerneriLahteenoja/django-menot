from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("aikaleima"))
    class Meta:
        abstract = True

class OwnedModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("omistaja"),
    )
    class Meta:
        abstract = True


class Account(TimestampModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, verbose_name=_("nimi"))
    bank_account = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("pankkitili"))

    class Meta:
        verbose_name = _("tili")
        verbose_name_plural = _("tilit")

    def __str__(self):
        return f"{self.id:04d} {self.name}"

class Document(TimestampModel, OwnedModel):
    class Type(models.TextChoices):
        BILL = ("BILL", _("Lasku"))
        RECEIPT = ("RECEIPT", _("Kuitti"))
        CALCULATION = ("CALCULATION", _("Laskelma"))
        OTHER = ("OTHER", _("Muu"))

    document_type = models.CharField(max_length=20, choices=Type.choices, verbose_name=_("tyyppi"))
    document_name = models.CharField(max_length=100, blank=True, verbose_name=_("nimi"))
    document_file = models.FileField(upload_to="docs/%Y-%m/", verbose_name=_("tiedosto"))

    class Meta:
        verbose_name = _("dokumentti")
        verbose_name_plural = _("dokumentit")

    def __str__(self):
        return self.document_name if self.document_name else f"Document {self.id}"


class Category(TimestampModel, OwnedModel):
    category_name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", 
        blank=True,
        null=True,
        related_name="subcategories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        prefix = f"{self.parent} / " if self.parent else ""
        return f"{prefix}{self.category_name}"
    
    class Meta:
        verbose_name = _("kategoria")
        verbose_name_plural = _("kategoriat")

class Transaction(TimestampModel):
    class Type(models.TextChoices):
        INCOME = ("IN", _("Tulo"))
        EXPENSE = ("EXP", _("Meno"))

    class State(models.TextChoices):
        PENDING = ("PENDING", _("Tuleva"))
        COMPLETE = ("COMPLETE", _("Tapahtunut"))
    
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, verbose_name=_("tili"))
    transaction_type = models.CharField(max_length=10, choices=Type.choices, verbose_name=_("tyyppi"))
    transaction_state = models.CharField(max_length=10, choices=State.choices, verbose_name=_("tila"))
    transaction_date = models.DateField(verbose_name=_("paivays"))
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("maara"))
    transaction_comment = models.CharField(max_length=200, verbose_name=_("kommentti"), blank=True)
    transaction_category = models.ForeignKey(
        Category, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        verbose_name=_("kategoria"),
    )
    transaction_documents = models.ManyToManyField(
        Document, 
        related_name="transactions",
        blank=True,
        verbose_name=_("dokumentit"),
    )

    class Meta:
        verbose_name = _("tilitapahtuma")
        verbose_name_plural = _("tilitapahtumat")
    
    def __str__(self):
        return (
            f"{self.transaction_date} {self.amount:8.2f}"
            f"{self.transaction_comment} ({self.State(self.transaction_state).label})"
            )
