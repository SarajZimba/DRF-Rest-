from rest_framework.response import Response
from rest_framework.decorators import api_view
from letsdoit.models  import Item3
from .serializers import mySerializers

@api_view(['GET'])
def addData(request):
    items = Item3.objects.all()
    serializer = mySerializers(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def getData(request):
    serializer = mySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # items = Item3.objects.all()
    # serializer = mySerializers(items, many=True)

    return Response(serializer.data)