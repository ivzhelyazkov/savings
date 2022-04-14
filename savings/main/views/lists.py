from itertools import chain
from django.utils import timezone
from django.views import generic as views

from savings.main.models import Incoming
from savings.main.models import Expense, ExpenseCategory
from savings.common.view_mixins import CustomLoginRequiredMixin


class FilteredIncomingsListView(CustomLoginRequiredMixin, views.ListView):
    paginate_by = 5

    # category changes both the queryset and the url. Categories are dynamic
    def get_queryset(self):
        filter_by = self.kwargs['category'].capitalize()
        if filter_by == 'All':
            return Incoming.objects.filter(user_id=self.request.user.id).order_by('-date')
        elif filter_by == 'Monthly':
            return Incoming.objects.filter(user_id=self.request.user.id) \
                .filter(date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).order_by(
                '-date')
        else:
            return Incoming.objects.filter(user_id=self.request.user.id) \
                .filter(category__name=filter_by).order_by('-date')

    template_name = 'main/lists/incoming_list.html'
    context_object_name = 'incomings_filtered'


class FilteredExpensesListView(CustomLoginRequiredMixin, views.ListView):
    paginate_by = 5

    # type/category/monthly changes both the queryset and the url
    def get_queryset(self):
        filter_by = self.kwargs['category'].capitalize()
        if filter_by == 'All':
            return Expense.objects.filter(user_id=self.request.user.id).order_by('-date')

        elif filter_by == 'Monthly':
            return Expense.objects.filter(user_id=self.request.user.id) \
                .filter(date__gte=timezone.now()
                        .replace(day=1, hour=0, minute=0, second=0, microsecond=0)).order_by('-date')

        elif filter_by in [c.name for c in ExpenseCategory.objects.all()]:
            expense_category = filter_by
            return Expense.objects.filter(user_id=self.request.user.id) \
                .filter(category__name=expense_category).order_by('-date')

        else:
            if '-' in filter_by:
                expense_type = filter_by.split('-')[1].capitalize()
                return Expense.objects.filter(user_id=self.request.user.id) \
                    .filter(type=expense_type) \
                    .filter(date__gte=timezone.now()
                            .replace(day=1, hour=0, minute=0, second=0, microsecond=0)).order_by('-date')
            else:
                expense_type = filter_by
                return Expense.objects.filter(user_id=self.request.user.id) \
                    .filter(type=expense_type).order_by('-date')

    template_name = 'main/lists/expense_list.html'
    context_object_name = 'expenses_filtered'


class ListAllView(CustomLoginRequiredMixin, views.ListView):
    paginate_by = 5

    def get_queryset(self):
        result_list = sorted(
            chain(Expense.objects.filter(user_id=self.request.user.id),
                  Incoming.objects.filter(user_id=self.request.user.id)),
            key=lambda instance: instance.date, reverse=True)

        return result_list

    template_name = 'main/lists/all_list.html'
    context_object_name = 'transactions'


class ListMonthlyView(CustomLoginRequiredMixin, views.ListView):
    paginate_by = 5

    def get_queryset(self):
        result_list = sorted(
            chain(Expense.objects.filter(user_id=self.request.user.id)
                  .filter(date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)),
                  Incoming.objects.filter(user_id=self.request.user.id)
                  .filter(date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0))),
            key=lambda instance: instance.date, reverse=True)
        return result_list

    template_name = 'main/lists/monthly_list.html'
    context_object_name = 'transactions'
