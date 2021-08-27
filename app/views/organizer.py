from app.forms.organizer import CreateForm, UpdateForm
from app.mixins import MyOrganizerMixin
from app.models import Organizer
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


class Create(generic.CreateView):
    template_name = 'organizer/create.html'
    model = Organizer
    form_class = CreateForm
    success_url = reverse_lazy('app:index')

    def form_valid(self, form):
        respons = super().form_valid(form)

        un = form.cleaned_data.get('username')
        pw = form.cleaned_data.get('password1')
        user = authenticate(username=un, password=pw)
        login(self.request, user)

        return respons


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'organizer/list.html'
    model = Organizer


class Detail(MyOrganizerMixin, generic.DetailView):
    template_name = 'organizer/detail.html'
    model = Organizer


class Update(MyOrganizerMixin, generic.UpdateView):
    template_name = 'organizer/update.html'
    model = Organizer
    form_class = UpdateForm
    success_url = reverse_lazy('app:organizer_list')


class Delete(MyOrganizerMixin, generic.DeleteView):
    template_name = 'organizer/delete.html'
    model = Organizer
    success_url = reverse_lazy('app:organizer_list')
