from app.forms.deck import CreateForm, UpdateForm
from app.mixins import MyDeckMixin, MyEventMixin
from app.models import Deck, Event
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib import messages


class Create(generic.CreateView):
    template_name = 'deck/create.html'
    model = Deck
    form_class = CreateForm

    def post(self, request, *args, **kwargs):
        event = Event.objects.get(uuid=self.kwargs['event_uuid'])
        if not event.is_active:
            kw = {'event_uuid': self.kwargs['event_uuid'], }
            url = reverse_lazy('app:deck_create', kwargs=kw)
            return HttpResponseRedirect(url)

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "デッキを登録しました。")

        event = Event.objects.get(uuid=self.kwargs['event_uuid'])

        form.instance.event = event
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        event = Event.objects.get(uuid=self.kwargs['event_uuid'])

        context = super().get_context_data(**kwargs)
        context['event'] = event
        return context

    def get_success_url(self):
        kw = {
            'event_uuid': self.kwargs['event_uuid'],
            'pk': self.object.pk,
        }
        return reverse_lazy('app:deck_detail', kwargs=kw)


class List(MyEventMixin, generic.ListView):
    template_name = 'deck/list.html'
    model = Deck

    def get_context_data(self, **kwargs):
        event = Event.objects.get(pk=self.kwargs['event_uuid'])
        context = super().get_context_data(**kwargs)
        context['event'] = event
        return context

    def get_queryset(self):
        event = Event.objects.get(pk=self.kwargs['event_uuid'])

        queryset = super().get_queryset()
        queryset = queryset.filter(event=event)
        queryset = queryset.order_by('number', 'created_at')
        return queryset


class Detail(generic.DetailView):
    template_name = 'deck/detail.html'
    model = Deck


class Update(MyDeckMixin, generic.UpdateView):
    template_name = 'deck/update.html'
    model = Deck
    form_class = UpdateForm

    def form_valid(self, form):
        messages.success(self.request, "デッキを更新しました。")
        return super().form_valid(form)

    def get_success_url(self):
        kw = {
            'event_uuid': self.kwargs['event_uuid'],
            'pk': self.object.pk,
        }
        return reverse_lazy('app:deck_detail', kwargs=kw)


class Delete(MyDeckMixin, generic.DeleteView):
    template_name = 'deck/delete.html'
    model = Deck

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "デッキを削除しました。")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        kw = {'event_uuid': self.kwargs['event_uuid'], }
        return reverse_lazy('app:deck_list', kwargs=kw)
