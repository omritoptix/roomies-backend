from django.contrib.auth.models import User
from tastypie.resources import fields
from tastypie.resources import ModelResource

from roomies_backend_app.models import *
from tastypie.constants import ALL
from tastypie.authorization import Authorization


# class UserResource(ModelResource):
#     class Meta:
#         queryset = User.objects.all()
#         allowed_methods = ['get','post']
#         always_return_data = True
#         #if want more field , add here:


class ApartmentResource(ModelResource):
    #if i want to filter fields i will use the roomieApartmentResource with lambda expression
#     roomie_id = fields.ToManyField(RoomieApartmentResource,'roomie',full = True)
    class Meta:
        queryset = Apartment.objects.all()
        resource_name = 'apartment'
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        filtering = {
            "address": ALL
        }
        authorization= Authorization()
        #fields = ['']
        
                
class RoomieResource(ModelResource):
    apartment = fields.ForeignKey(ApartmentResource,'apartment',full = True,null = True)
    class Meta:
        queryset = Roomie.objects.all()
        resource_name = 'roomie'
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        filtering = {
#             "slug": ('exact', 'startswith',),
            "username": ALL
        }
        authorization= Authorization()
        
# class RoomieApartmentResource(ModelResource):
# #     roomie = fields.ToOneField(RoomieResource,'roomie',full = True)
# #     apartment = fields.ToOneField('Main.resources.ApartmentResource','apartment', full = True)
#     class Meta:
#         queryset = RoomieApartment.objects.all()
#         resource_name = 'roomieApartment'
#         allowed_methods = ['get','post']
#         always_return_data = True

        
# class BillResource(ModelResource):
#     apartment_id = fields.ForeignKey(ApartmentResource,'apartment')
#     class Meta:
#         queryset = Bill.objects.all()
#         allowed_methods = ['get','post']
#         always_return_data = True
        
# class BillTypeResource(ModelResource):
#     
#     class Meta:
#         queryset = BillType.objects.all()
#         allowed_methods = ['get','post']
#         always_return_data = True
        
        
# class BillItemResource(ModelResource):
#     roomie_id = fields.ToManyField(RoomieResource,'roomie',full = True)
#     bill_id = fields.ForeignKey(BillResource,'billID',full = True)
#     billType_id = fields.ForeignKey(BillTypeResource,'billType',full = True)
#     class Meta:
#         queryset = BillItem.objects.all()
#         allowed_methods = ['get','post']
#         always_return_data = True
        
# class RoomieBillItemResource(ModelResource):
#     class Meta:
#         queryset = RoomieBillItem.objects.all()
#         resource_name = 'roomieBillItem'
#         allowed_methods = ['get','post']
#         always_return_data = True
    
    