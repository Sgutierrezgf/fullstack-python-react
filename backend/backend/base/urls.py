# from django.urls import path
# from .views import RegisterUserView, AuthUserView, ListUsersView, EditUserView, DeactivateUserView

# urlpatterns = [
#     path('register/', RegisterUserView.as_view(), name='register'),
#     path('login/', AuthUserView.as_view(), name='login'),
#     path('users/', ListUsersView.as_view(), name='list_users'),
#     path('users/<int:pk>/', EditUserView.as_view(), name='edit_user'),
#     path('users/deactivate/<int:pk>/', DeactivateUserView.as_view(), name='deactivate_user'),
# ]

from django.urls import path
from .views import RegisterUserView, LoginView, UserListView, EditUserView, DeactivateUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/edit/<int:pk>/', EditUserView.as_view(), name='edit-user'),
    path('users/deactivate/<int:pk>/', DeactivateUserView.as_view(), name='deactivate-user'),
]

