# Generated by Django 4.2.4 on 2023-08-18 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='seller',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='imageUrl',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listingcomment', to='auctions.listing')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personcomment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='imageURL',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]