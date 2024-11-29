
# Create your views here.
from rest_framework import viewsets
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated #For authentication
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication # uncomment if you use session/basic authentication

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    #permission_classes = [IsAuthenticated] #Requires authentication to create/update ratings

    # Optionally add these lines if you are using different authentication methods
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
