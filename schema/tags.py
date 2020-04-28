from tagging.registry import register

from schema.models import CameraModel, Developer, FilmStock, LensModel, Manufacturer, Mount, PaperStock, Toner

register(CameraModel)
register(Developer)
register(FilmStock)
register(LensModel)
register(Manufacturer)
register(Mount)
register(PaperStock)
register(Toner)
