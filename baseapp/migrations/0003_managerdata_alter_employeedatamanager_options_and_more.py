# Generated by Django 4.0.2 on 2022-02-23 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_remove_employeedatamanager_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField()),
                ('manager_name', models.CharField(max_length=200)),
                ('manager_age', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='employeedatamanager',
            options={'ordering': ['-employee_start_date']},
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('project_name', models.CharField(max_length=200)),
                ('project_field', models.CharField(max_length=200)),
                ('project_start_date', models.DateField()),
                ('project_end_date', models.DateField()),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.managerdata')),
            ],
        ),
        migrations.AddField(
            model_name='employeedatamanager',
            name='manager_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseapp.managerdata'),
            preserve_default=False,
        ),
    ]