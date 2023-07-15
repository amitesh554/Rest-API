from django.db import models

#creating users models

class User(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=100)

#creating contact models
#Since email is optional we will not add this field in contact model

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    spam_likelyhood=models.BooleanField(default=0)


