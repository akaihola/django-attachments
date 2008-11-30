from django.contrib import admin
from django.apps.attachments.models import Attachment

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("file", "title", "summary", "attached_timestamp", "attached_by")

admin.site.register(Attachment, AttachmentAdmin)

