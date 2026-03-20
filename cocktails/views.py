from django.shortcuts import render
from rest_framework import generics, filters
from .models import Cocktail, Ingredient
from.serializers import CocktailSerializer, IngredientSerializer
from django_filters.rest_framework import DjangoFilterBackend

# cocktail views

class CocktailListCreateView(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = ['category', 'ingredients']
    search_fields = ['name','instructions','ingredients__name']
    ordering_fields = ['name']

class CocktailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


# ingedient views

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = ['is_alcoholic', 'cocktail']
    search_fields = ['name','description', 'cocktail__name']
    ordering_fields = ['name']

class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer    

