from django.db import models


class Merchant(models.Model):
    mid = models.CharField("Merchant ID (MID)", max_length=15, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.mid})"


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        DECLINED = "DECLINED", "Declined"
        REFUNDED = "REFUNDED", "Refunded"

    merchant = models.ForeignKey(
        Merchant, on_delete=models.PROTECT, related_name="transactions"
    )
    tid = models.CharField("Terminal ID (TID)", max_length=8)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="EGP")
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.tid} - {self.amount} {self.currency} ({self.status})"
