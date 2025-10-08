
from django.urls import path
from .views import RegisterView, MissaoListCreateView, MissaoRetrUpdDes, LocalListCreateView, LocalRetrUpdDes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('cadastro/', RegisterView.as_view(), name='cadastro'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('missao/', MissaoListCreateView.as_view()),
    path('missao/<int:pk>', MissaoRetrUpdDes.as_view()),
    path('local/', LocalListCreateView.as_view()),
    path('local/<int:pk>', LocalRetrUpdDes.as_view()),
]
