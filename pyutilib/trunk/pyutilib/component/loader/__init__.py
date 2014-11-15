#  _________________________________________________________________________
#
#  PyUtilib: A Python utility library.
#  Copyright (c) 2008 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  _________________________________________________________________________

from pyutilib.component.core import PluginGlobals
PluginGlobals.push_env("pca")

from pyutilib.component.loader.plugin_importLoader import *
from pyutilib.component.loader.plugin_eggLoader import *

PluginGlobals.pop_env()
