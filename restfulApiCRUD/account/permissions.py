from rest_framework.permissions import BasePermission

class NotAuthenticated(BasePermission):
    message= 'You already have an account.'
    def has_permission(self, request, view): # her halukarda tetiklenir, sayfayi da goremez
        return not request.user.is_authenticated