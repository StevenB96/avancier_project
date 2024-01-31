# Generated by Django 4.1.13 on 2024-01-31 00:32

import course.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('venue', djongo.models.fields.EmbeddedField(model_container=course.models.Venue)),
                ('hotel', djongo.models.fields.ArrayField(model_container=course.models.Hotel)),
                ('booking_invoices', djongo.models.fields.ArrayField(model_container=course.models.BookingInvoice)),
            ],
            options={
                'db_table': 'address',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'attendee',
            },
        ),
        migrations.CreateModel(
            name='BookingInvoice',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('attendees', djongo.models.fields.ArrayField(model_container=course.models.Attendee)),
            ],
            options={
                'db_table': 'booking_invoice',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'certificate',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('booking_invoices', djongo.models.fields.ArrayField(model_container=course.models.BookingInvoice)),
                ('attendees', djongo.models.fields.ArrayField(model_container=course.models.Attendee)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('booking_invoices', djongo.models.fields.ArrayField(model_container=course.models.BookingInvoice)),
                ('courses', djongo.models.fields.ArrayField(model_container=course.models.Course)),
            ],
            options={
                'db_table': 'course_type',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'enquiry',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('booking_invoices', djongo.models.fields.ArrayField(model_container=course.models.BookingInvoice)),
                ('enquiries', djongo.models.fields.ArrayField(model_container=course.models.Enquiry)),
            ],
            options={
                'db_table': 'party',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('courses', djongo.models.fields.ArrayField(model_container=course.models.Course)),
                ('hotels', djongo.models.fields.ArrayField(model_container=course.models.Hotel)),
            ],
            options={
                'db_table': 'venue',
            },
        ),
    ]
