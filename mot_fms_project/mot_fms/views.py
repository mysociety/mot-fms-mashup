from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mot_fms.models import Postcode

class PostcodeListView(ListView):
    model = Postcode

class PostcodeDetailView(DetailView):
    model = Postcode
