import base64
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator


class Url(models.Model):
    url = models.CharField(max_length=250, validators=[URLValidator()], verbose_name='url')
    scheme = models.CharField(max_length=20, blank=True, null=True)
    hostname = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, related_name='urls', blank=True, null=True, on_delete=models.CASCADE, verbose_name='user')
    url_hash = models.CharField(max_length=10, unique=True, db_index=True, blank=True, null=True, verbose_name='url-hash')
    short_url = models.CharField(max_length=250, validators=[URLValidator()], blank=True, null=True, verbose_name='short-url')

    def __str__(self):
        return self.short_url

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_url_hash()
        self.short_url = self.create_short_url()
        super(Url, self).save(*args, **kwargs)

    def generate_url_hash(self):
        url_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:8]
        hash_exist = Url.objects.filter(url_hash=url_hash)
        while hash_exist:
            url_hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:8]
            hash_exist = Url.objects.filter(url_hash=url_hash)
            continue
        url_hash = url_hash.decode('utf-8')
        return url_hash

    def create_short_url(self):
        return self.scheme + '://' + self.hostname + '/' + self.url_hash
