from django.urls import path
from django.views.generic import TemplateView

from savings.main.views.generic import HomeView, DashboardView, MonthlyView, AboutPageView
from savings.main.views.expense import AddExpenseView, ExpenseDetailsView, EditExpenseView, DeleteExpenseView
from savings.main.views.incoming import AddIncomingView, IncomingDetailsView, EditIncomingView, DeleteIncomingView
from savings.main.views.lists import FilteredIncomingsListView, FilteredExpensesListView, ListAllView, ListMonthlyView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('monthly/', MonthlyView.as_view(), name='monthly'),

    path('list/all/', ListAllView.as_view(), name='list all'),
    path('list/monthly/', ListMonthlyView.as_view(), name='list monthly'),

    path('incomings/list/<str:category>/', FilteredIncomingsListView.as_view(), name='incomings list'),
    path('incomings/details/<int:pk>/', IncomingDetailsView.as_view(), name='incoming details'),
    path('incomings/add/', AddIncomingView.as_view(), name='add incoming'),
    path('incomings/edit/<int:pk>/', EditIncomingView.as_view(), name='edit incoming'),
    path('incomings/delete/<int:pk>/', DeleteIncomingView.as_view(), name='delete incoming'),

    path('expenses/list/<str:category>/', FilteredExpensesListView.as_view(), name='expenses list'),
    path('expenses/details/<int:pk>/', ExpenseDetailsView.as_view(), name='expense details'),
    path('expenses/add/', AddExpenseView.as_view(), name='add expense'),
    path('expenses/edit/<int:pk>/', EditExpenseView.as_view(), name='edit expense'),
    path('expenses/delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete expense'),

    path('about/', AboutPageView.as_view(), name='about'),
)
