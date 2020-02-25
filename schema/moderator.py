from moderation import moderation
from moderation.moderator import GenericModerator

from schema.models import Manufacturer, Battery, FlashProtocol, NegativeSize, Format, Mount, PaperStock, Process, Toner, FilmStock, Developer, LensModel, CameraModel

# Define custom moderation settings
class CustomModerator(GenericModerator):
    # By default moderation stores objects pending moderation in the changed_object field in the object’s corresponding ModeratedObject instance. If visible_until_rejected is set to True, objects pending moderation will be stored in their original model as usual and the most recently approved version of the object will be stored in changed_object. Default: False
    visible_until_rejected = True

    # When set to True this will allow multiple moderations per registered model instance. Otherwise there is only one moderation per registered model instance. Default: False.
    # This seems to conflict with visible_until_rejected
    keep_history = False

# Enable moderation on models
#moderation.register(Manufacturer, CustomModerator)
#moderation.register(Battery, CustomModerator)
#moderation.register(FlashProtocol, CustomModerator)
#moderation.register(NegativeSize, CustomModerator)
#moderation.register(Format, CustomModerator)
#moderation.register(Mount, CustomModerator)
#moderation.register(PaperStock, CustomModerator)
#moderation.register(Process, CustomModerator)
#moderation.register(Toner, CustomModerator)
#moderation.register(FilmStock, CustomModerator)
#moderation.register(Developer, CustomModerator)
#moderation.register(LensModel, CustomModerator)
#moderation.register(CameraModel, CustomModerator)
