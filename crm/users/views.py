from rest_framework import permissions, viewsets
from users.models import Client

from users.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer