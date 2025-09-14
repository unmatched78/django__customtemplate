from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Setup initial project data'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Superuser created successfully')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Project setup completed successfully')
        )
