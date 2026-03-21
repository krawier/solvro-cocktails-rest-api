from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,null=True)
    is_alcoholic = models.BooleanField(default=True)
    image = models.ImageField(upload_to="ingredients/",blank=True, null=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    instructions = models.TextField()

    #manytomany through table 
    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredient')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    favorited_by = models.ManyToManyField(User, related_name='favorite_cocktails', blank=True)
    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amount} of {self.ingredient.name} in {self.cocktail.name}"