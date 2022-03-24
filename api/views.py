from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from drf_multiple_serializer import ReadWriteSerializerMixin
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer, PrintSerializer, LensSerializer, CameraSerializer
from api.serializers import ManufacturerSerializer, ArchiveSerializer, BatterySerializer, FilterSerializer, NegativeSizeSerializer
from api.serializers import FormatSerializer, FlashModelSerializer, FlashSerializer, EnlargerModelSerializer, EnlargerSerializer, MountSerializer
from api.serializers import PaperStockSerializer, PersonSerializer, ProcessSerializer, TeleconverterModelSerializer, TeleconverterSerializer
from api.serializers import TonerSerializer, FilmStockSerializer, BulkFilmSerializer, MountAdapterSerializer, DeveloperSerializer
from api.serializers import LensModelSerializer, CameraModelSerializer, AccessorySerializer, OrderSerializer
from api.serializers import ExposureProgramSerializer, MeteringModeSerializer, ShutterSpeedSerializer, ExifSerializer

from api.rwserializers import FilmRWSerializer, NegativeRWSerializer, ScanRWSerializer, PrintRWSerializer, LensRWSerializer, CameraRWSerializer
from api.rwserializers import ArchiveRWSerializer
from api.rwserializers import FlashRWSerializer, EnlargerRWSerializer
from api.rwserializers import PersonRWSerializer, TeleconverterRWSerializer
from api.rwserializers import BulkFilmRWSerializer
from api.rwserializers import AccessoryRWSerializer, OrderRWSerializer

from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Filter, NegativeSize, Film, Format, ExposureProgram
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, MeteringMode, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, Developer
from schema.models import Lens, Print, Scan, Order, ShutterSpeed


class FilmViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows films to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Film.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': FilmSerializer,
        'write': FilmRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Film.objects.filter(owner=self.request.user)


class NegativeViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows negatives to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Negative.objects.none()
    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-f.]+'
    serializer_classes = {
        'read': NegativeSerializer,
        'write': NegativeRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['film', 'frame', 'slug']

    def get_queryset(self):
        return Negative.objects.filter(owner=self.request.user)


class ScanViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows scans to be viewed or edited.
    Actions provided by the ModelViewSet class: .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
    """
    queryset = Scan.objects.none()
    lookup_field = 'uuid'
    lookup_value_regex = '[0-9a-f]{32}'
    serializer_classes = {
        'read': ScanSerializer,
        'write': ScanRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uuid']

    def get_queryset(self):
        return Scan.objects.filter(owner=self.request.user)


class PrintViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows prints to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Print.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': PrintSerializer,
        'write': PrintRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Print.objects.filter(owner=self.request.user)


class CameraViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows cameras to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Camera.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': CameraSerializer,
        'write': CameraRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Camera.objects.filter(owner=self.request.user)


class LensViewSet(ReadWriteSerializerMixin, ModelViewSet):
    """
    API endpoint that allows lens to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Lens.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': LensSerializer,
        'write': LensRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lens.objects.filter(owner=self.request.user)


class ArchiveViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Archive.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': ArchiveSerializer,
        'write': ArchiveRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Archive.objects.filter(owner=self.request.user)


class FlashViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Flash.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': FlashSerializer,
        'write': FlashRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Flash.objects.filter(owner=self.request.user)


class EnlargerViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Enlarger.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': EnlargerSerializer,
        'write': EnlargerRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enlarger.objects.filter(owner=self.request.user)


class PersonViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Person.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': PersonSerializer,
        'write': PersonRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Person.objects.filter(owner=self.request.user)


class TeleconverterViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Teleconverter.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': TeleconverterSerializer,
        'write': TeleconverterRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Teleconverter.objects.filter(owner=self.request.user)


class BulkFilmViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = BulkFilm.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': BulkFilmSerializer,
        'write': BulkFilmRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BulkFilm.objects.filter(owner=self.request.user)


class MountAdapterViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = MountAdapter.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': MountAdapterSerializer,
        'write': MountAdapterSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MountAdapter.objects.filter(owner=self.request.user)


class AccessoryViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Accessory.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': AccessorySerializer,
        'write': AccessoryRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Accessory.objects.filter(owner=self.request.user)


class OrderViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Order.objects.none()
    lookup_field = 'id_owner'
    serializer_classes = {
        'read': OrderSerializer,
        'write': OrderRWSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)


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

class MeteringModeViewSet(ReadOnlyModelViewSet):
    queryset = MeteringMode.objects.all()
    serializer_class = MeteringModeSerializer

class ExposureProgramViewSet(ReadOnlyModelViewSet):
    queryset = ExposureProgram.objects.all()
    serializer_class = ExposureProgramSerializer

class ShutterSpeedViewSet(ReadOnlyModelViewSet):
    queryset = ShutterSpeed.objects.all()
    serializer_class = ShutterSpeedSerializer

class ExifViewSet(ReadOnlyModelViewSet):
    queryset = Scan.objects.none()
    serializer_class = ExifSerializer
    lookup_field = 'uuid'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uuid']

    def get_queryset(self):
        return Scan.objects.filter(owner=self.request.user)
