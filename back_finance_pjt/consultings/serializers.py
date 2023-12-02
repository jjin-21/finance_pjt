from rest_framework import serializers
from .models import Consulting, Answer
from django.contrib.auth import get_user_model


class AnswerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class ConsultingTitleSerializer(serializers.ModelSerializer):
        username = serializers.CharField(source='user.username', read_only=True)
        class Meta():
            model = Consulting
            fields = ('id', 'title', 'username')
            read_only_fields=('user',)
            
    consulting = ConsultingTitleSerializer(read_only=True)
    
    class Meta():
        model = Answer
        fields = '__all__'
        read_only_fields = ('user',)


class ConsultingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    answer_set = AnswerSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta():
        model = Consulting
        fields = '__all__'
        read_only_fields = ('user', 'user_name',)

