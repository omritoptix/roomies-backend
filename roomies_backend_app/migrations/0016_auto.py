# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field roomie on 'BillItem'
        db.delete_table(db.shorten_name(u'roomies_backend_app_billitem_roomie'))

        # Adding M2M table for field roomies on 'BillItem'
        m2m_table_name = db.shorten_name(u'roomies_backend_app_billitem_roomies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('billitem', models.ForeignKey(orm[u'roomies_backend_app.billitem'], null=False)),
            ('roomie', models.ForeignKey(orm[u'roomies_backend_app.roomie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['billitem_id', 'roomie_id'])


    def backwards(self, orm):
        # Adding M2M table for field roomie on 'BillItem'
        m2m_table_name = db.shorten_name(u'roomies_backend_app_billitem_roomie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('billitem', models.ForeignKey(orm[u'roomies_backend_app.billitem'], null=False)),
            ('roomie', models.ForeignKey(orm[u'roomies_backend_app.roomie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['billitem_id', 'roomie_id'])

        # Removing M2M table for field roomies on 'BillItem'
        db.delete_table(db.shorten_name(u'roomies_backend_app_billitem_roomies'))


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
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'roomies_backend_app.billitem': {
            'Meta': {'object_name': 'BillItem'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.Bill']"}),
            'billType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roomies_backend_app.BillType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'roomies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Roomie']", 'symmetrical': 'False'})
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
        }
    }

    complete_apps = ['roomies_backend_app']