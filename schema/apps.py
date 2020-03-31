from django.apps import AppConfig
from watson import search as watson

class SchemaConfig(AppConfig):
    name = 'schema'
    def ready(self):
        # Index public data for searching
        CameraModel = self.get_model("CameraModel")
        LensModel = self.get_model("LensModel")
        Battery = self.get_model("Battery")
        Developer = self.get_model("Developer")
        FilmStock = self.get_model("FilmStock")
        Manufacturer = self.get_model("Manufacturer")
        Mount = self.get_model("Mount")
        PaperStock = self.get_model("PaperStock")
        Toner = self.get_model("Toner")

        watson.register(CameraModel)
        watson.register(LensModel)
        watson.register(Battery)
        watson.register(Developer)
        watson.register(FilmStock)
        watson.register(Manufacturer)
        watson.register(Mount)
        watson.register(PaperStock)
        watson.register(Toner)
