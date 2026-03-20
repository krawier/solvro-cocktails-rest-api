from django.shortcuts import render
from rest_framework import generics, filters, permissions
from .models import Cocktail, Ingredient
from.serializers import CocktailSerializer, IngredientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorAdminOrReadOnly


# cocktail views

class CocktailListCreateView(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'ingredients']
    search_fields = ['name','instructions','ingredients__name']
    ordering_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CocktailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    permission_classes = [IsAuthorAdminOrReadOnly]


# ingedient views

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = ['is_alcoholic', 'cocktail']
    search_fields = ['name','description', 'cocktail__name']
    ordering_fields = ['name']


class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer    

    permission_classes = [IsAuthorAdminOrReadOnly]
