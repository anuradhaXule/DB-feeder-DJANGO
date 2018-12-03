# Generated by Django 2.1.3 on 2018-12-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetone', models.CharField(blank=True, db_column='streetOne', max_length=255, null=True)),
                ('streettwo', models.CharField(blank=True, db_column='streetTwo', max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('postalcode', models.IntegerField(blank=True, db_column='postalCode', null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoname', models.CharField(blank=True, db_column='photoName', max_length=255, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'photos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratetype', models.CharField(blank=True, db_column='rateType', max_length=255, null=True)),
                ('stylisttype', models.CharField(blank=True, db_column='stylistType', max_length=255, null=True)),
                ('ratevalue', models.FloatField(blank=True, db_column='rateValue', null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salonname', models.CharField(blank=True, db_column='salonName', max_length=255, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'salons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('sessiontype', models.CharField(blank=True, db_column='sessionType', max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'sessions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skilltype', models.CharField(blank=True, db_column='skillType', max_length=255, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'skills',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stylists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'stylists',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
