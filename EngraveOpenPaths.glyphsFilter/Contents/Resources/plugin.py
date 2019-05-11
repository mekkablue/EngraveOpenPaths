# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class EngraveOpenPaths(FilterWithoutDialog):
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Engrave Open Paths',
			'de': u'Offene Pfade für AI schließen',
		})
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		for path in layer.paths:
			if not path.closed:
				path.closed = True
				path.nodes = path.nodes[1:]+[path.nodes[0]]
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	