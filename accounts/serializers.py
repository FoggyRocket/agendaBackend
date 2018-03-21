from django.conf import settings
from rest_framework import serializers
from .models import Profile, FastNote
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
		fields = ['username', 'id','email','is_staff','is_superuser']

class BasicUserlserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
#ViewSet
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'




class UserCreateSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address')
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'is_staff',
            'is_superuser',

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
        is_staff = validated_data['is_staff']
        is_superuser = validated_data['is_superuser']
        user_obj = User(
                username = username,
                email = email,
                is_staff = is_staff,
                is_superuser = is_superuser
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

class EditFastNoteSerializer(serializers.ModelSerializer):
	user = BasicUserlserializer(many=False, read_only=True,allow_null = True)
	class Meta:
		model = FastNote
		fields = '__all__'

class FastNoteSerializer(serializers.ModelSerializer):
	user = BasicUserlserializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
	class Meta:
		model = FastNote
		fields = '__all__'

	def create(self,validated_data):
		fastnote= FastNote.objects.create(**validated_data)

		return fastnote
