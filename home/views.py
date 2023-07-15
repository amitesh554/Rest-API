from django.http import JsonResponse
from django.shortcuts import render 
from requests import Response
from rest_framework import viewsets,status,response
from .models import User
from .serializers import UserSerializer,ContactSerializers
from .models import Contact

#Used to show all the users

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def post(self,request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse({'user': serializer.data})
        else:
            return JsonResponse({'errors': serializer.errors}, status=400)
        
class SearchViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializers

    def get(self, request):
        
        q= request.GET['query']

        serializer = ContactSerializers(Contact.objects.filter(name__icontains=q, phone_number__icontains=q), many=True)

        return JsonResponse({'results': serializer.data})


class MarkSpamViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializers
    def post(self, request):

    
        phone_number = request.data.get('phone_number')
        user_id = request.data.get('user_id')   
        try:
            contact = Contact.objects.get(phone_number=phone_number, user_id=user_id) 
            contact.spam_likelihood = 1.0
            contact.save()
            return Response(status=status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

 
            
