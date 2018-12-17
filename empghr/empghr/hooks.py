# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "empghr"
app_title = "Empghr"
app_publisher = "kashif ali"
app_description = "customization of erpnext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kashif.sarwar@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/empghr/css/empghr.css"
# app_include_js = "/assets/empghr/js/empghr.js"

# include js, css files in header of web template
# web_include_css = "/assets/empghr/css/empghr.css"
# web_include_js = "/assets/empghr/js/empghr.js"

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
# get_website_user_home_page = "empghr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "empghr.install.before_install"
# after_install = "empghr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "empghr.notifications.get_notification_config"

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

doc_events = {
	# "Attendance" : {
    #     "validate" : "empghr.empghr.controllers.attendance.pass_validate",
    #     "before_save" : "empghr.empghr.controllers.attendance.pass_validate",
    #     "before_insert" : "empghr.empghr.controllers.attendance.pass_validate"
    # },
    "Shift Assignment" : {
        "before_update_after_submit" : "empghr.empghr.utils.documents.override_validate_update",
    }

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"empghr.tasks.all"
# 	],
# 	"daily": [
# 		"empghr.tasks.daily"
# 	],
# 	"hourly": [
# 		"empghr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"empghr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"empghr.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "empghr.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "empghr.event.get_events"
# }

fixtures = ["Attendance"]