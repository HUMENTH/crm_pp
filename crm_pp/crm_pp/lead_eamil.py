import frappe
from frappe.utils import get_url_to_form

def send_lead_owner_notification(doc, method=None):
    """Send email only when Lead Owner changes"""

    previous_doc = doc.get_doc_before_save()

    if not previous_doc or doc.lead_owner == previous_doc.lead_owner:
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

    lead_name = doc.lead_name or "Unnamed Lead"
    company_name = doc.company_name or "N/A"
    lead_link = get_url_to_form("Lead", doc.name)

    assigner = frappe.get_doc("User", frappe.session.user)
    assigner_name = assigner.full_name or assigner.first_name or assigner.name

    subject = f"Lead: {lead_name} has been assigned to you."

    # Email body
    body = f"""
        <p>Lead: <b>{lead_name}</b>, {company_name} has been assigned to you.</p>
        <p>To view the details of this lead in crm.promptpersonnel.com, click on the following link:<br>
        <a href="{lead_link}">{lead_link}</a></p>
        <br>
        <p>Regards,<br>
        Prompt Personnel Pvt. Ltd.</p>
    """

    frappe.sendmail(
        recipients=[assigned_user.email],
        sender=frappe.utils.get_formatted_email(assigner_name),
        subject=subject,
        message=body,
        reference_doctype="Lead",
        reference_name=doc.name
    )
