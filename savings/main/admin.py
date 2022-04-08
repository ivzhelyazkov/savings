from django.contrib import admin

from savings.main.models import IncomingCategory, Incoming, ExpenseCategory, Expense


@admin.register(IncomingCategory)
class IncomingCategoryAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('name', 'color')


@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('amount', 'date', 'category', 'user')


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('name', 'color')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('amount', 'date', 'type', 'category', 'user')
