# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RoomieApartmentInvites'
        db.create_table(u'roomies_backend_app_roomieapartmentinvites', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Apartment'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['RoomieApartmentInvites'])


    def backwards(self, orm):
        # Deleting model 'RoomieApartmentInvites'
        db.delete_table(u'roomies_backend_app_roomieapartmentinvites')


    models = {
        u'roomies_backend_app.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roomies_backend_app.bill': {
            'Meta': {'object_name': 'Bill'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'roomies_backend_app.billitem': {
            'Meta': {'object_name': 'BillItem'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'billID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Bill']"}),
            'billType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.BillType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'roomie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Roomie']", 'symmetrical': 'False'})
        },
        u'roomies_backend_app.billtype': {
            'Meta': {'object_name': 'BillType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roomies_backend_app.roomie': {
            'Meta': {'object_name': 'Roomie'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'roomies_backend_app.roomieapartmentinvites': {
            'Meta': {'object_name': 'RoomieApartmentInvites'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roomie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Roomie']"})
        }
    }

    complete_apps = ['roomies_backend_app']