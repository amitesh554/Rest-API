from django.contrib import admin
from django.urls import path,include
from .views import UserViewSet,RegisterViewSet,MarkSpamViewSet,SearchViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'users',UserViewSet,basename='user')
router.register(r'register',RegisterViewSet,basename='registration')
router.register(r'spam',MarkSpamViewSet,basename='MarkasSpam')
router.register(r'search',SearchViewSet,basename='search')

urlpatterns = [
    path('',include(router.urls))
]