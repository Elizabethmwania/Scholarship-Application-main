from django.contrib import admin
from .models import Applications


class SubmittedApplications(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'homeAddress',
                    'email', 'phone', 'academicLevel', 'approval_status')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(Applications, SubmittedApplications)
