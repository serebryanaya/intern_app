# Generated by Django 3.1.7 on 2021-04-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_student_my_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='initials',
            field=models.CharField(max_length=200, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Логин'),
        ),
    ]
