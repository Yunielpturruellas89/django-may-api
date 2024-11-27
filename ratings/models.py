from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Assuming you use Django's auth system
from product.models import Product # Import your Product model


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      unique_together = [['user', 'product']] # prevent a single user from rating the same product twice
      db_table = 'rating'
      
    def __str__(self):
        return f"{self.user} rated {self.product} {self.rating} stars"

        