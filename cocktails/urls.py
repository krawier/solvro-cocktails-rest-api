from django.urls import path
from . import views

urlpatterns =[

    path('cocktails/', views.CocktailListCreateView.as_view(), name='cocktail-list'),
    path('cocktails/<int:pk>/', views.CocktailRetrieveUpdateDestroyView.as_view(), name='cocktail-detail'),
    path('cocktails/<int:pk>/favorite/', views.CocktailFavoriteToggleView.as_view(), name='cocktail-favorite-toggle'),
    path('favorites/', views.FavoriteCocktailListView.as_view(), name='favorite-list'),
    path('ingredients/', views.IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient-detail'),


]