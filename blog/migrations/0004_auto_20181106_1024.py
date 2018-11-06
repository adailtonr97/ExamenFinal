# Generated by Django 2.1 on 2018-11-06 16:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='doctores',
            field=models.ManyToManyField(through='blog.Cita', to='blog.Doctor'),
        ),
    ]
