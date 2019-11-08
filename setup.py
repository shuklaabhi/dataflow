#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import setuptools
import setuptools.command.test


class Meta(object):
    name = 'dataflow'
    version = '1.0'
    description = 'Sam[ple]'
    long_description = 'Long description'
    keywords = ['ariflow', 'data']
    author = 'Abhishek'
    author_email = 'shuklaabhishek02@gmail.com'
    contact = 'shuklaabhishek02@gmail.com'
    url = 'dataflow.github.io'
    homepage = 'https://dataflow.github.io'
    license = 'Apache 3.0'


meta = Meta


# -*- Requirements -*-


def _strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (_strip_comments(l) for l in open(
            os.path.join(os.getcwd(), 'requirements', *f)).readlines()) if r
    ]


def reqs(*f):
    """Parse requirement file.

    Example:
        reqs('default.txt')          # requirements/default.txt
        reqs('extras', 'redis.txt')  # requirements/extras/redis.txt
    Returns:
        List[str]: list of requirements specified in the file.
    """
    return [req for subreq in _reqs(*f) for req in subreq]


# -*- Command: setup.py test -*-


class Pytest(setuptools.command.test.test):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        setuptools.command.test.test.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest as _pytest
        sys.exit(_pytest.main(self.pytest_args))


# -*- %%% -*-

setuptools.setup(
    name=meta.name,
    packages=setuptools.find_packages(exclude=['tests']),
    version=meta.version,
    description=meta.description,
    long_description=meta.long_description,
    keywords=meta.keywords,
    author=meta.author,
    author_email=meta.contact,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Monitoring',
    ],
    url=meta.homepage,
    license=meta.license,
    platforms=['any'],
    install_requires=reqs('common.txt'),
    python_requires=">=3.5",
    tests_require=reqs('tests.txt'),
    cmdclass={'test': Pytest},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'dataflow = dataflow.bin.cli:main',
        ]
    },
)
