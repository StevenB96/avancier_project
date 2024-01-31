from django.contrib import admin
from django import forms
from django_select2.forms import Select2Widget

from .models import (
    Certificate,
    Hotel,
    Attendee,
    BookingInvoice,
    Course,
    Venue,
    Enquiry,
    Address,
    Party,
    CourseType
)

class CertificateAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'course_type_id': Select2Widget,
        }
        required = {
            'course_type_id': False,
        }

    course_type_id = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=Select2Widget,
    )

class CertificateAdmin(admin.ModelAdmin):
    form = CertificateAdminForm
    exclude = ['_id']

class HotelAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'venue_id': Select2Widget,
            'address_id': Select2Widget,
        }
        required = {
            'venue_id': False,
            'address_id': False,
        }

    venue_id = forms.ModelChoiceField(
        queryset=Venue.objects.all(),
        widget=Select2Widget,
    )
    address_id = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=Select2Widget,
    )

class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    exclude = ['_id']


class AttendeeAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'bookinginvoice_id': Select2Widget,
            'course_id': Select2Widget
        }
        required = {
            'bookinginvoice_id': False,
            'course_id': False,
        }

    bookinginvoice_id = forms.ModelChoiceField(
        queryset=BookingInvoice.objects.all(),
        widget=Select2Widget,
    )
    course_id = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=Select2Widget,
    )


class AttendeeAdmin(admin.ModelAdmin):
    form = AttendeeAdminForm
    exclude = ['_id']

class BookingInvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'party_id': Select2Widget,
            'address_id': Select2Widget,
            'course_id': Select2Widget
        }
        required = {
            'party_id': False,
            'address_id': False,
            'course_id': False,
        }

    party_id = forms.ModelChoiceField(
        queryset=Party.objects.all(),
        widget=Select2Widget,
    )
    address_id = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=Select2Widget,
    )
    course_id = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=Select2Widget,
    )

class BookingInvoiceAdmin(admin.ModelAdmin):
    form = BookingInvoiceAdminForm
    exclude = ['_id', 'attendees']

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'venue_id': Select2Widget,
            'course_type_id': Select2Widget
        }
        required = {
            'venue_id': False,
            'course_type_id': False,
        }

    venue_id = forms.ModelChoiceField(
        queryset=Venue.objects.all(),
        widget=Select2Widget,
    )
    course_type_id = forms.ModelChoiceField(
        queryset=CourseType.objects.all(),
        widget=Select2Widget,
    )

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    exclude = ['_id', 'bookinginvoices', 'attendees']

class VenueAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'address_id': Select2Widget,
        }
        required = {
            'address_id': False,
        }

    address_id = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=Select2Widget,
    )

class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm
    exclude = ['_id', 'courses', 'hotels']

class EnquiryAdminForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = '__all__'
        widgets = {
            'course_type_id': Select2Widget,
            'party_id': Select2Widget
        }
        required = {
            'course_type_id': False,
            'party_id': False,
        }

    course_type_id = forms.ModelChoiceField(
        queryset=CourseType.objects.all(),
        widget=Select2Widget,
    )
    party_id = forms.ModelChoiceField(
        queryset=Party.objects.all(),
        widget=Select2Widget,
    )

class EnquiryAdmin(admin.ModelAdmin):
    form = EnquiryAdminForm
    exclude = ['_id']


class AddressAdmin(admin.ModelAdmin):
    exclude = ['_id', 'venue', 'hotel', 'bookinginvoices']


class PartyAdmin(admin.ModelAdmin):
    exclude = ['_id', 'bookinginvoices', 'enquiries']


class CourseTypeAdmin(admin.ModelAdmin):
    exclude = ['_id', 'enquiries', 'courses', 'certificates']


# Register each admin class for the corresponding model
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(BookingInvoice, BookingInvoiceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
