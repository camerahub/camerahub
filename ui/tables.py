from iommi import Table
from ui.pages import BasePage
from schema import models

class ManufacturerListPage(BasePage):
    table = Table(auto__model=models.Manufacturer, query_from_indexes=True)
