from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


class AdList(ListView):
    model = Ad
    template_name = 'ads/ads.html'
    context_object_name = 'ads'
    ordering = '-date'


class AdDetails(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'


class AdNew(CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/new-ad.html'
    success_url = reverse_lazy('ads')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdate(UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad-update.html'
    success_url = reverse_lazy('ads')


class AdDelete(DeleteView):
    model = Ad
    template_name = 'ads/ad_delete.html'
    success_url = reverse_lazy('ads')


class Responses(ListView):
    model = Response
    template_name = 'responses/my_responses.html'
    context_object_name = 'responses'
    ordering = '-date'

    def get_queryset(self):
        user = self.request.user
        return Response.objects.filter(ad__author=user)


class ResponseNew(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'responses/new-response.html'
    success_url = reverse_lazy('ads')

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        ad_id = self.kwargs['ad_id']
        ad = get_object_or_404(Ad, pk=ad_id)
        form.instance.ad = ad
        return super().form_valid(form)


class ResponseDel(DeleteView):
    model = Response
    template_name = 'responses/delete_response.html'
    success_url = reverse_lazy('my_responses')


def accept_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    response.status = 'accepted'
    response.save()
    return redirect('my_responses')
