# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField(default=59)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1)),
                ('cpf', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=22)),
                ('issuing', models.CharField(max_length=6)),
                ('date_issue', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('civil_state', models.CharField(choices=[(b'1', b'unmarried'), (b'2', b'married'), (b'3', b'divorced'), (b'4', b'widower')], default=(b'1', b'unmarried'), max_length=1)),
                ('education', models.CharField(choices=[(b'1', b'incomplete_primary_school'), (b'2', b'complete_primary_school'), (b'3', b'incomplete_high_school'), (b'4', b'complete_high_school'), (b'5', b'incomplete_third_school'), (b'6', b'complete_third_school')], max_length=1)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('nationality', models.IntegerField(default=76)),
                ('ddi', models.IntegerField()),
                ('ddd', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('mobile_operator', models.CharField(choices=[(b'1', b'claro'), (b'2', b'vivo'), (b'3', b'tim'), (b'4', b'nextel'), (b'5', b'br_telecon'), (b'6', b'oi'), (b'99', b'other')], max_length=1)),
                ('os_type', models.CharField(choices=[(b'1', b'Android'), (b'2', b'BlackBerry'), (b'3', b'IPhone'), (b'4', b'Windows Phone'), (b'5', b'Symbian'), (b'6', b'other')], max_length=1)),
                ('residence_zip_code', models.IntegerField()),
                ('residence_state', models.CharField(max_length=2)),
                ('residence_city', models.CharField(max_length=100)),
                ('residence_neighborhood', models.CharField(max_length=100)),
                ('residence_address', models.CharField(max_length=100)),
                ('residence_number', models.CharField(max_length=5)),
                ('residence_complement', models.CharField(max_length=100)),
                ('residence_ddi', models.IntegerField()),
                ('residence_ddd', models.IntegerField()),
                ('residence_phone_number', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('trading_name', models.CharField(max_length=100)),
                ('commercial_document', models.CharField(max_length=20)),
                ('commercial_open_date', models.CharField(max_length=10)),
                ('commercial_ddd', models.IntegerField()),
                ('commercial_phone_number', models.IntegerField()),
                ('commercial_branch_line', models.IntegerField(default=0)),
                ('commercial_zip_code', models.IntegerField()),
                ('commercial_state', models.CharField(max_length=2)),
                ('commercial_city', models.CharField(max_length=100)),
                ('commercial_neighborhood', models.CharField(max_length=100)),
                ('commercial_address', models.CharField(max_length=100)),
                ('commercial_number', models.CharField(max_length=5)),
                ('bank_code', models.CharField(max_length=4)),
                ('bank_agency', models.CharField(max_length=9)),
                ('bank_account', models.CharField(max_length=9)),
                ('bank_account_type', models.CharField(max_length=1)),
                ('bank_account_name', models.CharField(max_length=100)),
                ('bank_document_holder', models.IntegerField()),
                ('plans_link', models.CharField(default=b'True', max_length=5)),
                ('receiving_credits', models.CharField(default=b'True', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Billet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddi', models.IntegerField(default=55)),
                ('ddd', models.IntegerField(default=21)),
                ('phone_number', models.IntegerField()),
                ('product_code', models.IntegerField()),
                ('due_date', models.CharField(max_length=8)),
                ('value', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=30)),
                ('billet_ddi', models.IntegerField(default=55)),
                ('billet_ddd', models.IntegerField(default=21)),
                ('billet_phone_number', models.IntegerField()),
                ('drawn_blank', models.CharField(max_length=5)),
                ('tipagos_code', models.CharField(max_length=100)),
                ('base64', models.TextField()),
                ('digits', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rc', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('authorization_code', models.CharField(blank=True, max_length=255)),
                ('cancel_code_authorization', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PayerOfBillet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cpf_cnpj', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=70)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(max_length=2)),
                ('ddi', models.IntegerField()),
                ('ddd', models.IntegerField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_store', models.CharField(max_length=255)),
                ('key_store', models.CharField(blank=True, max_length=255)),
                ('product_code', models.CharField(max_length=255)),
                ('type_client_capture', models.CharField(choices=[(b'3', b'credit_card_not_cryptography')], max_length=1)),
                ('data_client', models.CharField(max_length=255)),
                ('security_code', models.CharField(blank=True, max_length=255)),
                ('value', models.IntegerField()),
                ('form_of_payment', models.CharField(choices=[(b'1', b'in_cash'), (b'2', b'installments_without_interest'), (b'3', b'installments_with_interest')], max_length=255)),
                ('installments', models.IntegerField()),
                ('captured_transaction', models.CharField(max_length=255)),
                ('order_description', models.CharField(blank=True, max_length=255)),
                ('authorization_code', models.CharField(max_length=255)),
                ('nsu_tipagos', models.CharField(max_length=255)),
                ('nsu_transaction', models.CharField(default=uuid.uuid4, editable=False, max_length=255, unique=True)),
                ('flag_code', models.CharField(blank=True, max_length=255)),
                ('split_value', models.CharField(blank=True, max_length=255)),
                ('error', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Error')),
            ],
        ),
        migrations.AddField(
            model_name='billet',
            name='error',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Error'),
        ),
        migrations.AddField(
            model_name='billet',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.PayerOfBillet'),
        ),
        migrations.AddField(
            model_name='account',
            name='error',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Error'),
        ),
    ]
