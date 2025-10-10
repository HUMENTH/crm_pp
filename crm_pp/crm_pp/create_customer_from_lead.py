import frappe
from erpnext.crm.doctype.lead.lead import _make_customer

def create_customer_from_lead(doc, method=None):
    # frappe.msgprint("this is custom method====================")
    """
    Automatically create a Customer whenever a Lead is created.
    """
    try:
        existing_customer = frappe.db.exists("Customer", {"lead_name": doc.name})
        if existing_customer:
            return

        customer_doc = _make_customer(source_name=doc.name)

        customer_doc.insert(ignore_permissions=True)
        frappe.db.commit()

        frappe.logger().info(f" Customer auto-created for Lead: {doc.name}")

    except Exception as e:
        frappe.log_error(f"Error auto-creating Customer from Lead {doc.name}: {str(e)}")
