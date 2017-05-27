import random

from django.core.management.base import BaseCommand
from django.db import transaction
from django_seed import Seed

from core.models import (RequestForResource, Pledge, Action, Location, UserProfile, Resource)

class Command(BaseCommand):
    help = 'Seeds the database.'

    def handle(self, *args, **kwargs):
        N_RESOURCES = 10

        with transaction.atomic():
            seeder = Seed.seeder()
            seeder.add_entity(Location, 5, {'name': lambda x: seeder.faker.city()})
            seeder.add_entity(Action, 15)
            seeder.add_entity(Resource, N_RESOURCES)
            created_element_ids = seeder.execute()

            for action_id in created_element_ids[Action]:
                for i in range(0, random.randrange(1, 3)):
                    resource_id = created_element_ids[Resource][random.randrange(N_RESOURCES)]
                    needed = random.randrange(10, 50)
                    request_for_resource = RequestForResource.objects.create(
                        action_id=action_id,
                        resource_id=resource_id,
                        needed=needed,
                        acquired=random.randrange(needed)
                    )
