from django.db import models

from djangoproject.common.models import BaseModel
from djangoproject.product.models.product import Product

class CurrencyChoices(models.TextChoices):
    KRW = "KRW", "₩"
    USD = "USD", "$"
    EUR = "EUR", "€"

class ProductPrice(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="상품 ID", related_name="price")
    base_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="기본 가격")
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="할인 가격")
    cost_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="원가 (관리용)")
    currency = models.CharField(max_length=10, choices=CurrencyChoices.choices, default="KRW", verbose_name="통화")
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, verbose_name="세율")

    class Meta:
        verbose_name = "상품 가격"
