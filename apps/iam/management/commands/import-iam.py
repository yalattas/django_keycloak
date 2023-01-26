from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
import json


class Command(BaseCommand):
    help = "Create missing groups and update users' groups if needed."

    def add_group(self, data):
        created_counter = 0
        counter = 0
        for instance in data:
            new_city, created = Group.objects.get_or_create(name=instance['name'])
            if created:
                created_counter += 1
                new_city.save()
            else:
                counter += 1
        return created_counter, counter

    def add_arguments(self, parser):
        parser.add_argument('iam_feed', nargs='+')

    def handle(self, *args, **options):
        try:
            settings_dir = options['iam_feed'][0]
        except:
            raise CommandError(
                'Please pass the directory name of a json file.')
        f = open(settings_dir)
        data = json.load(f)

        group_created_counter, group_updated_counter = self.add_group(data.get('groups'))
        group_output = f'\n{group_created_counter} groups were created.\n{group_updated_counter} groups were updated.'

        result = group_output
        self.stdout.write(self.style.SUCCESS(result))