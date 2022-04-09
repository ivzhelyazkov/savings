from django import forms
from savings.common.helpers import BootstrapFormMixin
from savings.main.models import Incoming, IncomingCategory, ExpenseCategory, Expense


class AddIncomingForm(BootstrapFormMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=IncomingCategory.objects)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false here does not persist to database, just returns the object to be created
        incoming = super().save(commit=False)

        incoming.user = self.user

        if commit:
            incoming.save()

        return incoming

    class Meta:
        model = Incoming
        fields = ('amount', 'date', 'category', 'description',)
        labels = {
            'description': 'Description (Optional)',
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter Amount...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Provide Description...'}),
        }


class AddExpenseForm(BootstrapFormMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ExpenseCategory.objects)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false here does not persist to database, just returns the object to be created
        expense = super().save(commit=False)

        expense.user = self.user

        if commit:
            expense.save()

        return expense

    class Meta:
        model = Expense
        fields = ('amount', 'date', 'category', 'type', 'description',)
        labels = {
            'description': 'Description (Optional)',
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter Amount...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Provide Description...'}),
        }


# next 2 are done by the generic class based view
# no form needed really but included to customize with better labels

class EditIncomingForm(forms.ModelForm):
    class Meta:
        model = Incoming
        fields = ('amount', 'date', 'category', 'description',)
        labels = {
            'description': 'Description (Optional)',
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'category', 'type', 'description',)
        labels = {
            'description': 'Description (Optional)',
        }
