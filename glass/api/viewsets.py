from glass.models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
"""
class MessageViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(query_set, many=True)
        return Response(serializer.data)
"""
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date_now').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()