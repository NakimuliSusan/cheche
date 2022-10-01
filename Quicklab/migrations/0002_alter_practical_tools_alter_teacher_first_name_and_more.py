# Generated by Django 4.0.6 on 2022-10-01 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quicklab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical',
            name='tools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_student', to='Quicklab.tool'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tool',
            name='label',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
