from django.contrib import admin
from .models import *

# this allows for adding ingredients directly 
#when creating the cocktail
class CocktailIngredientInline(admin.TabularInline):
    model = CocktailIngredient
    extra =1

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','is_alcoholic')
    search_fields = ('name',)

@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    search_fields = ('name',)
    inlines = [CocktailIngredientInline]    

