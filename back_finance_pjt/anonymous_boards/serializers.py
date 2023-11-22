from rest_framework import serializers
from .models import Board, Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class BoardTitleSerializer(serializers.ModelSerializer):
        username = serializers.CharField(source='user.username', read_only=True)
        class Meta():
            model = Board
            fields = ('id', 'title', 'username')
            read_only_fields=('user',)
            
    board = BoardTitleSerializer(read_only=True)
    
    class Meta():
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)


class BoardSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta():
        model = Board
        fields = '__all__'
        read_only_fields = ('user', 'user_name',)

