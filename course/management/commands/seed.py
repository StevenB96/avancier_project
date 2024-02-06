from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group
from ...model_classes import (
    Certificate,
    Hotel,
    Attendee,
    Bookinginvoice,
    Course,
    CourseCertificate,
    CourseType,
    Venue,
    Enquiry,
    Address,
    Party,
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Groups
        groupList = [
            {
                'name': 'business_group',
            },
        ]

        # Content types
        content_type_list = [
            Certificate,
            Hotel,
            Attendee,
            Bookinginvoice,
            Course,
            CourseCertificate,
            CourseType,
            Venue,
            Enquiry,
            Address,
            Party,
        ]

        # Users
        userList = [
            {
                'username': 'admin_user',
                'email': 'admin_user@example.com',
                'password': 'adminpass',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
            },
            {
                'username': 'business_user',
                'email': 'business_user@example.com',
                'password': 'businesspass',
                'is_superuser': False,
                'is_staff': True,
                'is_active': True,
            }
        ]

        for group in groupList:
            # Create the groups
            group_record, created = Group.objects.get_or_create(
                name=group["name"],
            )

        business_group_record = Group.objects.get(name='business_group')

        crud_operation_list = [
            'add',
            'change',
            'delete',
            'view',
        ]

        for content_type in content_type_list:
            # Create the content type
            content_type_record, created = ContentType.objects.get_or_create(
                app_label=content_type._meta.app_label,
                model=content_type._meta.model_name
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Content type for {content_type._meta.verbose_name_plural} created"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Content type for {content_type._meta.verbose_name_plural} already exists"))

            # Create the permissions
            for crud_operation in crud_operation_list:
                permission_record, created = Permission.objects.get_or_create(
                    content_type_id=content_type_record.id,
                    codename=f"{crud_operation}_{content_type_record.model}",
                    name=f"Can {crud_operation} {content_type_record.model}",
                )

                if (content_type_record.app_label == "course"):
                    # Assign to group
                    business_group_record.permissions.add(permission_record)

        for user in userList:
            if not User.objects.filter(username=user["username"]).exists():
                user_record = User.objects.create_user(
                    username=user["username"],
                    email=user["email"],
                    password=user["password"],
                    is_superuser=user["is_superuser"],
                    is_staff=user["is_staff"],
                    is_active=user["is_active"]
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"User {user_record.id} created successfully"
                    )
                )
                if (user["username"] == "business_user"):
                    # Assign group
                    user_record.groups.add(business_group_record)
            else:
                self.stdout.write(
                    self.style.WARNING(
                        'User already exists'
                    )
                )
