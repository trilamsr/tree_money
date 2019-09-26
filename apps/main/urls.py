from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.main),

    # Tri
    url(r"^get_stats$", views.get_stats),
    

    # Logan
    url(r"^getTicker$", views.getGraph),
    # url(r"^getGraph/(?P<ticker>\w+)/(?P<graph_range>\w+)$", views.getGraph),
]
