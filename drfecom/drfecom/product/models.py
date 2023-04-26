from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def product_image_path(instance, filename):
    # get the brand name
    brand_name = instance.brand.name
    category_name = instance.category.name
    return f"brands/{brand_name}/{category_name}/{filename}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path, null=True)
    image1 = models.ImageField(upload_to=product_image_path, null=True)
    image2 = models.ImageField(upload_to=product_image_path, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
