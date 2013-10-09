# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RoomieBillItem.needToPay'
        db.add_column(u'roomies_backend_app_roomiebillitem', 'needToPay',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RoomieBillItem.needToPay'
        db.delete_column(u'roomies_backend_app_roomiebillitem', 'needToPay')


    models = {
        u'roomies_backend_app.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roomiesNum': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'roomies_backend_app.bill': {
            'Meta': {'object_name': 'Bill'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']"}),
            'dateCreated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'roomies_backend_app.billitem': {
            'Meta': {'object_name': 'BillItem'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Bill']"}),
            'billType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.BillType']"}),
            'createdBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'createdBy'", 'to': u"orm['roomies_backend_app.Roomie']"}),
            'dateCreated': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'roomies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Roomie']", 'through': u"orm['roomies_backend_app.RoomieBillItem']", 'symmetrical': 'False'})
        },
        u'roomies_backend_app.billtype': {
            'Meta': {'object_name': 'BillType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roomies_backend_app.invite': {
            'Meta': {'object_name': 'Invite'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']"}),
            'fromRoomie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roomies_from'", 'to': u"orm['roomies_backend_app.Roomie']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'toRoomie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roomies_to'", 'to': u"orm['roomies_backend_app.Roomie']"})
        },
        u'roomies_backend_app.roomie': {
            'Meta': {'object_name': 'Roomie'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'roomies_backend_app.roomiebillitem': {
            'Meta': {'object_name': 'RoomieBillItem'},
            'amountPaid': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'billItem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.BillItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needToPay': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'roomie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Roomie']"})
        }
    }

    complete_apps = ['roomies_backend_app']