# Generated by Django 2.2.2 on 2019-06-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0007_codeschool_has_housing")]

    operations = [
        migrations.AddField(
            model_name="codeschool",
            name="is_vet_tec_approved",
            field=models.BooleanField(default=False),
        )
    ]
