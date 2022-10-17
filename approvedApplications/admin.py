from django.contrib import admin
from .models import ApprovedApplications


class AllApprovedApplications(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'homeAddress',
                    'email', 'phone', 'academicLevel', 'application_status')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

admin.site.register(ApprovedApplications, AllApprovedApplications)
