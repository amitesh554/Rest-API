from rest_framework import serializers
from .models import User,Contact

#create serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields= ('id','name','phone_no','email')

class ContactSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Contact
        fields=('name','phone_no','spam_likelyhood')