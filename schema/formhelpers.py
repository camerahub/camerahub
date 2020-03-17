from django.forms import ModelForm
from django import forms
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from crispy_forms import helper, layout, bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Button, Field
from crispy_forms.bootstrap import FormActions, AppendedText, InlineCheckboxes, PrependedText
import sys

from schema.models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from schema.models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from schema.models import Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from schema.models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

# These helpers are just for the filter forms


class AccessoryFormHelper(FormHelper):
    model = Accessory
    layout = Layout(
        Row('type', ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class ArchiveFormHelper(FormHelper):
    model = Archive
    layout = Layout(
        Row('type', 'location', 'storage', 'sealed'),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class BatteryFormHelper(FormHelper):
    model = Battery
    layout = Layout(
        Row(
            'chemistry',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class BulkFilmFormHelper(FormHelper):
    model = BulkFilm
    layout = Layout(
        Row(
            'format',
            'filmstock',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class CameraFormHelper(FormHelper):
    layout = Layout(
        Row(
            'cameramodel__manufacturer',
            'cameramodel__mount',
            'cameramodel__format',
            'cameramodel__negative_size',
            'cameramodel__body_type',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class CameraModelFormHelper(FormHelper):
    layout = Layout(
        Row(
            'manufacturer',
            'mount',
            'format',
            'negative_size',
            'body_type',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class DeveloperFormHelper(FormHelper):
    model = Developer
    layout = Layout(
        Row(
            'manufacturer',
            'for_paper',
            'for_film',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class EnlargerFormHelper(FormHelper):
    model = Enlarger
    layout = Layout(
        Row(
            'manufacturer',
            'negative_size',
            'type',
            'light_source',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class FilmStockFormHelper(FormHelper):
    model = FilmStock
    layout = Layout(
        Row(
            'manufacturer',
            'colour',
            'panchromatic',
            'process',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class FlashFormHelper(FormHelper):
    model = Flash
    layout = Layout(
        Row(
            'manufacturer',
            'pc_sync',
            'hot_shoe',
            'light_stand',
            'manual_control',
            'swivel_head',
            'tilt_head',
            'zoom',
            'ttl',
            'flash_protocol',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class LensFormHelper(FormHelper):
    model = Lens
    layout = Layout(
        Row('lensmodel__manufacturer',
            'lensmodel__mount',
            'lensmodel__zoom',
            'lensmodel__autofocus',
            'lensmodel__fixed_mount'
            ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class LensModelFormHelper(FormHelper):
    model = LensModel
    layout = Layout(
        Row('manufacturer',
            'mount',
            'zoom',
            'autofocus',
            'fixed_mount'
            ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class MountFormHelper(FormHelper):
    model = Mount
    layout = Layout(
        Row(
            'shutter_in_lens',
            'type',
            'purpose',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class MountAdapterFormHelper(FormHelper):
    model = MountAdapter
    layout = Layout(
        Row(
            'camera_mount',
            'lens_mount',
            'has_optics',
            'infinity_focus',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class OrderFormHelper(FormHelper):
    model = Order
    layout = Layout(
        Row(
            'printed',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class PaperStockFormHelper(FormHelper):
    model = PaperStock
    layout = Layout(
        Row(
            'manufacturer',
            'resin_coated',
            'colour',
            'finish',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class PrintFormHelper(FormHelper):
    model = Print
    layout = Layout(
        Row(
            'paper_stock',
            'developer',
            'fine',
            'archive',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class RepairFormHelper(FormHelper):
    model = Repair
    layout = Layout(
        Row(
            'camera',
            'lens',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class NegativeFormHelper(FormHelper):
    model = Negative
    layout = Layout(
        Row(
            'film',
            'lens',
            'filter',
            'metering_mode',
            'exposure_program',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class FilmFormHelper(FormHelper):
    model = Film
    layout = Layout(
        Row(
            'filmstock',
            'format',
            'camera',
            'developer',
            'bulk_film',
            'archive',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class TeleconverterFormHelper(FormHelper):
    model = Teleconverter
    layout = Layout(
        Row(
            'manufacturer',
            'mount',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )


class TonerFormHelper(FormHelper):
    model = Toner
    layout = Layout(
        Row(
            'manufacturer',
        ),
        FormActions(
            Submit('filter', 'Filter'),
        )
    )
