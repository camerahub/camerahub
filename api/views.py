from schema.models import Film
from rest_framework.fields import CurrentUserDefault
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import FilmSerializer


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
