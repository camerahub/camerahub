from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Field

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, EnlargerModel, FilmStock
from schema.models import Flash, FlashModel, Lens, LensModel
from schema.models import Mount, MountAdapter, Order, PaperStock, Print
from schema.models import Negative, Film, Teleconverter, TeleconverterModel, Toner

# Disable CSRF token for cleaner filter URLs
class CustomFormHelper(FormHelper):
    disable_csrf = True


# These helpers are just for the filter forms


class AccessoryFormHelper(CustomFormHelper):
    model = Accessory
    layout = Layout(
        Row(
            Field('type', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        ),
    )


class ArchiveFormHelper(CustomFormHelper):
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


class BatteryFormHelper(CustomFormHelper):
    model = Battery
    layout = Layout(
        Row(
            Field('chemistry', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class BulkFilmFormHelper(CustomFormHelper):
    model = BulkFilm
    layout = Layout(
        Row(
            Field('format', css_class="form-control-sm"),
            Field('filmstock', css_class="form-control-sm"),
            Field('finished', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )

class CameraFormHelper(CustomFormHelper):
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


class CameraModelFormHelper(CustomFormHelper):
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


class DeveloperFormHelper(CustomFormHelper):
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


class EnlargerModelFormHelper(CustomFormHelper):
    model = EnlargerModel
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('negative_size', css_class="form-control-sm"),
            Field('type', css_class="form-control-sm"),
            Field('light_source', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class EnlargerFormHelper(CustomFormHelper):
    model = Enlarger
    layout = Layout(
        Row(
            Field('enlargermodel', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class FilmStockFormHelper(CustomFormHelper):
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


class FlashModelFormHelper(CustomFormHelper):
    model = FlashModel
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
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )

class FlashFormHelper(CustomFormHelper):
    model = Flash
    layout = Layout(
        Row(
            Field('flashmodel', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class LensFormHelper(CustomFormHelper):
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


class LensModelFormHelper(CustomFormHelper):
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


class MountFormHelper(CustomFormHelper):
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


class MountAdapterFormHelper(CustomFormHelper):
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


class OrderFormHelper(CustomFormHelper):
    model = Order
    layout = Layout(
        Row(
            Field('printed', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class PaperStockFormHelper(CustomFormHelper):
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


class PrintFormHelper(CustomFormHelper):
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


class NegativeFormHelper(CustomFormHelper):
    model = Negative
    #disable_csrf = True
    layout = Layout(
        Row(
            Field('film', css_class="form-control-sm"),
            Field('film__camera', css_class="form-control-sm"),
            Field('lens', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class FilmFormHelper(CustomFormHelper):
    model = Film
    layout = Layout(
        Row(
            Field('filmstock', css_class="form-control-sm"),
            Field('format', css_class="form-control-sm"),
            Field('status', css_class="form-control-sm"),
            Field('camera', css_class="form-control-sm"),
            Field('bulk_film', css_class="form-control-sm"),
            Field('archive', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class TeleconverterFormHelper(CustomFormHelper):
    model = Teleconverter
    layout = Layout(
        Row(
            Field('teleconvertermodel', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class TeleconverterModelFormHelper(CustomFormHelper):
    model = TeleconverterModel
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('mount', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )


class TonerFormHelper(CustomFormHelper):
    model = Toner
    layout = Layout(
        Row(
            Field('manufacturer', css_class="form-control-sm"),
            Field('tags', css_class="form-control-sm"),
            Submit('filter', 'Filter', css_class="form-control-sm"),
        )
    )
