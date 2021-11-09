import glob
import os
import shutil
from pathlib import Path
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generates sets of icons for CameraHub'

    def handle(self):

        # Set up mappings between old and new icon names.
        # One source SVG can be mapped to multiple destination SVGs
        newnames = {
            'icons8-camera-addon': ['accessory'],
            'icons8-collectibles': ['archive'],
            'icons8-battery': ['battery'],
            'icons8-video-trimming': ['bulkfilm'],
            'icons8-camera': ['camera'],
            'icons8-camera-identification': ['condition'],
            'icons8-volume': ['developer'],
            'icons8-industrial-scales': ['enlarger'],
            'icons8-easel': ['exhibition'],
            'icons8-medium-icons': ['exposureprogram'],
            'icons8-film-roll': ['film'],
            'icons8-360-degrees': ['filter'],
            'icons8-camera-flash': ['flash'],
            'icons8-resolution': ['format'],
            'icons8-lens': ['lens'],
            'icons8-factory': ['manufacturer'],
            'icons8-slr-small-lens': ['mount'],
            'icons8-metamorphose': ['mountadapter', 'misc'],
            'icons8-movie': ['negative'],
            'icons8-surface': ['negativesize'],
            'icons8-transaction-list': ['order'],
            'icons8-sheets': ['paperstock'],
            'icons8-user': ['person'],
            'icons8-xlarge-icons': ['print'],
            'icons8-lab-items': ['process'],
            'icons8-jpg': ['scan'],
            'icons8-exposure': ['shutterspeed'],
            'icons8-small-lens': ['teleconverter'],
            'icons8-test-tube': ['toner'],
            'icons8-home': ['home'],
            'icons8-facebook': ['facebook'],
            'icons8-github': ['github'],
            'icons8': ['icons8'],
            'icons8-about': ['about'],
            'icons8-login': ['login'],
            'icons8-add-user-male': ['register'],
            'icons8-sign-in-form-password': ['password'],
            'icons8-bar-chart': ['stats'],
            'icons8-help': ['help'],
            'icons8-edit': ['edit'],
            'icons8-add': ['add'],
            'icons8-cancel': ['no'],
            'icons8-ok': ['yes'],
            'icons8-search-more': ['search'],
            'icons8-price-tag': ['tag'],
            'icons8-ios': ['history'],
            'icons8-color-wheel': ['colour'],
            'icons8-color-wheel-mono': ['bw'],
            'icons8-true-false': ['features'],
            'icons8-weight': ['weight'],
            'icons8-focal-length': ['optics'],
            'icons8-width': ['focus'],
            'icons8-voltmeter': ['meter'],
            'icons8-aperture': ['shutter'],
            'icons8-fast-forward': ['next'],
            'icons8-envelope': ['mail'],
            'icons8-google-plus': ['googleplus'],
            'icons8-reddit': ['reddit'],
            'icons8-twitter': ['twitter'],
            'icons8-vintage-camera': ['vintagecamera'],
            'icons8-slr-camera': ['bigcamera'],
            'icons8-ruler': ['ruler'],
            'icons8-receive-cash': ['ownership'],
            'icons8-overview': ['summary'],
            'icons8-diversity': ['compatibility'],
            'icons8-up': ['up'],
            'icons8-down': ['down'],
            'icons8-expired': ['expired'],
            'icons8-place-marker': ['location'],
            'icons8-rest-api': ['api'],
            'icons8-25-': ['percent'],
            'icons8-heart-monitor': ['status'],
        }

        # Define input directory, relative to ./manage.py
        input_dir = 'icons/svg'

        # Define output directory, relative to ./manage.py
        output_dir = 'schema2/static/svg'

        # Get list of SVGs
        files = glob.glob(input_dir + "/*.svg")

        # Delete and recreate the output dir
        shutil.rmtree(output_dir)
        os.mkdir(output_dir)

        for file in files:

            # Parse filename
            barename = Path(file).stem
            barename = barename.replace('-500', '')


            if barename in newnames.keys():
                # We found the file in the mapping
                for mapping in newnames.get(barename):
                    shutil.copyfile(file, f"{output_dir}/{mapping}.svg")
                    self.stdout.write(self.style.SUCCESS(f"generated {output_dir}/{mapping}.svg"))
            else:
                self.stdout.write(self.style.WARNING(f"{file} is not needed"))
