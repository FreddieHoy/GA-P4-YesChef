# Generated by Django 2.2.5 on 2019-09-09 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20190909_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='comments',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='meals.Comment'),
        ),
    ]
