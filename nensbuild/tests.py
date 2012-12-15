from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

import unittest
import mock

from nensbuild import build


class TestBuild(unittest.TestCase):

    @mock.patch('subprocess.call')
    def run_func(self, func, exists_return_value, subprocess_call):
        with mock.patch('os.path.exists',
                        return_value=exists_return_value):
            func()
        return subprocess_call

    def test_create_link(self):
        call = self.run_func(build.link, False)
        self.assertTrue(call.called)
        call.assert_called_with(
            ['ln', '-sf', 'development.cfg', 'buildout.cfg'])

    def test_not_create_link(self):
        call = self.run_func(build.link, True)
        self.assertFalse(call.called)

    def test_run_boostrap(self):
        call = self.run_func(build.bootstrap, False)
        self.assertTrue(call.called)
        call.assert_called_with(
            ['python', 'bootstrap.py'])

    def test_not_run_bootstrap(self):
        call = self.run_func(build.bootstrap, True)
        self.assertFalse(call.called)

    def test_run_buildout(self):
        call = self.run_func(build.buildout, False)
        self.assertTrue(call.called)
        call.assert_called_with(['bin/buildout'])

    def test_run_all(self):
        call = self.run_func(build.main, False)
        self.assertEqual(call.call_count, 3)
