from rest_framework import serializers
from .models import Board, Comment

class CommentSerializer(serializers.ModelSerializer):
    class BoardTitleSerializer(serializers.ModelSerializer):
        class Meta():
            model = Board
            fields = ('title',)
            
    board = BoardTitleSerializer(read_only=True)
    
    class Meta():
        model = Comment
        fields = '__all__'
        # read_only_fields = ('board',)


class BoardSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    
    class Meta():
        model = Board
        fields = '__all__'
        read_only_fields = ('user',)

