from django.urls import path
from user.views import CreateUserView, CreateTokenView, \
                       UserLogin


app_name = 'user'

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('login/', UserLogin.as_view(), name='login'),
]
