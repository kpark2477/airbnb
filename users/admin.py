from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as room_models
from . import models

# Register your models here.


class RoomInline(admin.StackedInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )


"""
admin.site.register(Models.User, CustomerUserAdmin)

above decorator can be replaced with this code.
Basically we resister a model to the admin and customize the admin to manipulate that model.

"""
