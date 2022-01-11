from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, display_name):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        if password is None:
            raise TypeError('Users must have a password')
        if display_name is None:
            raise TypeError('Users must have a display name')

        user = self.model(username=username,
                            display_name=display_name,
                            email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, display_name):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password, display_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=30,
                                unique=True, blank=False,
                                help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                        'Enter a valid username.'
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.', 'invalid'),
                                ],
                                error_messages={
                                    'unique':"A user with that username already exists.",
                                })
    email = models.EmailField(db_index=True, unique=True, blank=False)
    is_staff = models.BooleanField(default=False,
                                    help_text='Designates whether the user can log into this admin site')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(unique=True, max_length=30, blank=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIEL = 'email'
    REQUIRED_FIELDS = ['email', 'display_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"