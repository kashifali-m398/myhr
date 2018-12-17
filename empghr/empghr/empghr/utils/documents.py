import frappe
from frappe.model.base_document import BaseDocument


def _validate_update_after_submit(self):
		# get the full doc with children
		db_values = frappe.get_doc(self.doctype, self.name).as_dict()

		for key in self.as_dict():
			df = self.meta.get_field(key)
			db_value = db_values.get(key)

			if df and not df.allow_on_submit and (self.get(key) or db_value):
				if df.fieldtype=="Table":
					# just check if the table size has changed
					# individual fields will be checked in the loop for children
					self_value = len(self.get(key))
					db_value = len(db_value)

				else:
					self_value = self.get_value(key)


def override_validate_update(doc, method):
    BaseDocument._validate_update_after_submit = _validate_update_after_submit



		