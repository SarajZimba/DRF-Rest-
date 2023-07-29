from rest_framework import serializers

from letsdoit.models import Item

class letsdoitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields = '__all__'
        
