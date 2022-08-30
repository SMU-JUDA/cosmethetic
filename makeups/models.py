from config.models import Timestamp
from products.models import Product

import reserve as reserve
from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField

class Makeup(Timestamp):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ImageField(upload_to='reference')

    def get_absolute_url(self):
        return reserve('makeups:makeup_detail', args=[str(self.id)])
