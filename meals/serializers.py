from rest_framework import serializers
from jwt_auth.serializers import UserSerializer
from .models import Meal, Cuisine, Comment

class MealSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Meal
        fields = ('id', 'name', 'image', 'description', 'cuisine', 'user', 'comments', 'created_at',)


class CuisineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuisine
        fields = ('id', 'name',)

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'created_at',)

class PopulatedCommentSerializer(CommentSerializer):

    user = UserSerializer(read_only=True)

class PopulatedMealSerializer(MealSerializer):

    comments = PopulatedCommentSerializer(many=True)
    user = UserSerializer()
    cuisine = CuisineSerializer()


class PopulatedUserSerializer(UserSerializer):

    meals = MealSerializer(many=True)
