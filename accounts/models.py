from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete='CASCADE')
    address = models.CharField(max_length=300)
    email= models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Ingresa los 10 digitos de tu celular")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    avatar = models.ImageField('avatar para tu perfil', upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username
