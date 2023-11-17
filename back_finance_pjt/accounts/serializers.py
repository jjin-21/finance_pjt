from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token


class CustomRegisterSerializer(RegisterSerializer):
    GENDER_CHOICES = [
        (0, '남자'),
        (1, '여자'),
    ]
    email = serializers.EmailField(required=True)
    phone_num = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=True)
    asset = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    
    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['phone_num'] = self.validated_data.get('phone_num', '')
        cleaned_data['nickname'] = self.validated_data.get('nickname', '')
        cleaned_data['age'] = self.validated_data.get('age', '')
        cleaned_data['gender'] = self.validated_data.get('gender', '')
        cleaned_data['asset'] = self.validated_data.get('asset', '')
        cleaned_data['salary'] = self.validated_data.get('salary', '')
        return cleaned_data

    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        # fields = '__all__'
        exclude = ('password',
                    'last_login',
                    'is_superuser',
                    'first_name',
                    'last_name',
                    'is_staff',
                    'is_active',
                    'date_joined',
                    'groups',
                    'user_permissions'
                    )


class CustomTokenSerializer(serializers.ModelSerializer):
    username= serializers.SerializerMethodField()
    nickname= serializers.SerializerMethodField()
    email= serializers.SerializerMethodField()
    
    def get_username(self,obj):
        return obj.user.username
    
    def get_nickname(self,obj):
        return obj.user.nickname

    def get_email(self,obj):
        return obj.user.email

    class Meta:
        model = Token
        fields = ('key', 'user', 'username','nickname','email')