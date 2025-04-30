from django.db import models

from djangoproject.common.models import BaseModel
from djangoproject.product.models.product import Product


class ProductDetail(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="상품 ID")
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="무게")
    dimensions = models.JSONField(blank=True, null=True, verbose_name="크기")
    materials = models.TextField(blank=True, verbose_name="소재")
    country_of_origin = models.CharField(max_length=100, blank=True, verbose_name="원산지")
    warranty_info = models.TextField(blank=True, verbose_name="보증 정보")
    care_instructions = models.TextField(blank=True, verbose_name="관리 지침")
    additional_info = models.JSONField(blank=True, null=True, verbose_name="추가 정보")

    class Meta:
        verbose_name = "상품 상세"

    def __str__(self):
        return f"Detail of {self.product.name}"
