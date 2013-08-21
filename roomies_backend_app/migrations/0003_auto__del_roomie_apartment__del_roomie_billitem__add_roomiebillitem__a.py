# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Roomie_Apartment'
        db.delete_table(u'roomies_backend_app_roomie_apartment')

        # Deleting model 'Roomie_BillItem'
        db.delete_table(u'roomies_backend_app_roomie_billitem')

        # Adding model 'RoomieBillItem'
        db.create_table(u'roomies_backend_app_roomiebillitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('billItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.BillItem'])),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['RoomieBillItem'])

        # Adding model 'RoomieApartment'
        db.create_table(u'roomies_backend_app_roomieapartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Apartment'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['RoomieApartment'])


    def backwards(self, orm):
        # Adding model 'Roomie_Apartment'
        db.create_table(u'roomies_backend_app_roomie_apartment', (
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Apartment'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['Roomie_Apartment'])

        # Adding model 'Roomie_BillItem'
        db.create_table(u'roomies_backend_app_roomie_billitem', (
            ('billItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.BillItem'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['Roomie_BillItem'])

        # Deleting model 'RoomieBillItem'
        db.delete_table(u'roomies_backend_app_roomiebillitem')

        # Deleting model 'RoomieApartment'
        db.delete_table(u'roomies_backend_app_roomieapartment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'roomie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Roomie']", 'through': u"orm['roomies_backend_app.RoomieBillItem']", 'symmetrical': 'False'})
        },
        u'roomies_backend_app.billtype': {
            'Meta': {'object_name': 'BillType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roomies_backend_app.roomie': {
            'Meta': {'object_name': 'Roomie'},
            'apartment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Apartment']", 'through': u"orm['roomies_backend_app.RoomieApartment']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'roomies_backend_app.roomieapartment': {
            'Meta': {'object_name': 'RoomieApartment'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Apartment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roomie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Roomie']"})
        },
        u'roomies_backend_app.roomiebillitem': {
            'Meta': {'object_name': 'RoomieBillItem'},
            'billItem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.BillItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roomie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Roomie']"})
        }
    }

    complete_apps = ['roomies_backend_app']