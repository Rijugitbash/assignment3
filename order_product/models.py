from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)  # Corrected the field name from "titel" to "title"
    price = models.FloatField()
    location = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.item_name

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    deliver_status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return f"{self.user.username}'s order for {self.item.item_name}"

