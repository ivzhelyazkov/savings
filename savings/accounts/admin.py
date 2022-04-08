from django.contrib import admin

from savings.accounts.models import Profile, SavingsUser


@admin.register(SavingsUser)
class UserAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')
