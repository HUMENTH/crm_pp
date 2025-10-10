const OriginalCommunicationComposer = frappe.views.CommunicationComposer;

frappe.views.CommunicationComposer = class extends OriginalCommunicationComposer {
	get_fields() {
		let me = this;

		// Run custom fields only for Lead and Opportunity
		if (!["Lead", "Opportunity"].includes(this.frm?.doc?.doctype)) {
			return super.get_fields();
		}

		console.log("Custom get_fields() active for Lead/Opportunity...");

		const fields = [
			{
				label: __("To", null, "Email Recipients"),
				fieldtype: "MultiSelect",
				reqd: 0,
				fieldname: "recipients",
				default: this.get_default_recipients("recipients"),
			},
			{
				fieldtype: "Button",
				label: frappe.utils.icon("down", "xs"),
				fieldname: "option_toggle_button",
				click: () => {
					this.toggle_more_options();
				},
			},
			{
				fieldtype: "Section Break",
				hidden: 1,
				fieldname: "more_options",
			},
			{
				label: __("CC", null, "Email Recipients"),
				fieldtype: "MultiSelect",
				fieldname: "cc",
				default: this.get_default_recipients("cc"),
			},
			{
				label: __("BCC", null, "Email Recipients"),
				fieldtype: "MultiSelect",
				fieldname: "bcc",
				default: this.get_default_recipients("bcc"),
			},
			{
				label: __("Schedule Send At"),
				fieldtype: "Datetime",
				fieldname: "send_after",
			},
			{
				fieldtype: "Section Break",
				fieldname: "email_template_section_break",
				hidden: 1,
			},
			{
				label: __("Email Template"),
				fieldtype: "Link",
				options: "Email Template",
				fieldname: "email_template",
			},
			{
				fieldtype: "HTML",
				label: __("Clear & Add template"),
				fieldname: "clear_and_add_template",
			},
			{ fieldtype: "Section Break" },
			{
				label: __("Subject"),
				fieldtype: "Data",
				reqd: 1,
				fieldname: "subject",
				length: 524288,
			},
			{
				label: __("Message"),
				fieldtype: "Text Editor",
				fieldname: "content",
				onchange: frappe.utils.debounce(this.save_as_draft.bind(this), 300),
			},
			{
				fieldtype: "Button",
				label: __("Add Signature"),
				fieldname: "add_signature",
				hidden: 1,
				click: async () => {
					let sender_email = this.dialog.get_value("sender") || "";
					this.content_set = false;
					await this.set_content(sender_email);
				},
			},
			{ fieldtype: "Section Break" },
			{
				label: __("Send me a copy"),
				fieldtype: "Check",
				fieldname: "send_me_a_copy",
				default: frappe.boot.user.send_me_a_copy,
			},
			{
				label: __("Send Read Receipt"),
				fieldtype: "Check",
				fieldname: "send_read_receipt",
			},
			{
				label: __("Attach Document Print"),
				fieldtype: "Check",
				fieldname: "attach_document_print",
				hidden: 1,
			},
			{
				label: __("Select Print Format"),
				fieldtype: "Select",
				fieldname: "select_print_format",
				onchange: function () {
					me.guess_language();
				},
			},
			{
				label: __("Print Language"),
				fieldtype: "Link",
				options: "Language",
				fieldname: "print_language",
				default: frappe.boot.lang,
				depends_on: "attach_document_print",
			},
			{ fieldtype: "Column Break" },
			{
				label: __("Select Attachments"),
				fieldtype: "HTML",
				fieldname: "select_attachments",
			},
		];

		const email_accounts = frappe.boot.email_accounts.filter((account) => {
			return (
				!["All Accounts", "Sent", "Spam", "Trash"].includes(account.email_account) &&
				account.enable_outgoing
			);
		});

		if (email_accounts.length) {
			this.user_email_accounts = email_accounts.map((e) => e.email_id);

			fields.unshift({
				label: __("From", null, "Email Sender"),
				fieldtype: "Select",
				reqd: 1,
				fieldname: "sender",
				options: this.user_email_accounts,
				onchange: () => {
					this.setup_recipients_if_reply();
				},
			});

			if (this.user_email_accounts.length === 1) {
				this["sender"] = this.user_email_accounts[0];
			} else if (this.user_email_accounts.includes(frappe.session.user_email)) {
				this["sender"] = frappe.session.user_email;
			}
		}

		return fields;
	}

	setup_email() {
		if (!["Lead", "Opportunity"].includes(this.frm?.doc?.doctype)) {
			return super.setup_email();
		}

		const fields = this.dialog.fields_dict;

		if (fields.attach_document_print) {
			$(fields.attach_document_print.wrapper).hide();
		}

		if (fields.send_me_a_copy?.input) {
			$(fields.send_me_a_copy.input).on("click", () => {
				const val = fields.send_me_a_copy.get_value();
				frappe.db.set_value("User", frappe.session.user, "send_me_a_copy", val);
				frappe.boot.user.send_me_a_copy = val;
			});
		}
	}
};
