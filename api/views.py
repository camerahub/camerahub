from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from api.serializers import FilmSerializer, NegativeSerializer, ScanSerializer, PrintSerializer, LensSerializer, CameraSerializer
from api.serializers import ManufacturerSerializer, ArchiveSerializer, BatterySerializer, ConditionSerializer, ExposureProgramSerializer, FilterSerializer, NegativeSizeSerializer, FormatSerializer, FlashModelSerializer, FlashSerializer, EnlargerModelSerializer, EnlargerSerializer, MeteringModeSerializer, MountSerializer, PaperStockSerializer, PersonSerializer, ProcessSerializer, TeleconverterModelSerializer, TeleconverterSerializer, TonerSerializer, FilmStockSerializer, BulkFilmSerializer, MountAdapterSerializer, ShutterSpeedSerializer, DeveloperSerializer, LensModelSerializer, CameraModelSerializer, AccessorySerializer, LensSerializer, CameraSerializer, FilmSerializer, NegativeSerializer, PrintSerializer, ToningSerializer, ScanSerializer, OrderSerializer
from schema.models import Accessory, Archive,  Battery, Camera, CameraModel, Condition, ExposureProgram, Filter, NegativeSize, Film, Format
from schema.models import FlashModel, Flash, EnlargerModel, Enlarger, LensModel, Manufacturer, MeteringMode, Mount, Negative, PaperStock
from schema.models import Person, Process, TeleconverterModel, Teleconverter, Toner, FilmStock, BulkFilm, MountAdapter, ShutterSpeed, Developer
from schema.models import Lens, Print, Toning, Scan, Order


class FilmViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows films to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
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


class NegativeViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows negatives to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Negative.objects.none()
    serializer_class = NegativeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Negative.objects.filter(owner=self.request.user)
        else:
            qs = Negative.objects.none()
        return qs


class ScanViewSet(ModelViewSet):
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


class PrintViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows prints to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Print.objects.none()
    serializer_class = PrintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Print.objects.filter(owner=self.request.user)
        else:
            qs = Print.objects.none()
        return qs


class CameraViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows cameras to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Camera.objects.none()
    serializer_class = CameraSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Camera.objects.filter(owner=self.request.user)
        else:
            qs = Camera.objects.none()
        return qs


class LensViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows lens to be viewed.
    Actions provided by the ReadOnlyModelViewSet class: .list(), .retrieve()
    """
    queryset = Lens.objects.none()
    serializer_class = LensSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Lens.objects.filter(owner=self.request.user)
        else:
            qs = Lens.objects.none()
        return qs


class ArchiveViewSet(ModelViewSet):
    queryset = Archive.objects.none()
    serializer_class = ArchiveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Archive.objects.filter(owner=self.request.user)
        else:
            qs = Archive.objects.none()
        return qs

class FlashViewSet(ModelViewSet):
    queryset = Flash.objects.none()
    serializer_class = FlashSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Flash.objects.filter(owner=self.request.user)
        else:
            qs = Flash.objects.none()
        return qs

class EnlargerViewSet(ModelViewSet):
    queryset = Enlarger.objects.none()
    serializer_class = EnlargerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Enlarger.objects.filter(owner=self.request.user)
        else:
            qs = Enlarger.objects.none()
        return qs

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.none()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Person.objects.filter(owner=self.request.user)
        else:
            qs = Person.objects.none()
        return qs

class TeleconverterViewSet(ModelViewSet):
    queryset = Teleconverter.objects.none()
    serializer_class = TeleconverterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Teleconverter.objects.filter(owner=self.request.user)
        else:
            qs = Teleconverter.objects.none()
        return qs

class BulkFilmViewSet(ModelViewSet):
    queryset = BulkFilm.objects.none()
    serializer_class = BulkFilmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = BulkFilm.objects.filter(owner=self.request.user)
        else:
            qs = BulkFilm.objects.none()
        return qs

class MountAdapterViewSet(ModelViewSet):
    queryset = MountAdapter.objects.none()
    serializer_class = MountAdapterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = MountAdapter.objects.filter(owner=self.request.user)
        else:
            qs = MountAdapter.objects.none()
        return qs

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.none()
    serializer_class = AccessorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Accessory.objects.filter(owner=self.request.user)
        else:
            qs = Accessory.objects.none()
        return qs

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.none()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Order.objects.filter(owner=self.request.user)
        else:
            qs = Order.objects.none()
        return qs

class ToningViewSet(ModelViewSet):
    queryset = Toner.objects.none()
    serializer_class = ToningSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = Toning.objects.filter(owner=self.request.user)
        else:
            qs = Toning.objects.none()
        return qs


# Public objects: read-only and world-readable
class ManufacturerViewSet(ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class BatteryViewSet(ReadOnlyModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer

class ConditionViewSet(ReadOnlyModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ExposureProgramViewSet(ReadOnlyModelViewSet):
    queryset = ExposureProgram.objects.all()
    serializer_class = ExposureProgramSerializer

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

class MeteringModeViewSet(ReadOnlyModelViewSet):
    queryset = MeteringMode.objects.all()
    serializer_class = MeteringModeSerializer

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

class ShutterSpeedViewSet(ReadOnlyModelViewSet):
    queryset = ShutterSpeed.objects.all()
    serializer_class = ShutterSpeedSerializer

class DeveloperViewSet(ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class LensModelViewSet(ReadOnlyModelViewSet):
    queryset = LensModel.objects.all()
    serializer_class = LensModelSerializer

class CameraModelViewSet(ReadOnlyModelViewSet):
    queryset = CameraModel.objects.all()
    serializer_class = CameraModelSerializer

class FilterViewSet(ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
