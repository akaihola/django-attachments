from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from attachments.models import *
from attachments.forms import *


@login_required
def new_attachment(request, content_type, object_id):
    object_type = get_object_or_404(ContentType, id = int(content_type))
    try:
        object = object_type.get_object_for_this_type(pk=int(object_id))
    except object_type.DoesNotExist:
        raise Http404
    if request.method == "POST":
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.content_type = object_type
            attachment.object_id = object_id
            attachment.attached_by = request.user
            attachment.save()
            return HttpResponseRedirect(object.get_absolute_url())
    else:
        attachment_form = AttachmentForm()
    
    return render_to_response("attachments/new_attachment.html", {
        "attachment_form": attachment_form,
        "object": object
    }, context_instance=RequestContext(request))
    
@login_required
def delete_attachment(request, attachment_slug):
    attachment = get_object_or_404(Attachment, slug=attachment_slug)
    object_type = attachment.content_type
    try:
        object = object_type.get_object_for_this_type(pk=attachment.object_id)
    except object_type.DoesNotExist:
        raise Http404
    if request.method == "POST":
        attachment.delete()
    return HttpResponseRedirect(object.get_absolute_url())


