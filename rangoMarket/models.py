from django.db import models
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mark = models.IntegerField(max_length=2, )


class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post_items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " <from> " + self.seller.username


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"Image for {self.item.title}"


class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('FINISHED', 'Finished'),
        ('CANCELLED', 'Cancelled'),
    )
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_orders')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_orders')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.__str__() + " <from> " + self.seller.username \
            + " <to> " + self.buyer.username + " <status> " + self.status

















# class user(models.Model):
#     name = models.CharField(max_length=30)
#     id = models.IntegerField(max_length=20)
#     password=models.CharField(max_length=20)
#     category=models.IntegerField(max_length=5)
#     email=models.CharField(max_length=30)
#     mark=models.IntegerField(max_length=5)
#
#     def __str__(self):
#         return self.name,self.id,self.password,self.category,self.email
#
# class items(models.model):
#     item_id=models.IntegerField(max_length=30)
#     item_price=models.IntegerField(max_length=10)
#     item_detail=models.CharField(max_length=300)
#     item_name=models.CharField(max_length=100)
#     item_posttime=models.DateTimeField(auto_now=True)
#     item_address=models.CharField(max_length=300)
#     item_onwer_userid=models.IntegerField(max_length=30)
#     item_state=models.IntegerField(max_length=5)
#
#     def __str__(self):
#         return self.item_id,self.item_price,self. item_detail,self.item_name,self.item_posttime,self.item_address,self.item_onwer_userid
#
#
#
#
# class order(models.Model):
#     orderid=models.IntegerField(max_length=30)
#     order_userid=models.IntegerField(max_length=30)
#     order_item_id=models.IntegerField(max_length=30)
#     order_mark=models.IntegerField(max_length=10)
#     order_bought_time=models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.order_bought_time,self.order_mark,self.order_item_id,self.order_userid,self.orderid