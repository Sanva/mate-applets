# -*- coding: utf-8 -*-
from os.path import join
from gettext import gettext as _
from mate_invest.defs import VERSION
import mate_invest

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf

invest_logo = None
try:
	invest_logo = GdkPixbuf.Pixbuf.new_from_file_at_size(join(mate_invest.ART_DATA_DIR, "invest_neutral.svg"), 96, 96)
except Exception, msg:
	pass
	
def show_about():
	about = Gtk.AboutDialog()
	infos = {
		"program-name" : _("Invest"),
		"logo" : invest_logo,
		"version" : VERSION,
		"comments" : _("Track your invested money."),
		"copyright" : "Copyright © 2004-2005 Raphael Slinckx\nCopyright © 2009-2010 Enrico Minack\nCopyright © 2012-2016 MATE developers"
	}

#	about.set_authors("Raphael Slinckx <raphael@slinckx.net>\nEnrico Minack <enrico-minack@gmx.de>")
#	about.set_artists([])
#	about.set_documenters([])
	
	#translators: These appear in the About dialog, usual format applies.
	about.set_translator_credits( _("translator-credits") )
	
	for prop, val in infos.items():
		about.set_property(prop, val)
	
	about.connect ("response", lambda self, *args: self.destroy ())
	about.show_all()
