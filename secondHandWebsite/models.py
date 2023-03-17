from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField(max_length=20)
    password=models.CharField(max_length=20)
    category=models.IntegerField(max_length=5)
    email=models.CharField(max_length=30)
    mark=models.IntegerField(max_length=5)

    def __str__(self):
        return self.name,self.id,self.password,self.category,self.email

class items(models.model):
    item_id=models.IntegerField(max_length=30)
    item_price=models.IntegerField(max_length=10)
    item_detail=models.CharField(max_length=300)
    item_name=models.CharField(max_length=100)
    item_posttime=models.DateTimeField(auto_now=True)
    item_address=models.CharField(max_length=300)
    item_onwer_userid=models.IntegerField(max_length=30)
    item_state=models.IntegerField(max_length=5)

    def __str__(self):
        return self.item_id,self.item_price,self. item_detail,self.item_name,self.item_posttime,self.item_address,self.item_onwer_userid




class order(models.Model):
    orderid=models.IntegerField(max_length=30)
    order_userid=models.IntegerField(max_length=30)
    order_item_id=models.IntegerField(max_length=30)
    order_mark=models.IntegerField(max_length=10)
    order_bought_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_bought_time,self.order_mark,self.order_item_id,self.order_userid,self.orderid