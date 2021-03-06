# -*- coding: utf-8 -*-

# ERPNext - web based ERP (http://erpnext.com)
# Copyright (C) 2012 Web Notes Technologies Pvt Ltd
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# default settings that can be made for a profile.
from __future__ import unicode_literals

import webnotes

lang_names = {
	"हिंदी": "hi",
	"deutsch": "de",
	"english": "en",
	"español": "es",
	"français": "fr",
	"português": "pt",
	"português brasileiro": "pt-BR",
	"nederlands": "nl",
	"српски":"sr",
	"தமிழ்": "ta",
	"hrvatski": "hr",
	"italiano": "it",
	"ไทย": "th",
	"العربية":"ar"
}

lang_list = ["ar", "de", "en", "es", "fr", "hi", "hr", "it", "nl", "pt-BR", "pt", "th", "sr", "ta"]

product_name = "ERPNext"
profile_defaults = {
	"Company": "company",
	"Territory": "territory"
}

application_home_page = "desktop"

# add startup propertes
mail_footer = """<div style="padding: 7px; text-align: right; color: #888"><small>Sent via 
	<a style="color: #888" href="https://erpnext.com">ERPNext</a></div>"""
	
def get_monthly_bulk_mail_limit():
	import webnotes
	# if global settings, then 500 or unlimited
	if webnotes.conn.get_value('Email Settings', None, 'outgoing_mail_server'):
		return 999999
	else:
		return 500

def get_url():
	from webnotes.utils import get_request_site_address
	url = get_request_site_address()
	if not url or "localhost" in url:
		subdomain = webnotes.conn.get_value("Website Settings", "Website Settings",
			"subdomain")
		if subdomain:
			if "http" not in subdomain:
				url = "http://" + subdomain
	return url
