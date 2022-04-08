from django.views import generic as views

from savings.accounts.models import Profile
from savings.common.calculators import get_monthly
from savings.common.view_mixins import RedirectToDashboard, CustomLoginRequiredMixin
from savings.main.models import Incoming, Expense, IncomingCategory, ExpenseCategory


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        number_of_profiles = len(Profile.objects.all())
        incomings = sum(i.amount for i in Incoming.objects.all())
        expenses = sum(e.amount for e in Expense.objects.all())
        budgets = sum(p.budget for p in Profile.objects.all())

        context['profiles'] = number_of_profiles
        context['incomings'] = incomings
        context['expenses'] = expenses
        context['savings'] = (budgets + incomings) - expenses
        return context


class DashboardView(CustomLoginRequiredMixin, views.TemplateView):
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        profile = Profile.objects.get(user=user)
        profile_budget = profile.budget

        user_incomings = Incoming.objects.filter(user_id=user.id)
        incomings_total = sum(i.amount for i in user_incomings)

        user_expenses = Expense.objects.filter(user_id=user.id)
        expenses_total = sum(e.amount for e in user_expenses)
        user_ordinary_expenses = user_expenses.filter(type='Ordinary')
        expenses_ordinary = sum(e.amount for e in user_ordinary_expenses)
        user_extraordinary_expenses = user_expenses.filter(type='Extraordinary')
        expenses_extraordinary = sum(e.amount for e in user_extraordinary_expenses)

        savings_total = (profile_budget + incomings_total) - expenses_total

        incomings_categories = IncomingCategory.objects.all
        expenses_categories = ExpenseCategory.objects.all

        context['profile_name'] = profile.first_name
        context['profile_budget'] = profile_budget

        context['user_incomings'] = len(user_incomings)
        context['incomings_total'] = incomings_total

        context['user_expenses'] = len(user_expenses)
        context['expenses_total'] = expenses_total
        context['expenses_ordinary'] = expenses_ordinary
        context['expenses_extraordinary'] = expenses_extraordinary

        context['savings_total'] = savings_total

        context['incomings_categories'] = incomings_categories
        context['expenses_categories'] = expenses_categories

        return context


class MonthlyView(CustomLoginRequiredMixin, views.TemplateView):
    template_name = 'main/monthly.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        profile = Profile.objects.get(user=user)
        user_incomings = Incoming.objects.filter(user_id=user.id)
        user_expenses = Expense.objects.filter(user_id=user.id)
        user_ordinary_expenses = user_expenses.filter(type='Ordinary')
        user_extraordinary_expenses = user_expenses.filter(type='Extraordinary')
        incomings_categories = IncomingCategory.objects.all
        expenses_categories = ExpenseCategory.objects.all

        monthly_incomings = get_monthly(user_incomings)
        monthly_expenses = get_monthly(user_expenses)
        monthly_ordinary = get_monthly(user_ordinary_expenses)
        monthly_extraordinary = get_monthly(user_extraordinary_expenses)

        monthly_balance = monthly_incomings-monthly_expenses

        context['profile_name'] = profile.first_name
        context['monthly_balance'] = monthly_balance

        context['monthly_incomings'] = monthly_incomings
        context['monthly_expenses'] = monthly_expenses
        context['monthly_ordinary'] = monthly_ordinary
        context['monthly_extraordinary'] = monthly_extraordinary

        context['incomings_categories'] = incomings_categories
        context['expenses_categories'] = expenses_categories

        return context
