from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mot_fms.models import Postcode, VehicleMake

class PostcodeListView(ListView):
    model = Postcode

class PostcodeDetailView(DetailView):
    model = Postcode

class VehicleMakeListView(ListView):
    queryset = VehicleMake.objects.order_by('make')
    context_object_name = 'make_list'