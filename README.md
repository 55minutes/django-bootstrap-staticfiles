# static-django-twitter-bootstrap

This package provides a [Django][] app whose `static` folder contains the
compiled assets of [Twitter Bootstrap][].

Each Bootstrap version will be tagged accordingly.

## Setup

1.  Install the app:

    ```bash
    pip install static-django-twitter-bootstrap
    ```

2.  Inlude it in your Django project:

    ```python
    # settings.py:

    INSTALLED_APPS = (
        ...
        'static_django_twitter_bootstrap',
        ...
    )
    ```

3.  Make sure `django.contrib.staticfiles.finders.AppDirectoriesFinder` is in
    your list of `STATICFILES_FINDERS`.

## Usage

If you're not using an asset manager, you can just include them as usual in
your site templates.

```html
{% load staticfiles %}
...
<script type="text/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
...
```

[Django]: https://www.djangoproject.com
[Twitter Bootstrap]: http://twitter.github.io/bootstrap/
