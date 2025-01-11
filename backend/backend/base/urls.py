from django.urls import path
from .views import RegisterUserView, LoginView, UserListView, EditUserView, DeactivateUserView, ActivateUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/edit/<int:pk>/', EditUserView.as_view(), name='edit-user'),
    path('users/deactivate/<int:pk>/', DeactivateUserView.as_view(), name='deactivate-user'),
     path('users/activate/<int:pk>/', ActivateUserView.as_view(), name='activate-user'),
]

