from django.urls import reverse_lazy
from django.views import generic as views

from savings.common.view_mixins import CustomLoginRequiredMixin
from savings.main.forms import AddExpenseForm, EditExpenseForm
from savings.main.models import Expense


class ExpenseDetailsView(CustomLoginRequiredMixin, views.DetailView):
    model = Expense
    template_name = 'main/expense/expense_details.html'
    context_object_name = 'expense'


class AddExpenseView(CustomLoginRequiredMixin, views.CreateView):
    template_name = 'main/expense/add_expense.html'
    form_class = AddExpenseForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditExpenseView(CustomLoginRequiredMixin, views.UpdateView):
    # done by the generic class based view, no form needed but included to customize and follow project requirements
    model = Expense
    form_class = EditExpenseForm
    template_name = 'main/expense/edit_expense.html'
    success_url = reverse_lazy('dashboard')


# Simple is better than complex. No custom form needed
class DeleteExpenseView(CustomLoginRequiredMixin, views.DeleteView):
    model = Expense
    template_name = 'main/expense/delete_expense.html'
    success_url = reverse_lazy('dashboard')
