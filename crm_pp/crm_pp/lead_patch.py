import frappe

def execute():
    print("this is update lead record===================================")
    leads = frappe.get_all("Lead", fields=["name", "lead_owner"])
    for lead in leads:
        if lead.lead_owner:
            try:
                user = frappe.get_doc("User", lead.lead_owner)
                full_name = (user.first_name or "") + " " + (user.last_name or "")
                full_name = full_name.strip()

                if full_name:
                    frappe.db.set_value("Lead", lead.name, "lead_owner", full_name)
            except frappe.DoesNotExistError:
                pass

    frappe.db.commit()
    frappe.logger().info(" Lead Owner updated from email to full name.")

