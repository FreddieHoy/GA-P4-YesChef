# Generated by Django 2.2.5 on 2019-09-09 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20190909_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='meal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='meals.Meal'),
            preserve_default=False,
        ),
    ]
