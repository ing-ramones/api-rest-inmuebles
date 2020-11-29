from real_estate_api.serializers import EstateSerializer
from real_estate_api.models import Estate, Company
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def estateList(request):
    estate = Estate.objects.all()
    serializer = EstateSerializer(estate, many=True)
    return Response(serializer.data)


"""
@api_view(['GET'])
def estateFindById(request, pk):
    estate = Estate.objects.get(id=pk)
    serializer = EstateSerializer(estate, many=False)
    return Response(serializer.data)


@api_view(['POST'])
# @schema(CustomSchema())
def estateCreate(request):
    serializer = EstateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def estateUpdateById(request, pk):

    estate = Estate.objects.get(id=pk)
    serializer = EstateSerializer(instance=estate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)"""
