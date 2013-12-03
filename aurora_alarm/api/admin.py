from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from api.models import UserProfile


# Define an inline admin descriptor for UserProfile model which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    """
    Here we add user profile settings to admin site. Now user profile (threshold, location) can be set
    through django's admin site.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user profiles'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)