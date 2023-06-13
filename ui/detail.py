from iommi import html
from .pages import BasePage

class ManufacturerPage(BasePage):
    body = html.h1("Manufacturer detail page")
