from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.main),
    url(r"^get_nav/?$", views.get_nav),
    url(r"^get_financial/?$", views.get_data('financial')),
    url(r"^get_technical/?$", views.get_data('technical')),
    url(r"^get_profile/?$", views.get_data('profile')),
    url(r"^get_news/?$", views.get_news),
    url(r"^getTicker/?$", views.getGraph),
    url(r"^getTicker1/?$", views.getGraph),
]
