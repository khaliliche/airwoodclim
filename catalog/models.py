from django.db import models
from django.urls import reverse


class Category(models.Model):
    CLIMATISEUR = 'climatiseur'
    SERVICE = 'service'
    TYPE_CHOICES = [
        (CLIMATISEUR, 'Climatiseur'),
        (SERVICE, 'Service'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=CLIMATISEUR)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    brand = models.CharField(max_length=100, blank=True)
    capacity_btu = models.PositiveIntegerField(
        blank=True, null=True,
        help_text="Capacite en BTU (laisser vide pour un service)"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.slug])