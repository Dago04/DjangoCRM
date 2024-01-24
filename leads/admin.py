from django.contrib import admin

from .models import User, Lead, Agent
# Register your models here.


admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)

admin.site.site_header = "Django CRM"
