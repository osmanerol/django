from django.urls import path
from core.views import SellerRegistrationView, BuyerRegistrationView
app_name = 'core'

urlpatterns = [
    #Registration Urls
    path('registration/seller/', SellerRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
]