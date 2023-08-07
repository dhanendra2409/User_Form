from rest_framework import generics, parsers
from rest_framework.response import Response
from django.core.mail import send_mail
from .serializers import *
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import * 
from helper.funtions import *
from helper import messages
class UserFormView(generics.CreateAPIView):
    serializer_class = UserFormSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
             errors = serializer.errors
             err = error_message_function(errors)
             return Response(ResponseHandling.failure_response_message(err, {}), status=400)
        serializer.save()
        user_data = serializer.data
        if user_data['want_copy']: 
            send_registration_form_email(user_data)
            return Response(ResponseHandling.success_response_message(messages.FORM_COPY_SHARED, {}),status=200) 
        send_email(user_data)   
        return Response(ResponseHandling.success_response_message(messages.FORM_SUBMITTED, {}),status=200)    

# class RequestAdminView(generics.CreateAPIView):
#     serializer_class = RequestAdminViewSerializer
#     def create(self,request):
#         query = request.data
#         name = query.get('name')
#         choice = query.get('choice')
#         data = query.get('data')
#         to_email = settings.DEFAULT_FROM_EMAIL

#         serializer = self.get_serializer(data=query)
#         if not serializer.is_valid():
#             return Response({'error': 'Please provide right Information'})

#         subject = f"{name} had a request for changes ."
#         message = f"Dear Admin, Please change {name}'s,{choice} to {data} ."
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [to_email]
#         send_mail(subject, message, from_email, recipient_list)
#         return Response({'message': 'Request Submitted'},status=200)        


    
