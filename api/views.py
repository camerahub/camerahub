from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer
from schema.models import Film, Negative, Scan

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited.
    """
    queryset = Film.objects.none()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            mystr = Film.objects.filter(owner=self.request.user)
        else:
            mystr = Film.objects.none()
        return mystr

class NegativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows negatives to be viewed or edited.
    """
    queryset = Negative.objects.none()
    serializer_class = NegativeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.query_params['film']:
            mystr = Negative.objects.filter(owner=self.request.user, id_owner=self.request.query_params['film'])
        else:
            mystr = Negative.objects.none()
        return mystr

class ScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scans to be viewed or edited.
    """
    queryset = Scan.objects.none()
    serializer_class = ScanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            mystr = Scan.objects.filter(owner=self.request.user)
        else:
            mystr = Scan.objects.none()
        return mystr
