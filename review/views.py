from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from review.serializer import ReviewSerializers
from review.models import Review
from rest_framework.views import APIView

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

class ReviewAPIList(APIView):
        def get(self, request): #전체 목록
            qs = Review.objects.all()
            serializer = ReviewSerializers(qs, many=True)
            return Response(serializer.data)
        def post(self, request):
            serializer = ReviewSerializers(data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewAPIDetail(APIView):
        def get(self, request, pk): #단일 Data , pk : primary key
            qs = Review.objects.get(id=pk)
            serializer = ReviewSerializers(qs, many=False)
            return Response(serializer.data)
        def put(self,request, pk):
            qs = Review.objects.get(id=pk)
            serializer = ReviewSerializers(qs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def delete(self, request, pk):
            qs = Review.objects.get(id=pk)
            qs.delete()
            return Response( status=status.HTTP_204_NO_CONTENT_CREATED)