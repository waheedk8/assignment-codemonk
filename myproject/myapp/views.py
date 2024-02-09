from rest_framework import generics, permissions
from .serializers import ParagraphSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Paragraph

class ParagraphList(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
