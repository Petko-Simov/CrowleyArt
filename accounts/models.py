from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=50,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # задължително при създаване през createsuperuser

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    nickname = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    is_adult = models.BooleanField(
        default=False,
        verbose_name="Over 18 years old",
    )

    tattoos_made = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name="Tattoos Made (for staff only)"
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    social_media = models.URLField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.nickname.username

