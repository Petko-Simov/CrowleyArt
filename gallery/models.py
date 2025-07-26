from django.conf import settings
from django.db import models

User =  settings.AUTH_USER_MODEL

class Tattoo(models.Model):
    tattoo_name = models.CharField(
        max_length=50,
    )

    artist = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='Unknown',
        help_text='The tattoo artist; leave blank for “Unknown”.'
    )

    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tattoos',
        help_text='Which user/staff added this entry.'
    )

    image = models.ImageField(
        upload_to='tattoos/',
        help_text='Upload an image of the tattoo.'
    )

    style = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='Unknown',
        help_text='Tattoo style, e.g. Gothic, Realism.'
    )

    description = models.TextField(
        blank=True,
        help_text='Optional description or notes.'
    )

    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text='The price of the tattoo in your currency.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='When this tattoo entry was created.'
    )

    class Meta:
        ordering = ['-created_at',]
        verbose_name = 'Tattoo'
        verbose_name_plural = 'Tattoos'

    def __str__(self) -> str:
        return f"{self.tattoo_name} ({self.style})"
