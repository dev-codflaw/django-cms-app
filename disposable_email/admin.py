from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import DisposableEmailDomain

@admin.register(DisposableEmailDomain)
class DisposableEmailAdmin(ImportExportModelAdmin):
    list_display = ('domain', 'status', 'created_at', 'updated_at')
    pass