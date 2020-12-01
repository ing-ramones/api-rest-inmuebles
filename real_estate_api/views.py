from real_estate_api.serializers import EstateSerializer, CompanySerializer, EstateGeoHyperlinkedSerializer
from real_estate_api.models import Estate, Company
from rest_framework.response import Response
from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@api_view(['GET'])
def estateList(request):
    estate = Estate.objects.all()
    serializer = EstateSerializer(estate, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def estateFindById(request, pk):
    estate = Estate.objects.get(id=pk)
    serializer = EstateSerializer(estate, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def companyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companyFindById(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)


@swagger_auto_schema(methods=['put'], request_body=EstateSerializer)
@api_view(['PUT'])
def estateUpdateById(request, pk):

    estate = Estate.objects.get(id=pk)
    serializer = EstateSerializer(instance=estate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(methods=['post'], request_body=EstateSerializer)
@api_view(['POST'])
def estateCreate(request):
    serializer = EstateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
    http_method_names = ['post', 'delete']


class EstateGeoHyperlinkedViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateGeoHyperlinkedSerializer
    http_method_names = ['get']
