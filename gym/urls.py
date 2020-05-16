from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    path("", views.MyView.as_view()),
    path("gyms", views.MyView.as_view()),
    path("coaches", views.CoachView.as_view()),
    path("pricing", views.PricingView.as_view()),
    path("gallery", views.GalleryView.as_view()),
    # path("", views.GymsView.as_view()),
    # path("<int:pk/>", views.GymDetailView.as_view()),
    # path("", views.ServiceView.as_view()),
]