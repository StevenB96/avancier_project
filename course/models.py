from djongo import models


class BaseModel(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        abstract = True


class Certificate(BaseModel):
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    certificate_code = models.CharField(max_length=255, blank=True, null=True)
    certificate_name = models.CharField(max_length=255, blank=True, null=True)
    certification_body = models.CharField(max_length=255, blank=True, null=True)
    link_to_syllabus = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.certificate_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Certificates'
        db_table = 'certificate'


class Hotel(BaseModel):
    venue_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.CharField(max_length=255, blank=True, null=True)
    hotel_name = models.CharField(max_length=255, blank=True, null=True)
    hotel_website = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.hotel_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Hotels'
        db_table = 'hotel'


class Attendee(BaseModel):
    bookinginvoice_id = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)
    instruction_email_address = models.CharField(max_length=255, blank=True, null=True)
    exam_result_email_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instruction_sent_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Attendees'
        db_table = 'attendee'


class BookingInvoice(BaseModel):
    attendees = models.ArrayField(model_container=Attendee)

    party_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.CharField(max_length=255, blank=True, null=True)
    course_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    po_or_ref_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Bookinginvoices'
        db_table = 'bookinginvoice'


class Course(BaseModel):
    bookinginvoices = models.ArrayField(model_container=BookingInvoice)
    attendees = models.ArrayField(model_container=Attendee)

    venue_id = models.CharField(max_length=255, blank=True, null=True)
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    delegate_total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Courses'
        db_table = 'course'


class Venue(BaseModel):
    courses = models.ArrayField(model_container=Course)
    hotels = models.ArrayField(model_container=Hotel)

    address_id = models.CharField(max_length=255, blank=True, null=True)
    venue_name = models.CharField(max_length=255, blank=True, null=True)
    venue_contact_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.venue_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Venues'
        db_table = 'venue'


class Enquiry(BaseModel):
    course_type_id = models.CharField(max_length=255, blank=True, null=True)
    party_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.description) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Enquiries'
        db_table = 'enquiry'


class Address(BaseModel):
    venue = models.EmbeddedField(model_container=Venue)
    hotel = models.EmbeddedField(model_container=Hotel)
    bookinginvoices = models.ArrayField(model_container=BookingInvoice)

    building_name = models.CharField(max_length=255, blank=True, null=True)
    building_number_and_thoroughfare_name = models.CharField(max_length=255, blank=True, null=True)
    locality_name = models.CharField(max_length=255, blank=True, null=True)
    town_name = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_name = models.CharField(max_length=255, blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return str(self.building_number_and_thoroughfare_name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Addresses'
        db_table = 'address'
        managed = True


class Party(BaseModel):
    bookinginvoices = models.ArrayField(model_container=BookingInvoice)
    enquiries = models.ArrayField(model_container=Enquiry)

    email_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    approved_supplier_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Parties'
        db_table = 'party'
        managed = True


class CourseType(BaseModel):
    enquiries = models.ArrayField(model_container=Enquiry)
    courses = models.ArrayField(model_container=Course)
    certificates = models.ArrayField(model_container=Certificate)

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    delivery_mode = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self._id)

    class Meta:
        verbose_name_plural = 'Course Types'
        db_table = 'course_type'
        managed = True
