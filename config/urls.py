
from django.urls import include
from django.contrib import admin
from django.urls import path
import product.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('product.urls')),
    path('',include('review.urls')),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
]

