from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Email
from .forms import EmailForm

class CreateMail(CreateView):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('mail_sender:mail_list')
    template_name = 'form.html'


class ListMail(ListView):
    model = Email
    context_object_name = 'mail_list'
    template_name = 'mail_list.html'