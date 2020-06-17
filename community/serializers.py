from rest_framework import serializers
from .models import Article, Comment

from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializer


class ArticleSerializer(serializers.ModelSerializer):
    writer = UserSerializer(required=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'writer', 'movies', 'formatted_created_at', 'formatted_updated_at',)
        read_only_fields = ('id', 'writer', 'formatted_created_at', 'formatted_updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'commenter', 'formatted_created_at', 'formatted_updated_at')
        read_only_fields = ('id', 'commenter', 'formatted_created_at', 'formatted_updated_at',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ArticleSerializer.Meta.fields + ('comments',)
