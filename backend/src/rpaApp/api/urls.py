#""" from django.urls import path

#from rpaviews import Ar """

from django.urls import path
from rpaApp.api.views import PersonaDetailView, PersonaListView


urlpatterns = [
    path('', PersonaListView.as_view()),
    path('<pk>', PersonaDetailView.as_view()),
]
