from django.db import models

from inoks.models import Profile, City, District
from inoks.models.Address import Address


class AddressProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
