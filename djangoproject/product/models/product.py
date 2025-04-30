from django.db import models
from django.utils.text import slugify

from djangoproject.common.models import BaseModel

class ProductStatus(models.TextChoices):
    ACTIVE = "active", "판매중"
    SOLD_OUT = "sold_out", "품절"
    DELETED = "deleted", "삭제됨"

class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name="상품명")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL 슬러그 (SEO 최적화용)")
    short_description = models.TextField(blank=True, verbose_name="짧은 설명")
    full_description = models.TextField(blank=True, verbose_name="전체 설명 (HTML 허용)")

    seller = models.ForeignKey("seller.Seller", on_delete=models.CASCADE, verbose_name="판매자 ID")
    brand = models.ForeignKey("brand.Brand", on_delete=models.CASCADE, verbose_name="브랜드 ID")

    status = models.CharField(max_length=20, choices=ProductStatus.choices, default=ProductStatus.ACTIVE, verbose_name="상태")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "상품"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
