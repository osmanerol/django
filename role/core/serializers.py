from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from core.models import Seller, Buyer

class SellerCustomRegistrationSerializer(RegisterSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    area = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(SellerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'area' : self.validated_data.get('area', ''),
                'address' : self.validated_data.get('address', ''),
                'description': self.validated_data.get('description', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(SellerCustomRegistrationSerializer, self).save(request)
        user.is_seller = True
        user.save()
        seller = Seller(seller=user, area=self.cleaned_data.get('area'), 
                address=self.cleaned_data.get('address'),
                description=self.cleaned_data.get('description'))
        seller.save()
        return user


class BuyerCustomRegistrationSerializer(RegisterSerializer):
    buyer = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    country = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(BuyerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'country' : self.validated_data.get('country', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(BuyerCustomRegistrationSerializer, self).save(request)
        user.is_buyer = True
        user.save()
        buyer = Buyer(buyer=user,country=self.cleaned_data.get('country'))
        buyer.save()
        return user