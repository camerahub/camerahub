from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer, PrintSerializer, LensSerializer, CameraSerializer
from schema.models import Film, Negative, Scan, Print, Lens, Camera


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
            if self.request.query_params and self.request.query_params['film_id']:
                qs = Negative.objects.filter(
                    owner=self.request.user, film__pk=self.request.query_params['film_id'])
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
            if self.request.query_params and self.request.query_params['film_id']:
                qs = Scan.objects.filter(
                    owner=self.request.user, id_owner=self.request.query_params['film_id'])
            else:
                qs = Scan.objects.filter(owner=self.request.user)
        else:
            qs = Scan.objects.none()
        return qs


class PrintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prints to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Print.objects.none()
    serializer_class = PrintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.query_params and self.request.query_params['film_id']:
                qs = Print.objects.filter(
                    owner=self.request.user, id_owner=self.request.query_params['film_id'])
            else:
                qs = Print.objects.filter(owner=self.request.user)
        else:
            qs = Print.objects.none()
        return qs


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.none()
    serializer_class = CameraSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.query_params and self.request.query_params['film_id']:
                qs = Camera.objects.filter(
                    owner=self.request.user, id_owner=self.request.query_params['film_id'])
            else:
                qs = Camera.objects.filter(owner=self.request.user)
        else:
            qs = Camera.objects.none()
        return qs


class LensViewSet(viewsets.ModelViewSet):
    queryset = Lens.objects.none()
    serializer_class = LensSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.query_params and self.request.query_params['film_id']:
                qs = Lens.objects.filter(
                    owner=self.request.user, id_owner=self.request.query_params['film_id'])
            else:
                qs = Lens.objects.filter(owner=self.request.user)
        else:
            qs = Lens.objects.none()
        return qs
