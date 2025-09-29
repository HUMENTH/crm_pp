import frappe
from frappe.utils import now_datetime

def update_lead_assign_date(doc, method):
    if doc.reference_type == "Lead" and doc.reference_name:
        assigned_time = now_datetime()
        
        frappe.db.set_value("Lead", doc.reference_name, "custom_assigned_date", assigned_time)

        frappe.publish_realtime(
            event="update_lead_assign_date",
            message={"lead": doc.reference_name, "assigned_time": str(assigned_time)},
            doctype="Lead",
            docname=doc.reference_name
        )
