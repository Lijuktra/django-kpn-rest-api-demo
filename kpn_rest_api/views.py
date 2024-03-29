from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from kpn-rest-api import serializers



class HelloApiView(APIView):
    """ Test API HelloApiView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns the list of API fetaures """
        an_apiview = [
            'uses the methods as function (get, post, patch , put , delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic'
            'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello a message from Liju!' , 'an_apiview': an_apiview})

    def post(self, request):
        """ create a message with the name"""
        #retrive the data from request and validate and validate the data via serilizer
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request , pk=None):
        """ Handle updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, request , pk=None):
        """ Handle a partial update on an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request , pk=None):
        """ Handle deleting an object"""
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test hallo view set """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hallo view set """
        a_viewset = [
            'Uses actions (list , create, retrieve, update, partial_update)',
            'Automatically maps the urls to a router'
            'provide more funcationality with less code',
        ]
        return Response({'message': 'Hello message from Liju!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
