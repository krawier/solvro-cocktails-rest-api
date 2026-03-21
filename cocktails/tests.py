from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Cocktail,Ingredient

class CocktailApiTests(APITestCase):

    def test_get_cocktails_list_returns_200(self):
        url = '/api/cocktails/'
        response =self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_ingredient(self):

        url = '/api/ingredients/'
        data = {'name': 'Wódka', 'is_alcoholic': True}   
        response = self.client.post(url,data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)   
