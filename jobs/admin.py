from django.contrib import admin

# Register your models here.

from .models import frontInfo
admin.site.register(frontInfo)

from .models import detail
admin.site.register(detail)
