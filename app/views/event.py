from app.forms.event import CreateForm, UpdateForm
from app.mixins import MyEventMixin
from app.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
import shutil
from django.conf import settings


class Create(LoginRequiredMixin, generic.CreateView):
    template_name = 'event/create.html'
    model = Event
    success_url = reverse_lazy('app:event_list')
    form_class = CreateForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        kw = {'pk': self.object.pk, }
        return reverse_lazy('app:event_detail', kwargs=kw)


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'event/list.html'
    model = Event

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(organizer=self.request.user)
        queryset = queryset.order_by('date')
        queryset = queryset.reverse()
        return queryset


class Detail(MyEventMixin, generic.DetailView):
    template_name = 'event/detail.html'
    model = Event


class Update(MyEventMixin, generic.UpdateView):
    template_name = 'event/update.html'
    model = Event
    form_class = UpdateForm

    def get_success_url(self):
        kw = {'pk': self.object.pk, }
        return reverse_lazy('app:event_detail', kwargs=kw)


class Delete(MyEventMixin, generic.DeleteView):
    template_name = 'event/delete.html'
    model = Event
    success_url = reverse_lazy('app:event_list')


class DonwloadAllDeck(MyEventMixin, generic.RedirectView):
    def get(self, request, *args, **kwargs):
        event_uuid = self.kwargs['pk']
        shutil.make_archive('./zips/files', 'zip', f"{settings.MEDIA_ROOT}/")
        return super().get(request, *args, **kwargs)
