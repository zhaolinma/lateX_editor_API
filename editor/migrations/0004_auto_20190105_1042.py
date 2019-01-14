# Generated by Django 2.1.3 on 2019-01-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0003_auto_20190105_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]