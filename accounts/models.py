from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

GENDER = [('man', 'Мужской'), ('woman', 'Женский')]


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    avatar = models.ImageField(null=False, blank=False, upload_to='avatar', verbose_name='Аватар')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'

