from django.contrib import admin
from attachments.models import *

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("file", "title", "summary", "attached_timestamp", "attached_by")

admin.site.register(Attachment, AttachmentAdmin)

