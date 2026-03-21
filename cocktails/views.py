from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters, permissions, status
from .models import Cocktail, Ingredient
from.serializers import CocktailSerializer, IngredientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

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


class CocktailFavoriteToggleView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request,pk):
        cocktail = get_object_or_404(Cocktail,pk=pk)
        user = request.user

        if user in cocktail.favorited_by.all():
            cocktail.favorited_by.remove(user)
            return Response({"detail":"Deleted from favourites"},status=status.HTTP_200_OK)
        else:
            cocktail.favorited_by.add(user)
            return Response({"detail":"Added to favourties"}, status=status.HTTP_200_OK)


class FavouriteCocktailListView(generics.ListAPIView):

    serializer_class = CocktailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cocktail.objects.filter(favorited_by=self.request.user)