from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer
from schema.models import Film, Negative, Scan

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Film.objects.none()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Film.objects.filter(owner=self.request.user)
        else:
            qs = Film.objects.none()
        return qs

class NegativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows negatives to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Negative.objects.none()
    serializer_class = NegativeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self .request.data and self.request.data['film']:
                qs = Negative.objects.filter(owner=self.request.user, id_owner=self.request.data['film'])
            else:
                qs = Negative.objects.filter(owner=self.request.user)
        else:
            qs = Negative.objects.none()
        return qs

class ScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scans to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Scan.objects.none()
    serializer_class = ScanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Scan.objects.filter(owner=self.request.user)
        else:
            qs = Scan.objects.none()
        return qs
