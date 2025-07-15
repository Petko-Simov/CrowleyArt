from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password



class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user_object(self, username: str, email: str, password: str, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = self.normalize_username(username)

        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def _create_user(self, username: str, email: str, password: str, **extra_fields):
        user = self._create_user_object(username, email, password, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, username: str = None, password: str = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email: str, username: str = None, password: str = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

    @staticmethod
    def normalize_username(username: str) -> str:
        return username
