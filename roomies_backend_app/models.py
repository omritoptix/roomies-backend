from django.db import models
import customModelField
# from django.contrib.auth.models import User

# Create your models here.


class Apartment(models.Model):
    address = models.CharField(max_length = 128)
#     roomie = models.ManyToManyField(Roomie, through = 'Roomie_Apartment')
#     roomie = models.ManyToManyField(Roomie)

    def __unicode__(self):
        return self.address
    
class Roomie(models.Model):
#     user = models.OneToOneField(User)
    username = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    apartment = models.ForeignKey(Apartment,null = True)
    
    def __str__(self):
        return str(self.username)
    
# the related name attribute, tells django which name to use for the reverse realation.
#since we have 2 FK , if we wouldn't define it, we would end up with a clash since django
#will try to define 2 reverse relation on 'Roomie' with the same name    
class Invite(models.Model):
    fromRoomie = models.ForeignKey(Roomie,related_name='roomies_from')
    toRoomie = models.ForeignKey(Roomie,related_name='roomies_to')
    apartment = models.ForeignKey(Apartment)
    new = models.BooleanField()
    # 0 - declined, 1- accepted, 2 - not sent answer - wrote custom range field, but needed to add south logic so gave up for now.
    status = models.PositiveIntegerField()
    
# class RoomieApartment(models.Model):
#     roomie = models.ForeignKey(Roomie)
#     apartment = models.ForeignKey(Apartment)
#     
#     def __unicode__(self):
#         return "apartment:%s, roomie:%s" %(self.apartment.address,self.roomie.user.username)
    
class Bill(models.Model):
    apartment = models.ForeignKey(Apartment)
    date = models.DateField(auto_now_add = True)
    isActive = models.BooleanField()
    
    def __unicode__(self):
#         return self.date.__str__()
        return "on date %s apartment %s" %(self.date.__str__(), self.apartment)
    
class BillType(models.Model):
    description = models.CharField(max_length = 128)
    
    def __unicode__(self):
        return self.description
    
class BillItem(models.Model):
    billID = models.ForeignKey(Bill)
    # how to add other and make a text box open.
    # where to save it? (create a field named other)
    billType = models.ForeignKey(BillType,verbose_name = 'Bill Type')
    other = models.CharField(null=True,blank=True,max_length = 128)
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)
#     roomie = models.ManyToManyField(Roomie, through = 'RoomieBillItem')
    roomie = models.ManyToManyField(Roomie)

    
    def __unicode__(self):
        return "%s need to pay %.2f on %s" %(self.billID,self.amount,self.billType)
    
# class RoomieBillItem(models.Model):
#     billItem = models.ForeignKey(BillItem)
#     roomie = models.ForeignKey(Roomie)
#     
#     def __unicode__(self):
#         return "billItem id:%d,roomie:%s" %(self.billItem.id, self.roomie.user.username) 