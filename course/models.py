from djongo import models


class BaseModel(models.Model):
    id = models.ObjectIdField(primary_key=True)

    class Meta:
        abstract = True


class Attendee(models.Model):
    id = models.ObjectIdField(primary_key=True)
    # Other fields for the Attendee model if needed

    class Meta:
        db_table = 'attendee'  # Specify your preferred collection name


class Certificate(models.Model):
    id = models.ObjectIdField(primary_key=True)
    # Other fields for the Certificate model if needed

    class Meta:
        db_table = 'certificate'


class BookingInvoice(models.Model):
    id = models.ObjectIdField(primary_key=True)
    attendees = models.ArrayField(model_container=Attendee)
    # Other fields for the BookingInvoice model if needed

    class Meta:
        db_table = 'booking_invoice'


class Course(BaseModel):
    id = models.ObjectIdField(primary_key=True)
    booking_invoices = models.ArrayField(model_container=BookingInvoice)
    attendees = models.ArrayField(model_container=Attendee)
    # Other fields for the Course model if needed

    class Meta:
        db_table = 'course'


class Hotel(BaseModel):
    id = models.ObjectIdField(primary_key=True)
    # Other fields for the Hotel model if needed

    class Meta:
        db_table = 'hotel'


class Venue(BaseModel):
    id = models.ObjectIdField(primary_key=True)
    courses = models.ArrayField(model_container=Course)
    hotels = models.ArrayField(model_container=Hotel)
    # Other fields for the Venue model if needed

    class Meta:
        db_table = 'venue'


class Enquiry(models.Model):
    id = models.ObjectIdField(primary_key=True)
    # Other fields for the Enquiry model if needed

    class Meta:
        db_table = 'enquiry'


class Address(BaseModel):
    id = models.ObjectIdField(primary_key=True)
    venue = models.EmbeddedField(model_container=Venue)
    hotel = models.ArrayField(model_container=Hotel)
    booking_invoices = models.ArrayField(model_container=BookingInvoice)
    # Other fields for the Address model if needed

    class Meta:
        db_table = 'address'
        abstract = False


class Party(BaseModel):
    id = models.ObjectIdField(primary_key=True)
    booking_invoices = models.ArrayField(model_container=BookingInvoice)
    enquiries = models.ArrayField(model_container=Enquiry)
    # Other fields for the Party model if needed

    class Meta:
        db_table = 'party'
        abstract = False


class CourseType(models.Model):
    id = models.ObjectIdField(primary_key=True)
    booking_invoices = models.ArrayField(model_container=BookingInvoice)
    courses = models.ArrayField(model_container=Course)
    # Other fields for the CourseType model if needed

    class Meta:
        db_table = 'course_type'
        abstract = False
