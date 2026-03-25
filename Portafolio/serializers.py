from rest_framework import serializers
from porfolio.models import Project

class portafolioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields='__all__'
