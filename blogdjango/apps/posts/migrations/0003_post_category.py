# Generated by Django 2.0.10 on 2019-02-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190206_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Web Design', 'Web Design'), ('photoshop', 'photoshop'), ('html5 e css3', 'html5 e css3'), ('web application', 'web application'), ('SEO', 'SEO')], default='Sem Categoria', max_length=1),
        ),
    ]
