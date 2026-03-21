from rest_framework import serializers
from .models import Cocktail,Ingredient,CocktailIngredient
from django.contrib.auth.models import User


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
    ingredients_detail = CocktailIngredientSerializer(source='cocktailingredient_set',many=True)

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'instructions', 'author_name' ,'ingredients_detail']

    def create(self,validated_data):
            ingredients_data = validated_data.pop('cocktailingredient_set')
            cocktail = Cocktail.objects.create(**validated_data)
            for item in ingredients_data:
                CocktailIngredient.objects.create(
                    cocktail=cocktail,
                    ingredient=item['ingredient'],
                    amount=item['amount']
                )
            
            return cocktail


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create_user(

                username=validated_data['username'],
                email= validated_data.get('email',''),
                password=validated_data['password']
        )
        return user