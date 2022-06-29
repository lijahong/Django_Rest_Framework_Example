from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from review.serializer import ReviewSerializers
from review.models import Review

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get_queryset(self): #오버라이딩할 method
        qs = super().get_queryset() #부모의 get_queryset()을 가져온다
        search_score = self.request.query_params.get('score',) #django에서 request.GET.get으로 사용
        if search_score: #search_name이 있다면
            qs = qs.filter(score__icontains = search_score)#원하는 목록만 filter로 가져온다
        return qs

    @action(detail=False, methods=['get'] , url_path="search/(?P<score>[^/.]+)") #detail이 true면 하나 조회, false면 목록, method에는 허용할 method들 정의
    def abc(self, request, score=None): #name이 없다면 None으로 처리
        qs = self.get_queryset().filter(score__icontains=score)  #모델을 검색하여 뽑아온다
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)