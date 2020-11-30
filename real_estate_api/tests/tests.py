from real_estate_api.models import Company
from rest_framework.test import APITestCase
from django.urls import reverse
from model_mommy import mommy


class RealEstatesTestClass(APITestCase):

    def setUp(self) -> None:
        mommy.make(Company, _quantity=20)

    def test_endpoint_return_all_companies(self):
        url = '/api/v1/estates/'
        response = self.client.get(url)
        print(response)
        self.assertEquals(
            response.context['object_list'].count(), Company.objects.all().count())
