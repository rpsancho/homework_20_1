from django.core.management import BaseCommand
from django.core import serializers

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('catalog_data.json', mode='r', encoding='UTF-8') as f:
            for deserialized_object in serializers.deserialize(format="json", stream_or_string=f):
                deserialized_object.save()
