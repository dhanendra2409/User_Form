from django.urls import path
from owner import apis
urlpatterns = [
    path("user-info/", apis.GetUserListView.as_view()),
    path("all-user-info/", apis.GetAllUserInfoView.as_view()),
    path("one-user-info/", apis.GetOneUserInfoView.as_view()),
    path("delete-user/<str:contact>/", apis.DeleteUserView.as_view()),
    
]