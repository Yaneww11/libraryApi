from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from libraryApi.accounts.views import RegisterApiView, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]