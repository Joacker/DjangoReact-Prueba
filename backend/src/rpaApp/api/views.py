from rpaApp.models import Persona
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rpaApp.api.serializers import PersonaSerializer

class PersonaListView(ListAPIView):
    queryset = Persona.objects.all() #
    serializer_class = PersonaSerializer

class PersonaDetailView(RetrieveAPIView):
    queryset = Persona.objects.all() #Persona.objects.all()
    serializer_class = PersonaSerializer