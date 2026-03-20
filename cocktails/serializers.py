from rest_framework import serializers
from .models import Cocktail,Ingredient,CocktailIngredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','name','description',"is_alcoholic","image"]

class CocktailIngredientSerializer(serializers.ModelSerializer):
    # added so we see more than just the id 
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = CocktailIngredient
        fields = ['ingredient','ingredient_name','amount']

class CocktailSerializer(serializers.ModelSerializer):
    # we want to see the details
    ingredient_detail = CocktailIngredientSerializer(source='cocktailingredient_set',many=True,read_only=True)

    class Meta:
        model = Cocktail
        fields = ['id','name','category','instructions','ingredients_detail']              