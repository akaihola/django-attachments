from django import forms

from django.apps.attachments.models import Attachment


class AttachmentForm(forms.ModelForm):
    
    class Meta:
        model = Attachment
        exclude = ('content_type', 'object_id', 'attached_by')