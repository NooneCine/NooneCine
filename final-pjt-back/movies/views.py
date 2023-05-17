from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewSerializer


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    pass


@api_view(['GET', 'POST', 'PUT'])
def movie_detail(request, movie_pk):
    pass