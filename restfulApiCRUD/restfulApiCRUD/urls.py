from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include('post.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/favourite/', include('favourite.urls')),
    path('api/user/', include('account.urls')),
     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
