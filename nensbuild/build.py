from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


from fabric.contrib.files import exists

from fabric import local


def link():
    result_file = 'buildout.cfg'
    if not exists(result_file):
        local('ln -sf development.cfg %s' % result_file)


def bootstrap():
    result_file = 'bin/buildout'
    if not exists(result_file):
        local('python bootrap.py')


def buildout():
    local('bin/buildout')


def combine():
    link()
    bootstrap()
    buildout()
