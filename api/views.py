from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from drf_multiple_serializer import ReadWriteSerializerMixin

from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer, PrintSerializer, LensSerializer, CameraSerializer
from api.serializers import ManufacturerSerializer, ArchiveSerializer, BatterySerializer, FilterSerializer, NegativeSizeSerializer
from api.serializers import FormatSerializer, FlashModelSerializer, FlashSerializer, EnlargerModelSerializer, EnlargerSerializer, MountSerializer
from api.serializers import PaperStockSerializer, PersonSerializer, ProcessSerializer, TeleconverterModelSerializer, TeleconverterSerializer
from api.serializers import TonerSerializer, FilmStockSerializer, BulkFilmSerializer, MountAdapterSerializer, DeveloperSerializer
from api.serializers import LensModelSerializer, CameraModelSerializer, AccessorySerializer, OrderSerializer

from api.rwserializers import FilmRWSerializer, NegativeRWSerializer, ScanRWSerializer, PrintRWSerializer, LensRWSerializer, CameraRWSerializer
from api.rwserializers import ArchiveRWSerializer
from api.rwserializers import FlashRWSerializer, EnlargerRWSerializer
from api.rwserializers import PersonRWSerializer, TeleconverterRWSerializer
from api.rwserializers import BulkFilmRWSerializer
from api.rwserializers import AccessoryRWSerializer, OrderRWSerializer

from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, Developer
from schema.models import Lens, Print, Scan, Order


class FilmViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows films to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Film.objects.none()
    serializer_classes = {
        'read': FilmSerializer,
        'write': FilmRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Film.objects.filter(owner=self.request.user)
        else:
            qs = Film.objects.none()
        return qs


class NegativeViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows negatives to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Negative.objects.none()
    serializer_classes = {
        'read': NegativeSerializer,
        'write': NegativeRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Negative.objects.filter(owner=self.request.user)
        else:
            qs = Negative.objects.none()
        return qs


class ScanViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows scans to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Scan.objects.none()
    serializer_classes = {
        'read': ScanSerializer,
        'write': ScanRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Scan.objects.filter(owner=self.request.user)
        else:
            qs = Scan.objects.none()
        return qs


class PrintViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows prints to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Print.objects.none()
    serializer_classes = {
        'read': PrintSerializer,
        'write': PrintRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Print.objects.filter(owner=self.request.user)
        else:
            qs = Print.objects.none()
        return qs


class CameraViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows cameras to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Camera.objects.none()
    serializer_classes = {
        'read': CameraSerializer,
        'write': CameraRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Camera.objects.filter(owner=self.request.user)
        else:
            qs = Camera.objects.none()
        return qs


class LensViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows lens to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Lens.objects.none()
    serializer_classes = {
        'read': LensSerializer,
        'write': LensRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Lens.objects.filter(owner=self.request.user)
        else:
            qs = Lens.objects.none()
        return qs


class ArchiveViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Archive.objects.none()
    serializer_classes = {
        'read': ArchiveSerializer,
        'write': ArchiveRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Archive.objects.filter(owner=self.request.user)
        else:
            qs = Archive.objects.none()
        return qs


class FlashViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Flash.objects.none()
    serializer_classes = {
        'read': FlashSerializer,
        'write': FlashRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Flash.objects.filter(owner=self.request.user)
        else:
            qs = Flash.objects.none()
        return qs


class EnlargerViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Enlarger.objects.none()
    serializer_classes = {
        'read': EnlargerSerializer,
        'write': EnlargerRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Enlarger.objects.filter(owner=self.request.user)
        else:
            qs = Enlarger.objects.none()
        return qs


class PersonViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Person.objects.none()
    serializer_classes = {
        'read': PersonSerializer,
        'write': PersonRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Person.objects.filter(owner=self.request.user)
        else:
            qs = Person.objects.none()
        return qs


class TeleconverterViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Teleconverter.objects.none()
    serializer_classes = {
        'read': TeleconverterSerializer,
        'write': TeleconverterRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Teleconverter.objects.filter(owner=self.request.user)
        else:
            qs = Teleconverter.objects.none()
        return qs


class BulkFilmViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = BulkFilm.objects.none()
    serializer_classes = {
        'read': BulkFilmSerializer,
        'write': BulkFilmRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = BulkFilm.objects.filter(owner=self.request.user)
        else:
            qs = BulkFilm.objects.none()
        return qs


class MountAdapterViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = MountAdapter.objects.none()
    serializer_classes = {
        'read': MountAdapterSerializer,
        'write': MountAdapterSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = MountAdapter.objects.filter(owner=self.request.user)
        else:
            qs = MountAdapter.objects.none()
        return qs


class AccessoryViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Accessory.objects.none()
    serializer_classes = {
        'read': AccessorySerializer,
        'write': AccessoryRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Accessory.objects.filter(owner=self.request.user)
        else:
            qs = Accessory.objects.none()
        return qs


class OrderViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Order.objects.none()
    serializer_classes = {
        'read': OrderSerializer,
        'write': OrderRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Order.objects.filter(owner=self.request.user)
        else:
            qs = Order.objects.none()
        return qs


# Public objects: read-only and world-readable
class ManufacturerViewSet(ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BatteryViewSet(ReadOnlyModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer


class NegativeSizeViewSet(ReadOnlyModelViewSet):
    queryset = NegativeSize.objects.all()
    serializer_class = NegativeSizeSerializer


class FormatViewSet(ReadOnlyModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class FlashModelViewSet(ReadOnlyModelViewSet):
    queryset = FlashModel.objects.all()
    serializer_class = FlashModelSerializer


class EnlargerModelViewSet(ReadOnlyModelViewSet):
    queryset = EnlargerModel.objects.all()
    serializer_class = EnlargerModelSerializer


class MountViewSet(ReadOnlyModelViewSet):
    queryset = Mount.objects.all()
    serializer_class = MountSerializer


class PaperStockViewSet(ReadOnlyModelViewSet):
    queryset = PaperStock.objects.all()
    serializer_class = PaperStockSerializer


class ProcessViewSet(ReadOnlyModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer


class TeleconverterModelViewSet(ReadOnlyModelViewSet):
    queryset = TeleconverterModel.objects.all()
    serializer_class = TeleconverterModelSerializer


class TonerViewSet(ReadOnlyModelViewSet):
    queryset = Toner.objects.all()
    serializer_class = TonerSerializer


class FilmStockViewSet(ReadOnlyModelViewSet):
    queryset = FilmStock.objects.all()
    serializer_class = FilmStockSerializer


class DeveloperViewSet(ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class LensModelViewSet(ReadOnlyModelViewSet):
    queryset = LensModel.objects.all()
    serializer_class = LensModelSerializer


class CameraModelViewSet(ReadOnlyModelViewSet):
    queryset = CameraModel.objects.all()
    serializer_class = CameraModelSerializer


class FilterViewSet(ReadOnlyModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
