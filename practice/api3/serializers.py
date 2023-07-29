from rest_framework import serializers
from letsdoit.models import Item3

class mySerializers(serializers.ModelSerializer):
    class Meta:
        model = Item3
        fields = "__all__"