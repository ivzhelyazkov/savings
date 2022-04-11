from django.contrib import admin

from savings.main.models import IncomingCategory, Incoming, ExpenseCategory, Expense


@admin.register(IncomingCategory)
class IncomingCategoryAdmin(admin.ModelAdmin):
    # inlines =
    list_display = ('name', 'color')


@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'category', 'user')


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'type', 'category', 'user')


# @admin.register(AboutContent)
# class AboutContentAdmin(admin.ModelAdmin):
#     list_display = ('author',)