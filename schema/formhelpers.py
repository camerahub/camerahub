from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Field

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock
from schema.models import Flash, Lens, LensModel
from schema.models import Mount, MountAdapter, Order, PaperStock, Print
from schema.models import Repair, Negative, Film, Teleconverter, Toner

# These helpers are just for the filter forms


class AccessoryFormHelper(FormHelper):
    model = Accessory
    layout = Layout(
        Row(
            Field('type', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        ),
    )


class ArchiveFormHelper(FormHelper):
    model = Archive
    layout = Layout(
        Row(
            Field('type', css_class="form-control-sm"),
            Field('location', css_class="form-control-sm"),
            Field('storage', css_class="form-control-sm"),
            Field('sealed', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class BatteryFormHelper(FormHelper):
    model = Battery
    layout = Layout(
        Row(
            Field('chemistry', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class BulkFilmFormHelper(FormHelper):
    model = BulkFilm
    layout = Layout(
        Row(
            Field('format', css_class="form-control-sm"),
            Field('filmstock', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )

class CameraFormHelper(FormHelper):
    model = Camera
    layout = Layout(
        Row(
            Field('cameramodel__manufacturer', css_class="form-control-sm"),
            Field('cameramodel__mount', css_class="form-control-sm"),
            Field('cameramodel__format', css_class="form-control-sm"),
            Field('cameramodel__negative_size', css_class="form-control-sm"),
            Field('cameramodel__body_type', css_class="form-control-sm"),
            Field('own', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class CameraModelFormHelper(FormHelper):
    model = CameraModel
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('mount', css_class="form-control-sm"),
            Field('format', css_class="form-control-sm"),
            Field('negative_size', css_class="form-control-sm"),
            Field('body_type', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class DeveloperFormHelper(FormHelper):
    model = Developer
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('for_paper', css_class="form-control-sm"),
            Field('for_film', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class EnlargerFormHelper(FormHelper):
    model = Enlarger
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('negative_size', css_class="form-control-sm"),
            Field('type', css_class="form-control-sm"),
            Field('light_source', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class FilmStockFormHelper(FormHelper):
    model = FilmStock
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('colour', css_class="form-control-sm"),
            Field('panchromatic', css_class="form-control-sm"),
            Field('process', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class FlashFormHelper(FormHelper):
    model = Flash
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('pc_sync', css_class="form-control-sm"),
            Field('hot_shoe', css_class="form-control-sm"),
            Field('light_stand', css_class="form-control-sm"),
            Field('manual_control', css_class="form-control-sm"),
            Field('swivel_head', css_class="form-control-sm"),
            Field('tilt_head', css_class="form-control-sm"),
            Field('zoom', css_class="form-control-sm"),
            Field('ttl', css_class="form-control-sm"),
            Field('flash_protocol', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class LensFormHelper(FormHelper):
    model = Lens
    layout = Layout(
        Row(
            Field('lensmodel__manufacturer', css_class="form-control-sm"),
            Field('lensmodel__mount', css_class="form-control-sm"),
            Field('lensmodel__zoom', css_class="form-control-sm"),
            Field('lensmodel__autofocus', css_class="form-control-sm"),
            Field('own', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class LensModelFormHelper(FormHelper):
    model = LensModel
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('mount', css_class="form-control-sm"),
            Field('zoom', css_class="form-control-sm"),
            Field('autofocus', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Field('lens_type', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class MountFormHelper(FormHelper):
    model = Mount
    layout = Layout(
        Row(
            Field('shutter_in_lens', css_class="form-control-sm"),
            Field('type', css_class="form-control-sm"),
            Field('purpose', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class MountAdapterFormHelper(FormHelper):
    model = MountAdapter
    layout = Layout(
        Row(
            Field('camera_mount', css_class="form-control-sm"),
            Field('lens_mount', css_class="form-control-sm"),
            Field('has_optics', css_class="form-control-sm"),
            Field('infinity_focus', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class OrderFormHelper(FormHelper):
    model = Order
    layout = Layout(
        Row(
            Field('printed', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class PaperStockFormHelper(FormHelper):
    model = PaperStock
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('resin_coated', css_class="form-control-sm"),
            Field('colour', css_class="form-control-sm"),
            Field('finish', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class PrintFormHelper(FormHelper):
    model = Print
    layout = Layout(
        Row(
            Field('paper_stock', css_class="form-control-sm"),
            Field('developer', css_class="form-control-sm"),
            Field('fine', css_class="form-control-sm"),
            Field('archive', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class RepairFormHelper(FormHelper):
    model = Repair
    layout = Layout(
        Row(
            Field('camera', css_class="form-control-sm"),
            Field('lens', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class NegativeFormHelper(FormHelper):
    model = Negative
    layout = Layout(
        Row(
            Field('film', css_class="form-control-sm"),
            Field('lens', css_class="form-control-sm"),
            Field('filter', css_class="form-control-sm"),
            Field('metering_mode', css_class="form-control-sm"),
            Field('exposure_program', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class FilmFormHelper(FormHelper):
    model = Film
    layout = Layout(
        Row(
            Field('filmstock', css_class="form-control-sm"),
            Field('format', css_class="form-control-sm"),
            Field('camera', css_class="form-control-sm"),
            Field('developer', css_class="form-control-sm"),
            Field('bulk_film', css_class="form-control-sm"),
            Field('archive', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class TeleconverterFormHelper(FormHelper):
    model = Teleconverter
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('mount', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class TonerFormHelper(FormHelper):
    model = Toner
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )
