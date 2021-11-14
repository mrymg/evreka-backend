# Generated by Django 3.2.9 on 2021-11-14 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10, verbose_name='plate')),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=0, verbose_name='Latitude')),
                ('lng', models.FloatField(default=0, verbose_name='Longtitude')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Datetime')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='q1.vehicle', verbose_name='Plate')),
            ],
        ),
    ]