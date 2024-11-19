from setuptools import setup, find_packages

setup(
    name='django_view_redirect_middleware',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    author='Open Library of Humanities',
    author_email='olh-tech@bbk.ac.uk',
    description='A Django middleware that redirects based on the current view name.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/openlibhums/django_view_redirect_middleware',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3',
    ],
    license='AGPL-3.0-or-later',
)
