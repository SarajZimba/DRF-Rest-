from rest_framework import serializers
from letsdoit.models import Item1

class mySerializers(serializers.ModelSerializer):
    class Meta:
        model = Item1
        fields = "__all__"