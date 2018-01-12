from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id','email','is_staff']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'




class UserCreateSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Los correos electrónicos deben coincidir.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
	            raise ValidationError("Este usuario ya se ha registrado.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Los correos electrónicos deben coincidir.")
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



class UserLoginSerializer(serializers.ModelSerializer):
    #token = CharField(allow_blank=True, read_only=True)
    #username = CharField()
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            #'username',
            'email',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, user):
        user = None
        return user
