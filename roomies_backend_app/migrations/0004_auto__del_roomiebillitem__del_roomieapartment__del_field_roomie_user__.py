# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RoomieBillItem'
        db.delete_table(u'roomies_backend_app_roomiebillitem')

        # Deleting model 'RoomieApartment'
        db.delete_table(u'roomies_backend_app_roomieapartment')

        # Adding M2M table for field roomie on 'Apartment'
        m2m_table_name = db.shorten_name(u'roomies_backend_app_apartment_roomie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apartment', models.ForeignKey(orm[u'roomies_backend_app.apartment'], null=False)),
            ('roomie', models.ForeignKey(orm[u'roomies_backend_app.roomie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['apartment_id', 'roomie_id'])

        # Adding M2M table for field roomie on 'BillItem'
        m2m_table_name = db.shorten_name(u'roomies_backend_app_billitem_roomie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('billitem', models.ForeignKey(orm[u'roomies_backend_app.billitem'], null=False)),
            ('roomie', models.ForeignKey(orm[u'roomies_backend_app.roomie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['billitem_id', 'roomie_id'])

        # Deleting field 'Roomie.user'
        db.delete_column(u'roomies_backend_app_roomie', 'user_id')

        # Adding field 'Roomie.username'
        db.add_column(u'roomies_backend_app_roomie', 'username',
                      self.gf('django.db.models.fields.CharField')(default='omri', max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'RoomieBillItem'
        db.create_table(u'roomies_backend_app_roomiebillitem', (
            ('billItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.BillItem'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['RoomieBillItem'])

        # Adding model 'RoomieApartment'
        db.create_table(u'roomies_backend_app_roomieapartment', (
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Apartment'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('roomie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roomies_backend_app.Roomie'])),
        ))
        db.send_create_signal(u'roomies_backend_app', ['RoomieApartment'])

        # Removing M2M table for field roomie on 'Apartment'
        db.delete_table(db.shorten_name(u'roomies_backend_app_apartment_roomie'))

        # Removing M2M table for field roomie on 'BillItem'
        db.delete_table(db.shorten_name(u'roomies_backend_app_billitem_roomie'))

        # Adding field 'Roomie.user'
        db.add_column(u'roomies_backend_app_roomie', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='toDelete', to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Roomie.username'
        db.delete_column(u'roomies_backend_app_roomie', 'username')


    models = {
        u'roomies_backend_app.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roomie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roomies_backend_app.Roomie']", 'symmetrical': 'False'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['roomies_backend_app']