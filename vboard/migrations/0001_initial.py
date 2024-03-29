# Generated by Django 3.1.7 on 2021-04-14 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20210414_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Навык')),
                ('owner', models.CharField(choices=[('U', 'university'), ('E', 'employer')], default='U', max_length=1, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Вакансия')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.employer', verbose_name='Работодатель')),
                ('skills', models.ManyToManyField(blank=True, null=True, to='vboard.Skill', verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Стажировка',
                'verbose_name_plural': 'Стажировки',
                'ordering': ['-published'],
            },
        ),
    ]
