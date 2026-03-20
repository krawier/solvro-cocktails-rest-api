from django.shortcuts import render
from rest_framework import generics
from .models import Cocktail, Ingredient
from.serializers import CocktailSerializer, IngredientSerializer

# cocktail views

class CocktailListCreateView(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


# ingedient views

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer    

