from django.contrib.auth.models import User
from tastypie.resources import fields
from tastypie.resources import ModelResource

from roomies_backend_app.models import *
from tastypie.constants import ALL, ALL_WITH_RELATIONS
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
            "address": ALL,
            "roomiesNum" : ALL
        }
        authorization= Authorization()
        #fields = ['']

    def dehydrate(self,bundle):
        roomie_ids = []
        for roomie in Roomie.objects.filter(apartment = bundle.obj.pk):
            roomie_ids.append(roomie.id)
        bundle.data['roomies'] = roomie_ids
#         bundle.data['roomieBillItem_length'] = len(roomie_bill_item_ids)
        return bundle

        
                
class RoomieResource(ModelResource):
    apartment = fields.ForeignKey(ApartmentResource,'apartment',full = True,null = True)
    class Meta:
        queryset = Roomie.objects.all()
        resource_name = 'roomie'
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        filtering = {
#             "slug": ('exact', 'startswith',),
            "username": ALL,
            "apartment" : ALL_WITH_RELATIONS
        }
        authorization= Authorization()
    # saving null to apartment when the json for it is empty  
    def hydrate(self,bundle):
        if 'apartment' not in bundle.data:
            bundle.obj.apartment = None
            return bundle
        return bundle
    
    
class InviteResource(ModelResource):
    fromRoomie = fields.ForeignKey(RoomieResource,'fromRoomie',full=True)
    toRoomie = fields.ForeignKey(RoomieResource,'toRoomie',full=True)
    apartment = fields.ForeignKey(ApartmentResource,'apartment',full=True)
    class Meta:
        queryset = Invite.objects.all()
        resource_name = 'invite'
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        authorization= Authorization()
        filtering = {
            "fromRoomie": ALL_WITH_RELATIONS,
            "toRoomie": ALL_WITH_RELATIONS,
            "apartment": ALL_WITH_RELATIONS,
            "new" : ALL,
            "status" : ALL
        }
             
                
        
# class RoomieApartmentResource(ModelResource):
# #     roomie = fields.ToOneField(RoomieResource,'roomie',full = True)
# #     apartment = fields.ToOneField('Main.resources.ApartmentResource','apartment', full = True)
#     class Meta:
#         queryset = RoomieApartment.objects.all()
#         resource_name = 'roomieApartment'
#         allowed_methods = ['get','post']
#         always_return_data = True

        
class BillResource(ModelResource):
    apartment = fields.ForeignKey(ApartmentResource,'apartment')
    class Meta:
        queryset = Bill.objects.all()
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        authorization= Authorization()
        filtering = {
            "apartment": ALL_WITH_RELATIONS,
            "year": ALL,
            "month": ALL,
            "dateCreated" : ALL,
            "isActive" : ALL
        }
        
class BillTypeResource(ModelResource):
     
    class Meta:
        queryset = BillType.objects.all()
        resource_name = 'bill_type'
        allowed_methods = ['get','post']
        always_return_data = True
        
        
class BillItemResource(ModelResource):
#     roomies = fields.ToManyField(RoomieResource,'roomies',full = True)
    createdBy = fields.ForeignKey(RoomieResource,'createdBy',full = True)
    bill = fields.ForeignKey(BillResource,'bill',full = True)
    billType = fields.ForeignKey(BillTypeResource,'billType',full = True)
    class Meta:
        resource_name = "bill_item"
        queryset = BillItem.objects.all()
        allowed_methods = ['get','post','put','delete']
        always_return_data = True
        authorization= Authorization()
        filtering = {
            "bill": ALL_WITH_RELATIONS,
            "roomies": ALL_WITH_RELATIONS,
            "billType": ALL,
            "other" : ALL,
            "amount" : ALL,
            "dateCreated" : ALL,
            "createdBy" : ALL
        }
        
    def dehydrate(self,bundle):
        roomie_bill_item_ids = []
        for roomieBillItem in RoomieBillItem.objects.filter(billItem = bundle.obj.pk):
            roomie_bill_item_ids.append(roomieBillItem.id)
        bundle.data['roomieBillItem'] = roomie_bill_item_ids
#         bundle.data['roomieBillItem_length'] = len(roomie_bill_item_ids)
        return bundle
        
        
class RoomieBillItemResource(ModelResource):
    roomie = fields.ForeignKey(RoomieResource,'roomie',full = True)
    billItem = fields.ForeignKey(BillItemResource,'billItem',full = True)
    class Meta:
        queryset = RoomieBillItem.objects.all()
        resource_name = 'roomie_bill_item'
        llowed_methods = ['get','post','put','delete']
        always_return_data = True
        authorization= Authorization()
        filtering = {
            "roomie": ALL_WITH_RELATIONS,
            "billItem": ALL_WITH_RELATIONS,
        }
    
    