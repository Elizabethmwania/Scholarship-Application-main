from django.contrib import admin
from .models import SponsoredApplications


class AllSponsoredApplications(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'homeAddress',
                    'email', 'phone', 'sponsorName', 'sponsorPhoneNumber')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

admin.site.register(SponsoredApplications, AllSponsoredApplications)
