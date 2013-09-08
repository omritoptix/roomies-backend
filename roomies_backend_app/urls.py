from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from tastypie.api import Api
from roomies_backend_app.resources import *
import roomies_backend_app
import roomies_backend_app.views

v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
v1_api.register(RoomieResource())
v1_api.register(ApartmentResource())
v1_api.register(InviteResource())
# v1_api.register(BillResource())
# v1_api.register(BillTypeResource())
# v1_api.register(BillItemResource())
# v1_api.register(RoomieApartmentResource())
# v1_api.register(RoomieBillItemResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#     url(r'^$', 'roomies_backend_app.views.main_page'),
    (r'^api/', include(v1_api.urls)),
    ('^$', roomies_backend_app.views.porthole),
    ('^proxy/', roomies_backend_app.views.proxy),
    # Examples:
    # url(r'^$', 'Roomies.views.home', name='home'),
    # url(r'^Roomies/', include('Roomies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
