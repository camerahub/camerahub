from django.apps import AppConfig
from watson import search as watson


class SchemaConfig(AppConfig):
    name = 'schema'

    def ready(self):
        # Index public data for searching
        cameramodel = self.get_model("CameraModel")
        lensmodel = self.get_model("LensModel")
        battery = self.get_model("Battery")
        developer = self.get_model("Developer")
        filmstock = self.get_model("FilmStock")
        manufacturer = self.get_model("Manufacturer")
        mount = self.get_model("Mount")
        paperstock = self.get_model("PaperStock")
        toner = self.get_model("Toner")

        watson.register(cameramodel)
        watson.register(lensmodel)
        watson.register(battery)
        watson.register(developer)
        watson.register(filmstock)
        watson.register(manufacturer)
        watson.register(mount)
        watson.register(paperstock)
        watson.register(toner)
