from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Gym, Service, Coach, Pricing, Gallery


# class GymsView(View):
#     def get(self, request):
#         gyms = Gym.objects.all()
#         return render(request, "gyms/gym_list.html", {"gym_list": gyms})


# class GymDetailView(View):
#     def get(self, request, pk):
#         gym = Gym.objects.get(id=pk)
#         return render(request, "gyms/gym_detail.html", {"gym": gym})


class MyView(ListView):
    context_object_name = 'gym_list'
    template_name = 'gyms/gym_list.html'
    queryset = Gym.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        # context['services1'] = Service.objects.get(id=1)
        # context['services2'] = Service.objects.get(id=2)
        # context['services3'] = Service.objects.get(id=3)
        context['gyms'] = self.queryset
        return context


class CoachView(View):
    def get(self, request):
        coach = Coach.objects.all()
        return render(request, "gyms/coaches.html", {"coach": coach})


class PricingView(View):
    def get(self, request):
        price = Pricing.objects.all()
        return render(request, "gyms/pricing.html", {"price": price})


class GalleryView(View):
    def get(self, request):
        gallery = Gallery.objects.all()
        return render(request, "gyms/gallery.html", {"gallery": gallery})
