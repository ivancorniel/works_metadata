from functools import cache
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Works
from .serializers import WorkSerializer

class ContributorsView(generics.RetrieveAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer
    lookup_field = 'iswc'
    renderer_classes = [JSONRenderer]

    

