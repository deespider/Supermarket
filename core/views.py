from django.shortcuts import render
from django.views import View
from django.utils import timezone

class BaseShopView(View):
    """
    Base Class for Shop Views

    Parameters
    ----------
    View : _type_
        _description_

    """
    template_name = None

    def get_context_data(self, extra_data=None):
        data = {"current_date": timezone.now()}
        if extra_data:
            data.update(extra_data)
        return data

    def render(self, request, data=None):
        return render(request, self.template_name, data or self.get_context_data())
