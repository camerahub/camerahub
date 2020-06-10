from django.views.generic.list import ListView

from schema.models import Condition

class ConditionListView(ListView):

    model = Condition
    template_name = "condition.html"
