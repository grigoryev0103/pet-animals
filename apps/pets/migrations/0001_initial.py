# Generated by Django 2.2.5 on 2019-09-18 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full name')),
            ],
            options={
                'verbose_name': 'Owner',
                'verbose_name_plural': 'Owners',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets.Owner', verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Dog',
                'verbose_name_plural': 'Dogs',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pets.Owner', verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Cat',
                'verbose_name_plural': 'Cats',
            },
        ),
    ]
