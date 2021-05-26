from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from open_pages.serializers import PageSerializer
from open_pages.models import Pages


# Create your views here.
class ListPageAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Pages.objects.all()
    serializer_class = PageSerializer
