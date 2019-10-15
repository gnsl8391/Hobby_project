# Generated by Django 2.2.6 on 2019-10-14 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191014_1537'),
        ('boards', '0002_auto_20191014_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postfree',
            name='name',
        ),
        migrations.RemoveField(
            model_name='posthobby',
            name='name',
        ),
        migrations.AddField(
            model_name='postfree',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posthobby',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
            preserve_default=False,
        ),
    ]