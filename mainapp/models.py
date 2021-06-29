from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория', unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='имя')
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(max_length=150, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')

    def __str__(self):
        return f'{self.name} ({self.category.name})'
