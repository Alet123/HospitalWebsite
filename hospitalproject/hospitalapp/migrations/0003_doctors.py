# Generated by Django 4.1.2 on 2023-06-22 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_departments_dep_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_img', models.ImageField(upload_to='images')),
                ('doc_name', models.CharField(max_length=255)),
                ('dep_spec', models.CharField(max_length=255)),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.departments')),
            ],
        ),
    ]
