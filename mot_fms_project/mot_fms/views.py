from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mot_fms.models import Postcode, VehicleMake, Vehicle
from django.db.models import Count

class PostcodeListView(ListView):
    model = Postcode

class PostcodeDetailView(DetailView):
    model = Postcode

class VehicleMakeListView(ListView):
    # there's probably a neater way of doing this but I haven't been able to find it
    queryset = VehicleMake.objects.annotate(num_vehicles=Count('vehicle')).filter(num_vehicles__gt=0).order_by('make')
    context_object_name = 'make_list'

class VehicleMakeDetailView(DetailView):
    model = VehicleMake

    def get_context_data(self, **kwargs):
        context = super(VehicleMakeDetailView, self).get_context_data(**kwargs)
        context['count'] = Vehicle.objects.filter(make_id=self.get_object().make_id).count
        context['total_vehicles'] = Vehicle.objects.count
        return context
