from glass.api.viewsets import MessageViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('message', MessageViewSet)