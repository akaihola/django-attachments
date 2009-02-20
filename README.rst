====================
 django-attachments
====================

A generic attachment framework for Django.

This is a branch from the original Chicago Django user group
project. The following changes have been made:

* 'attachments' module assumed to be directly in PYTHONPATH instead of
  django.apps.attachments
* title and summary not required by the model

From the `django-attachments Google Code page
<http://code.google.com/p/django-attachments/>`_:

    This is the first project by Chicago's Django user group.

    We use `Google Code <http://code.google.com/>`_ for issue
    tracking; please see GitHub for our `source code
    <http://github.com/korpios/django-chicago/tree>`_.

    The `mailing list
    <http://groups.google.com/group/django-attachments>`_ is hosted in
    Google Groups.


`Bob Haugen`_ writes in the announcement_:

    Incubated in my current cohousing project.  You can see the code
    `here
    <http://code.google.com/p/pinax-cohousing/source/browse/#svn/trunk/cohousing/apps/attachments>`_.

    Basically works.  If you want to check out the whole project, you
    will find that you can attach files to Circles (orgs of OrgType
    Circle), Meetings and Households (OrgType Household).

    But you might have better luck just checking out the attachments
    app.

--------------
 Instructions
--------------

Also from the announcement_ (by `Bob Haugen`_):

    What you need to do to attach files to you domain objects:

    In settings.py, add "attachments" to INSTALLED_APPS

    In your template, add::

        {% load attachment_inclusion_tag %}

    and then at the appropriate place::

        {% attachments your_domain_object %}

    Let me know if you run into any problems.

------------
 Background
------------

* `design talk and pseudo code
  <http://groups.google.com/group/django-attachments/browse_thread/thread/02995c38911b2e23/443e457c7181e3ad#443e457c7181e3ad>`_
* announcement_

.. _announcement: http://groups.google.com/group/django-attachments/msg/e345520274612105
.. _`Bob Haugen`: http://code.google.com/u/bob.haugen/
