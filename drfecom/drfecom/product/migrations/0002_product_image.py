# Generated by Django 4.2 on 2023-04-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to="products/<django.db.models.fields.related.ForeignKey>_<django.db.models.fields.CharField>",
            ),
        ),
    ]
