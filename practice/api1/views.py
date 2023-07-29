from rest_framework.response  import Response
from rest_framework.decorators  import api_view
from letsdoit.models import Item1
from .serializers import mySerializers

@api_view(['GET'])
def getItem(request):
    items = Item1.objects.all()
    serializers = mySerializers(items, many=True)
    return Response(serializers.data)
@api_view(['POST'])
def addItem(request):
    serializer = mySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # items = Item1.objects.all()
    # serializers = mySerializers(items, many=True)
    return Response(serializer.data)

