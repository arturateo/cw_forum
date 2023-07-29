from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm
from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'avatar',
                )
            }
        )
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'is_staff',
                    'avatar',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
