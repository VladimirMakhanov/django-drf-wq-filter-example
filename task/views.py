from wq.db.rest.views import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class CustomViewSet(ModelViewSet):
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    ordering_fields = '__all__'

