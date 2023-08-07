from rest_framework import generics
from owner import serializers
from user import serializers
from user import models
from rest_framework.response import Response


class GetUserListView(generics.ListAPIView):
    serializer_class = serializers.AllUserFormSerializer

    def list(self, request, *args, **kwargs):
        data = models.UserForm.objects.all()
        if not data:
            return Response({'error' : 'data not found'}, status=400)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=200)


class GetAllUserInfoView(generics.ListAPIView):
    serializer_class = serializers.UserFormSerializer

    def list(self, request, *args, **kwargs):
        data = models.UserForm.objects.all()
        if not data:
            return Response({'error' : 'data not found'}, status=400)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=200)


class GetOneUserInfoView(generics.ListAPIView):
    serializer_class = serializers.UserFormSerializer

    def list(self, request, *args, **kwargs):
        contact = request.data.get('contact')
        queryset = models.UserForm.objects.get(contact_no=contact)
        if not queryset:
            return Response({'error' : 'data not found'}, status=400)
        serializer = self.get_serializer(queryset,context={'request':request})
        return Response(serializer.data, status=200)
        

class DeleteUserView(generics.DestroyAPIView):
    queryset= models.UserForm.objects.all()
    serializer_class = serializers.UserFormSerializer

    

        


