from django.contrib import admin

from .models import Merchant, Transaction


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ("mid", "name", "is_active", "created_at")
    search_fields = ("mid", "name")
    list_filter = ("is_active",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("tid", "merchant", "amount", "currency", "status", "created_at")
    search_fields = ("tid", "merchant__mid", "merchant__name")
    list_filter = ("status", "currency")
