from rest_framework.routers import DefaultRouter
from django.urls import path,include
import product.views


router = DefaultRouter() #url을 자동으로 생성해주는 도구
router.register('product',product.views.ProductViewSet) #viewset class 안의 메소드들의 url을 만들어준다

urlpatterns = [
    path('',include(router.urls)),
]


