static-django-twitter-bootstrap
===============================

This package provides a Django_ app whose ``static`` folder contains the
compiled assets of `Twitter Bootstrap`_.

Each Bootstrap version will be tagged accordingly.

Setup
-----

1. Install the app::

    pip install static-django-twitter-bootstrap

2. Inlude it in your Django project::

    # settings.py:

    INSTALLED_APPS = (
        ...
        'static_django_twitter_bootstrap',
        ...
    )

3. Make sure ``django.contrib.staticfiles.finders.AppDirectoriesFinder`` is in
   your list of ``STATICFILES_FINDERS``.

Usage
-----

If you're not using an asset manager, you can just include them as usual in
your site templates.::

    {% load staticfiles %}
    ...
    <script type="text/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
    ...

.. _Django: https://www.djangoproject.com
.. _Twitter Bootstrap: http://twitter.github.io/bootstrap/
