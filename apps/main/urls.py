from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.main),
    url(r"^getTicker$", views.getTicker),
    url(r"^getGraph/(?P<ticker>\w+)/(?P<graph_range>\w+)$", views.getGraph),
]
