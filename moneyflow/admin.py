from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Account, Category, Document, Transaction


# Register your models here.
@admin.register(Account)
class AccountAdmin(ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = [
        "account",
        "transaction_type",
        "transaction_state",
        "transaction_date",
        "amount",
        "transaction_comment",
        "transaction_category"
    ]
    list_display_links = list_display
