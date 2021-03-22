from django.contrib import admin
from core.models import Seller, Buyer, User

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)