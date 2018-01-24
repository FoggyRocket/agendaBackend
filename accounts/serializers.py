from django.conf import settings
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from rest_framework.serializers import (
    CharField,
    EmailField,
    Field,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id','email','is_staff']
#ViewSet
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    #avatar= serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = '__all__'
    # def get_avatar(self, profile ):
    #     request= self.context.get('request')
    #     avatar=profile.avatar.url
    #     return request.build_absolute_uri(avatar)




class UserCreateSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address')
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email= value
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
	            raise ValidationError("This user has already registered.")

        return value

    def validate_password1(self, value):
        data = self.get_initial()
        password1 = data.get("password2")
        password2 = value
        if password1 != password2:
            raise ValidationError("Password does not match")
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise ValidationError("Password does not match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()

    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
