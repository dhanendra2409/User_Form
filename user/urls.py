from django.urls import path
from user import apis

urlpatterns = [
    path('user-form/',apis.UserFormView.as_view()),
    #path('send-request/',apis.RequestAdminView.as_view()),
]
