# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="static-django-twitter-bootstrap",
    version="2.3.2.1",
    packages=find_packages(),
    package_data={
        'static_django_twitter_bootstrap': [
            'static/css/*.css',
            'static/img/*.png',
            'static/js/bootstrap-*.js',
        ],
    },

    # metadata for upload to PyPI
    author="George Song",
    author_email="george@55minutes.com",
    description="Django app that provides compiled Bootstrap assets",
    license="MIT",
    keywords="django app staticfiles twitter bootstrap",
    url="https://github.com/55minutes/static-django-twitter-bootstrap",
    download_url="http://pypi.python.org/pypi/static-django-twitter-bootstrap",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ]
)
