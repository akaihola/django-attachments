"""

>>> from attachments.models import *
>>> from django.contrib.auth.models import User
>>> from django.contrib.contenttypes.models import ContentType

>>> import os
>>> TEST_DIR = os.path.join(os.path.dirname(__file__))
>>> TEST_FILE1 = os.path.join(TEST_DIR, "models.py")
>>> TEST_FILE2 = os.path.join(TEST_DIR, "views.py")

>>> bob = User(username="bob")
>>> bob
<User: bob>
>>> bob.save()

>>> tm = TestModel(name="Test1")
>>> tm.name
'Test1'
>>> tm.save()


>>> att1 = Attachment.objects.create_for_object(
...     tm, file=TEST_FILE1, attached_by=bob, title="Something",
...     summary="Something more")
>>> att1
<Attachment: Something>


>>> att2 = Attachment.objects.create_for_object(
...     tm, file=TEST_FILE2, attached_by=bob, title="Something Else",
...     summary="Something else more")
>>> att2
<Attachment: Something Else>

>>> Attachment.objects.attachments_for_object(tm)
[<Attachment: Something Else>, <Attachment: Something>]


"""
