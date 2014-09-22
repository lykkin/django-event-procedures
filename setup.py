from setuptools import setup


setup(
    name="django-event-procedures",
    version="0.1.2",
    author="Bryan Clement",
    author_email="bclement01@gmail.com",
    description="An event driven code execution system backed by Django",
    long_description=open("README.md", 'rb').read().decode('utf-8'),
    license="GNU",
    url="http://www.github.com/MindClickGlobal/django-event-procedures",
    include_package_data=True,
    packages=['event_procedures'],
    install_requires=[
        "django >= 1.5.0",
        "django-genericadmin >= 0.6.1"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
