import datetime
import json
import pytest

from real_estate_api.views import CompanyViewSet
from time import strftime

from real_estate_api.models import Estate, Company
from real_estate_api.serializers import EstateSerializer, CompanySerializer
from real_estate_api.urls import urlpatterns

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError

from django.urls import reverse, URLPattern
from django_mock_queries.query import MockSet


class TestCompanyEstateUrl(APITestCase):

    def test_url_exists_at_desired_location(self):
        for url in urlpatterns:
            print(url.pattern.regex.groups)
            # Acepta solo solicitudes GET e ignore las URL que necesitan argumentos.
            if not isinstance(url, URLPattern) or url.pattern.regex.groups or not url.name or url.name.find("detail") == -1 or url.name.find("create") == -1:
                continue

            urlpath = reverse(url.name)
            response = self.client.get(urlpath, follow=True)
            print(urlpath, response.status_code)
            assert response.status_code == status.HTTP_200_OK


class TestCompanyManager:

    def test_get_company_by_created(self, mocker):

        expected_results = [
            Company(name='Inmobiliaria Europa S.A',
                    nif=432827568,
                    created_at=datetime.datetime.now(),
                    last_modified_at=datetime.datetime.now()
                    )
        ]

        date = strftime('%Y-%m-%d')

        # Se crea la consulta con django-mock-queries para crear el Mock QuerySets
        # con el cual logramos omitir la consulta a la base de datos
        qs = MockSet(expected_results[0])

        # Patch el metodo qet_queryset para modificar su comportamiento
        # Se modifica el comportamiento con patch el metodo qet_queryset
        # para que retorne nuestro queryset y no el da la base de datos
        mocker.patch.object(Company.objects, 'get_queryset', return_value=qs)

        result = list(Company.objects.get_company_by_created(date))

        assert result == expected_results
        assert str(result[0]) == expected_results[0].name


class TestCompanySerializer:

    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'name': 'Inmobiliaria Europa S.A',
            'nif': 432827568
        }

        company = Company(**expected_results)
        results = CompanySerializer(company).data

        assert results == expected_results

    @pytest.mark.django_db
    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            'name': 'Inmobiliaria Europa',
        }

        serializer = CompanySerializer(data=incomplete_data)

        # ContextManager para verificar que se ejecute
        # correctamente la Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestViewSet():

    @pytest.mark.urls('real_estate_api.urls')
    def test_list(self, rf, mocker):
        # django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este objeto RequestFactory(rf)
        # y mocker para hacer patch a objetos y funciones
        url = reverse('company-list')
        request = rf.get(url)

        queryset = MockSet(
            Company(id=1, name='Inmobiliaria Europa 1', nif=43282757),
            Company(id=2, name='Inmobiliaria Europa 2', nif=43282758),
            Company(id=3, name='Inmobiliaria Europa 3', nif=43282759)
        )

        mocker.patch.object(CompanyViewSet, 'get_queryset',
                            return_value=queryset)
        response = CompanyViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == status.HTTP_200_OK
        assert len(json.loads(response.content)) == 3


class TestEstateManager:

    def test_get_estate_by_created(self, mocker):

        expected_results = [
            Estate(geom='SRID=4326;POINT(-16.3917103 -151.9053074)',
                   address='Un lugar muy muy lejano',
                   area=1000,
                   rooms=30,
                   garage=True,
                   other={"url": "http://www.borabora.com"},
                   company_id=1,
                   created_at=datetime.datetime.now(),
                   last_modified_at=datetime.datetime.now()
                   )
        ]

        date = strftime('%Y-%m-%d')

        qs = MockSet(expected_results[0])

        mocker.patch.object(Estate.objects, 'get_queryset', return_value=qs)

        result = list(Estate.objects.get_estate_by_created(date))

        assert result == expected_results
        assert str(result[0]) == expected_results[0].address


class TestEstateSerializer:

    def test_expected_serialized_json(self):
        expected_results = {
            "id": 1,
            "geom": "SRID=4326;POINT (50.084068 8.238381)",
            "address": "Un lugar muy muy lejano",
            "area": 100,
            "rooms": 2,
            "garage": True,
            "other": {"url": "http://www.borabora.com"},
            "company_id": 1
        }

        estate = Estate(**expected_results)
        results = EstateSerializer(estate).data

        assert results == expected_results

    @pytest.mark.django_db
    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            "geom": "SRID=4326;POINT (50.084068 8.238381)",
        }

        serializer = EstateSerializer(data=incomplete_data)

        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
