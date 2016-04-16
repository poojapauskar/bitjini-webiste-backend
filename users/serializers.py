from rest_framework import serializers
from users.models import Users
import random
from random import randint
import json
import time


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('pk','name', 'email', 'phone','address','project_description','domain')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Users.objects.create(name=validated_data.get('name'),email=validated_data.get('email'),phone=validated_data.get('phone'),address=validated_data.get('address'),project_description=validated_data.get('project_description'),doamin=validated_data.get('domain'))
        # print >> sys.stderr, objects
        


        return objects

