from django.contrib import admin
from .models import UserAccount

class AccountsAdmin(admin.ModelAdmin):
	list_display = ('email', 'name', 'phone_number', 'is_active')

	def active(self, obj):
		return obj.is_active == 1

	active.boolean = True

admin.site.register(UserAccount, AccountsAdmin)

