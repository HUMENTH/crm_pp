app_name = "crm_pp"
app_title = "CRM PP"
app_publisher = "Octavision Software Solutions"
app_description = "CRM Fixtures"
app_email = "info@octavision.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "crm_pp",
# 		"logo": "/assets/crm_pp/logo.png",
# 		"title": "CRM PP",
# 		"route": "/crm_pp",
# 		"has_permission": "crm_pp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/crm_pp/css/crm_pp.css"
# app_include_js = "/assets/crm_pp/js/crm_pp.js"

# include js, css files in header of web template
# web_include_css = "/assets/crm_pp/css/crm_pp.css"
# web_include_js = "/assets/crm_pp/js/crm_pp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "crm_pp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Lead" : "public/js/crm_note.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "crm_pp/public/icons.svg"
app_include_js = [
    "/assets/crm_pp/js/crm_note.js","assets/crm_pp/js/custom_communication.js"
]

# app_include_js = "crm_pp/public/js/custom_communication.js"


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "crm_pp.utils.jinja_methods",
# 	"filters": "crm_pp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "crm_pp.install.before_install"
# after_install = "crm_pp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "crm_pp.uninstall.before_uninstall"
# after_uninstall = "crm_pp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "crm_pp.utils.before_app_install"
# after_app_install = "crm_pp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "crm_pp.utils.before_app_uninstall"
# after_app_uninstall = "crm_pp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crm_pp.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes




override_doctype_class = {
	"CRM Note": "crm_pp.crm_pp.crm_note_override.CRMNote"

}




# override_whitelisted_methods = {
#     "erpnext.crm.utils.add_note": "crm_pp.crm_pp.crm_note_override.add_note",
#     "erpnext.crm.utils.edit_note": "crm_pp.crm_pp.crm_note_override.edit_note",
#     "erpnext.crm.utils.delete_note": "crm_pp.crm_pp.crm_note_override.delete_note",
# }



# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# hooks.py
doc_events = {
#     "Lead": {
#         "validate": "crm_pp.lead_validations.validate_lead_phone"
#     },
#     "Lead": {
#         "before_validate": "crm_pp.lead_validations.allow_duplicate_email"
#     },
    # "ToDo": {
    #     "after_insert": "crm_pp.crm_pp.custom_lead.update_lead_assign_date"
    # },
    "Lead": {
        "on_update": "crm_pp.crm_pp.lead_eamil.send_lead_owner_notification",
        "before_save":"crm_pp.crm_pp.lead_owner.save_previous_owner"
    }


}



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"crm_pp.tasks.all"
# 	],
# 	"daily": [
# 		"crm_pp.tasks.daily"
# 	],
# 	"hourly": [
# 		"crm_pp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crm_pp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"crm_pp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "crm_pp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crm_pp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "crm_pp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["crm_pp.utils.before_request"]
# after_request = ["crm_pp.utils.after_request"]

# Job Events
# ----------
# before_job = ["crm_pp.utils.before_job"]
# after_job = ["crm_pp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"crm_pp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    # {
    #     "dt": "Custom Field",
    #     "filters": [
    #         ["module", "=", "CRM PP"]  # Your app's module name
    #     ]
    # },
    # {
    #     "dt": "Property Setter",
    #     "filters": [
    #         ["module", "=", "CRM PP"]
    #     ]
    # },
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", ["Lead", "Opportunity", "Customer", "Contact"]]
        ]
    },
    {
        "dt": "Property Setter",
        "filters": [
            ["doc_type", "in", ["Lead", "Opportunity", "Customer", "Contact"]]
        ]
    },
    "Client Script",
    "Server Script"
]