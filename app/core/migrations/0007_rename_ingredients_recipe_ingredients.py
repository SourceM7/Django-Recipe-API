# Generated by Django 4.2.20 on 2025-03-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredients',
            new_name='ingredients',
        ),
    ]
