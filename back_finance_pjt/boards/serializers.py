from rest_framework import serializers
from .models import Board, Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta():
        model = Board
        fields = '__all__'
        read_only_fields = ('user',)