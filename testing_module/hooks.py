# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "testing_module"
app_title = "Testting"
app_publisher = "Frappe"
app_description = "module of testing"
app_icon = "octico octicon-briefcase"
app_color = "#589494"
app_email = "gerson.caballero@grintsys.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/testing_module/css/testing_module.css"
# app_include_js = "/assets/testing_module/js/testing_module.js"

# include js, css files in header of web template
# web_include_css = "/assets/testing_module/css/testing_module.css"
# web_include_js = "/assets/testing_module/js/testing_module.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "testing_module.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "testing_module.install.before_install"
# after_install = "testing_module.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "testing_module.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"testing_module.tasks.all"
# 	],
# 	"daily": [
# 		"testing_module.tasks.daily"
# 	],
# 	"hourly": [
# 		"testing_module.tasks.hourly"
# 	],
# 	"weekly": [
# 		"testing_module.tasks.weekly"
# 	]
# 	"monthly": [
# 		"testing_module.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "testing_module.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "testing_module.event.get_events"
# }

