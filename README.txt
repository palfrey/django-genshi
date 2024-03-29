:Author: John Millikin
:Copyright: This document has been placed in the public domain.

Overview
========

``django-genshi`` is a small wrapper library around Genshi that provides
an API similar to ``django.template``. Included are imitations of
``Context`` and ``RequestContext``. There is also an implemention of the
Django template loader system adapted for Genshi, and a selection of
shortcut functions.

Usage
=====

See the `Django` [#]_ and `Genshi` [#]_ documentation for detailed usage notes.
The API of ``django-genshi`` is intended to mirror that of Django, while
writing or manipulating the templates will require knowledge of Genshi.

Genshi cannot use Django's default template loaders -- to work around this,
the ``app_directories``, ``eggs``, and ``filesystem`` loaders have been
modified and included in the ``django_genshi.loaders`` package. To avoid
conflicts with Django's template system, place such loaders in the
``GENSHI_TEMPLATE_LOADERS`` setting.

Example::

    >>> from django_genshi import render_to_response
    >>> response = render_to_response ('template_name.xml', {"name": "world"})
    >>> print response.content
    <h1>Hello world!</h1>

.. [#] http://docs.djangoproject.com/en/dev/ref/templates/api/
.. [#] http://genshi.edgewall.org/wiki/Documentation

Output Type Autodetection
=========================

Because Genshi is based on abstract markup streams, it is possible for a
template to be rendered to multiple output representations (such as HTML or
XHTML). The decision of which to render is usually based on the HTTP
``Accept`` header. The ``shortcuts.render_to_response_autodetect`` function
implements a reasonable algorithm for autodetecting output formats, and
serves as an example for writing custom encoders in general.

Filters
=======

Arbitrary Genshi filter functions may be registered, using the
``GENSHI_TEMPLATE_FILTERS`` setting. They will be applied to generated
template streams by the shortcut functions prior to rendering the
streams. Example filters are included in the ``django_genshi.filters``
module.
