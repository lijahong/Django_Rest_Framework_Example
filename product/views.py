from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.serializer import ProductSerializers
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self): #오버라이딩할 method
        qs = super().get_queryset() #부모의 get_queryset()을 가져온다
        search_name = self.request.query_params.get('name',) #django에서 request.GET.get으로 사용
        if search_name: #search_name이 있다면
            qs = qs.filter(name__icontains = search_name)#원하는 목록만 filter로 가져온다
        return qs

    @action(detail=False, methods=['get'],url_path="search/(?P<name>[^/.]+)") #detail이 true면 하나 조회, false면 목록, method에는 허용할 method들 정의
    def abc(self, request, name=None): #name이 없다면 None으로 처리
        qs = self.get_queryset().filter(name__icontains=name)  #모델을 검색하여 뽑아온다
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)
