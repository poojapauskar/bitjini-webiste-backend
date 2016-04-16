from users.models import Users
from users.serializers import UsersSerializer
from rest_framework import generics
# from users.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class UsersList(generics.ListCreateAPIView):
 queryset = Users.objects.all()
 serializer_class = UsersSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Users.objects.all()
 serializer_class = UsersSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

