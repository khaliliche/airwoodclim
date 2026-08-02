from django.db import models


class WorkPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True, help_text="Optionnel, ex: 'Installation à Casablanca'")
    order = models.PositiveIntegerField(default=0, help_text="Plus petit = affiché en premier")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.caption or f"Photo {self.pk}"


class Testimonial(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(5, 0, -1)]

    name = models.CharField(max_length=100, verbose_name="Nom")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5, verbose_name="Note")
    comment = models.TextField(verbose_name="Avis")
    is_approved = models.BooleanField(default=False, help_text="Coché = visible sur le site")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"