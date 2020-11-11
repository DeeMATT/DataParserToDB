# Generated by Django 3.1.3 on 2020-11-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.TextField(null=True)),
                ('store_id', models.IntegerField(null=True)),
                ('previous_price', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('currency', models.CharField(max_length=8, null=True)),
                ('offer_description', models.TextField(null=True)),
                ('manufacturersku', models.TextField(null=True)),
                ('eankod', models.TextField(null=True)),
                ('additional_info', models.TextField(null=True)),
                ('producturl', models.TextField(null=True)),
                ('stock', models.IntegerField(null=True)),
            ],
        ),
    ]
