from rest_framework import viewsets
from .serializers import PolicySerializer
from .models import Policy


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
