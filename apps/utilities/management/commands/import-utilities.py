from django.core.management.base import BaseCommand, CommandError
from apps.utilities import models
import json


class Command(BaseCommand):
    help = "Create missing cities, districts and update if needed."

    # def add_districts(self, data, city):
    #     district_created_counter = 0
    #     district_updated_counter = 0
    #     for instance in data:
    #         new_district, created = models.District.objects.get_or_create(name_ar=instance['name_ar'], name_en=instance['name_en'], city=city)
    #         if created:
    #             district_created_counter += 1
    #             new_district.save()
    #         else:
    #             district_updated_counter += 1
    #     return district_created_counter, district_updated_counter

    # def add_cities(self, data):
    #     city_created_counter = 0
    #     city_updated_counter = 0
    #     for instance in data:
    #         new_city, created = models.City.objects.get_or_create(name_ar=instance['name_ar'], name_en=instance['name_en'])
    #         if created:
    #             city_created_counter += 1
    #             new_city.save()
    #         else:
    #             city_updated_counter += 1
    #         self.add_districts(instance['districts'], new_city)
    #     return city_created_counter, city_updated_counter

    def add_arguments(self, parser):
        parser.add_argument('city_feed', nargs='+')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("skipped"))
        # try:
        #     settings_dir = options['city_feed'][0]
        # except:
        #     raise CommandError(
        #         'Please pass the directory name of a json file.')
        # f = open(settings_dir)
        # data = json.load(f)

        # city_created_counter, city_updated_counter = self.add_cities(data.get('cities'))
        # city_output = f'\n{city_created_counter} cities were created.\n{city_updated_counter} cities were updated.'

        # result = city_output
        # self.stdout.write(self.style.SUCCESS(result))