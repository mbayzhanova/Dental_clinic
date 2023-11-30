# Generated by Django 4.2.7 on 2023-11-30 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_alter_service_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayofWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dayofweek')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_id', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Часы работы')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctorsemployment',
            name='dates_of_records',
        ),
        migrations.RemoveField(
            model_name='doctorsemployment',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='patientcard',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='patientcard',
            name='patient_id',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='service',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='DoctorsEmployment',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='PatientCard',
        ),
        migrations.DeleteModel(
            name='Registry',
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.service'),
        ),
        migrations.AddField(
            model_name='doctorsschedule',
            name='working_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.workingtime'),
        ),
    ]
