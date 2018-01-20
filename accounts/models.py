from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete='CASCADE')
    full_name = models.CharField(max_length=140,blank=True, null=True)
    address = models.CharField(max_length=300)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Ingresa los 10 digitos de tu celular")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    avatar = models.ImageField('avatar para tu perfil', upload_to='avatars/', blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def __str__(self):
        return self.user.username
