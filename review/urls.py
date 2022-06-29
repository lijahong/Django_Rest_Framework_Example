from rest_framework.routers import DefaultRouter
from django.urls import path,include
import review.views


router = DefaultRouter() #url을 자동으로 생성해주는 도구
router.register('review',review.views.ReviewViewSet) #viewset class 안의 메소드들의 url을 만들어준다

urlpatterns = [
    path('',include(router.urls)),
    path('reviewapi/', review.views.ReviewAPIList.as_view()),
    path('reviewapi/<int:pk>/', review.views.ReviewAPIDetail.as_view())
]

