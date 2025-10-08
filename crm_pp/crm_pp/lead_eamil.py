import frappe
from frappe.utils import get_url_to_form

def send_lead_owner_notification(doc, method=None):
    """Send email only when Lead Owner changes"""

    previous_doc = doc.get_doc_before_save()
    
    if not previous_doc:
        return

    if doc.lead_owner == previous_doc.lead_owner:
        return

    if not doc.lead_owner:
        return

    assigned_user = frappe.db.get_value(
        "User",
        doc.lead_owner,
        ["full_name", "email", "enabled"],
        as_dict=True
    )

    if not assigned_user or not assigned_user.enabled:

        return

    lead_name = doc.lead_name or ""
    company_name = doc.company_name or ""
    lead_link = get_url_to_form("Lead", doc.name)

    assigner = frappe.get_doc("User", frappe.session.user)
    assigner_email = assigner.email or frappe.utils.get_formatted_email(assigner.name)

    subject = f"Lead Assigned: {lead_name or 'Unnamed Lead'}"
    body = f"""
        <p>Dear {assigned_user.full_name},</p>
        <p>A new lead has been assigned to you.</p>
        <p><b>Lead:</b> {lead_name or 'N/A'}<br>
        <b>Company:</b> {company_name or 'N/A'}</p>
        <p><a href="{lead_link}">Click here to open this Lead</a></p>
        <br>
        <p>Regards,<br>Prompt Personnel Pvt. Ltd.</p>
    """

    frappe.sendmail(
        recipients=[assigned_user.email],
        sender=assigner_email,
        subject=subject,
        message=body,
        reference_doctype="Lead",
        reference_name=doc.name
    )
