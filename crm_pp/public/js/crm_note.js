frappe.provide("erpnext.utils");

erpnext.utils.CRMNotes = class CRMNotes {
	constructor(opts) {
		$.extend(this, opts);
	}

	refresh() {
		frappe.msgprint("this is custom method ===========================")
		let me = this;
		this.notes_wrapper.find(".notes-section").remove();

		let notes = this.frm.doc.notes || [];
		notes.sort((a, b) => new Date(b.added_on) - new Date(a.added_on));

		let notes_html = frappe.render_template("crm_notes", { notes: notes });
		$(notes_html).appendTo(this.notes_wrapper);

		this.add_note();

		$(".notes-section").find(".edit-note-btn").on("click", function () {
			me.edit_note(this);
		});

		$(".notes-section").find(".delete-note-btn").on("click", function () {
			me.delete_note(this);
		});
	}

	add_note() {
		let me = this;
		let _add_note = () => {
			let d = new frappe.ui.Dialog({
				title: __("Add new Call Log"),
				fields: [
					{
						label: "Subject",
						fieldname: "subject",
						fieldtype: "Data",
						reqd: 1
					},
					{
						label: "Note",
						fieldname: "note",
						fieldtype: "Text Editor",
						reqd: 1,
						enable_mentions: true,
					},
				],
				primary_action: function () {
					let data = d.get_values();
					frappe.call({
						method: "add_note",
						doc: me.frm.doc,
						args: {
							subject: data.subject,
							note: data.note,
						},
						freeze: true,
						callback: function (r) {
							if (!r.exc) {
								me.frm.refresh_field("notes");
								me.refresh();
							}
							d.hide();
						},
					});
				},
				primary_action_label: __("Add"),
			});
			d.show();
		};
		$(".new-note-btn").off("click").on("click", _add_note);
	}

	edit_note(edit_btn) {
		let me = this;
		let row = $(edit_btn).closest(".comment-content");
		let row_id = row.attr("name");
		let row_subject = $(row).find(".subject").text();
		let row_content = $(row).find(".content").html();

		if (row_content) {
			let d = new frappe.ui.Dialog({
				title: __("Edit Note"),
				fields: [
					{
						label: "Subject",
						fieldname: "subject",
						fieldtype: "Data",
						default: row_subject,
						reqd: 1
					},
					{
						label: "Note",
						fieldname: "note",
						fieldtype: "Text Editor",
						default: row_content,
					},
				],
				primary_action: function () {
					let data = d.get_values();
					frappe.call({
						method: "edit_note",
						doc: me.frm.doc,
						args: {
							row_id: row_id,
							subject: data.subject,
							note: data.note,
						},
						freeze: true,
						callback: function (r) {
							if (!r.exc) {
								me.frm.refresh_field("notes");
								me.refresh();
								d.hide();
							}
						},
					});
				},
				primary_action_label: __("Done"),
			});
			d.show();
		}
	}

	delete_note(delete_btn) {
		let me = this;
		let row_id = $(delete_btn).closest(".comment-content").attr("name");
		frappe.call({
			method: "delete_note",
			doc: me.frm.doc,
			args: {
				row_id: row_id,
			},
			freeze: true,
			callback: function (r) {
				if (!r.exc) {
					me.frm.refresh_field("notes");
					me.refresh();
				}
			},
		});
	}
};
