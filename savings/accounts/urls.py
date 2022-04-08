from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from savings.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileEditView, \
    ChangeUserPasswordView, UserDeleteView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('home')), name='password_change_done'), #
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete profile'),
)