from django.db.models import fields
from rpaApp.models import Persona
from rest_framework import serializers;

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre','apellido','email','domicilio',)