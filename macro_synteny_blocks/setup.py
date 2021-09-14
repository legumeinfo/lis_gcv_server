#!/usr/bin/env python
# Python
import setuptools
from setuptools.command.build_py import build_py
# package
from macro_synteny_blocks import commands


PACKAGE_DIRECTORIES = {
  '': '.',
}


COMMAND_CLASS = {}


build_proto_command = 'build_proto'


class BuildPy(build_py):
  '''Custom build_py command class.'''

  def run(self):
    build_py.run(self)
    self.run_command(build_proto_command)


SETUP_REQUIRES = ('grpcio-tools>=1.39,<2',)
COMMAND_CLASS = {
  build_proto_command: commands.BuildProtos,
  'build_py': BuildPy
}


setuptools.setup(
  package_dir=PACKAGE_DIRECTORIES,
  setup_requires=SETUP_REQUIRES,
  cmdclass=COMMAND_CLASS,
)
