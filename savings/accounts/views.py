from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from savings.accounts.forms import CreateProfileForm

from savings.common.view_mixins import CustomLoginRequiredMixin
from savings.accounts.models import Profile, SavingsUser


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/profile_login.html'
    success_url = reverse_lazy('dashboard')

    # used to redirect to the correct address
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(CustomLoginRequiredMixin, auth_views.LogoutView):
    # redirect is done through global variable in settings.py
    # or could be done with a next_url attribute in request in html
    # so no need to add anything more here
    pass


class ChangeUserPasswordView(CustomLoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/profile_change_password.html'


class ProfileEditView(CustomLoginRequiredMixin, views.UpdateView):
    # done by the class based view, no form needed if not customized
    model = Profile
    fields = ('first_name', 'last_name', 'budget', 'email',)
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('dashboard')


class UserDeleteView(CustomLoginRequiredMixin, views.DeleteView):
    model = SavingsUser
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('dashboard')
