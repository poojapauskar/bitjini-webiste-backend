from rest_framework import serializers
from users.models import Users
import random
from random import randint
import json
import time


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('pk','name', 'email', 'phone','project_description','domain')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        objects=Users.objects.create(name=validated_data.get('name'),email=validated_data.get('email'),phone=validated_data.get('phone'),project_description=validated_data.get('project_description'),domain=validated_data.get('domain'))
        # print >> sys.stderr, objects
        
        msg1="Thank You for contacting Bitjini. We will get back to you soon."
        msg2=validated_data.get('name')+" with email "+validated_data.get('email')+" and phone "+validated_data.get('phone')+" has contacted Bitjini. Project description is as follows "+validated_data.get('project_description')+" .Interested domain "+validated_data.get('domain')

        from django.core.mail import send_mail
        send_mail('Bitjini: ',msg1, 'poojapauskar22@gmail.com', [validated_data.get('email')], fail_silently=False)


        from django.core.mail import send_mail
        send_mail('Bitjini: ',msg2, 'poojapauskar22@gmail.com', ['contact@bitjini.com'], fail_silently=False)




        return objects

