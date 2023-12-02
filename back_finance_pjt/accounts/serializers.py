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
    FIN_CHOICES = [
        (0, '금융 비관련 업종'),
        (1, '금융 관련 업종'),
    ]
    email = serializers.EmailField(required=True)
    company = serializers.CharField(max_length=20, default='무직')
    is_fin_job = serializers.ChoiceField(choices=FIN_CHOICES, required=True)
    phone_num = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=True)
    asset = serializers.IntegerField(default=0)
    salary = serializers.IntegerField(default=0)
    
    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['company'] = self.validated_data.get('company', '')
        cleaned_data['is_fin_job'] = self.validated_data.get('is_fin_job', '')
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
        user.company = self.cleaned_data.get('company')
        user.is_fin_job = self.cleaned_data.get('is_fin_job')
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
    company= serializers.SerializerMethodField()
    is_fin_job= serializers.SerializerMethodField()
    
    def get_username(self,obj):
        return obj.user.username
    
    def get_nickname(self,obj):
        return obj.user.nickname

    def get_email(self,obj):
        return obj.user.email

    def get_is_fin_job(self,obj):
            return obj.user.is_fin_job

    def get_company(self,obj):
            return obj.user.company
        
    class Meta:
        model = Token
        fields = ('key', 'user', 'username','nickname','email','company','is_fin_job')