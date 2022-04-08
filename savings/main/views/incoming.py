from django.urls import reverse_lazy
from django.views import generic as views

from savings.common.view_mixins import CustomLoginRequiredMixin
from savings.main.forms import AddIncomingForm, EditIncomingForm
from savings.main.models import Incoming


class IncomingDetailsView(CustomLoginRequiredMixin, views.DetailView):
    model = Incoming
    template_name = 'main/incoming/incoming_details.html'
    context_object_name = 'incoming'


class AddIncomingView(CustomLoginRequiredMixin, views.CreateView):
    template_name = 'main/incoming/add_incoming.html'
    form_class = AddIncomingForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditIncomingView(CustomLoginRequiredMixin, views.UpdateView):
    # done by the generic class based view, no form needed but included to customize and follow project requirements
    model = Incoming
    form_class = EditIncomingForm
    template_name = 'main/incoming/edit_incoming.html'
    success_url = reverse_lazy('dashboard')


# Simple is better than complex. No custom form needed
class DeleteIncomingView(CustomLoginRequiredMixin, views.DeleteView):
    model = Incoming
    template_name = 'main/incoming/delete_incoming.html'
    success_url = reverse_lazy('dashboard')
