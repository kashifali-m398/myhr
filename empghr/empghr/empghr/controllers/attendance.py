import frappe
from frappe import _
from frappe.utils import getdate, nowdate
from erpnext.hr.utils import set_employee_name
from frappe.utils import cstr

from erpnext.hr.doctype.attendance.attendance import Attendance
from erpnext.controllers.status_updater import validate_status


# def validate(doc):
   
#     validate_status(doc.status, ["Present", "Absent", "On Leave", "Half Day"])
#     validate_attendance_date(doc)
#     validate_duplicate_record(doc)
#     check_leave_record(doc)

# def validate_attendance_date(doc):

#     date_of_joining = frappe.db.get_value("Employee", doc.employee, "date_of_joining")

#     if getdate(doc.attendance_date) > getdate(nowdate()):
#         frappe.throw(_("Attendance can not be marked for future dates"))
#     elif date_of_joining and getdate(doc.attendance_date) < getdate(date_of_joining):
#         frappe.throw(_("Attendance date can not be less than employee's joining date"))

# # overriding attendance controller function
# def validate_duplicate_record(doc):

#     # if document is submitted then check only submitted documents,
#     # or else check for boht saved and submitted documents
#     doctstatus = ["1"]
#     if(doc.docstatus == 0):
#         doctstatus = ["0","1"]

#     # fetching records to check if already exists
#     documents = frappe.get_list("Attendance", "*", {"employee" : doc.employee, "docstatus": ["in" , doctstatus ], "attendance_date" : doc.attendance_date , "type" : doc.type})
    
#     if(len(documents) > 0):

#         # if already checkedin, then return
#         if(doc.type == "checkin"):
#             frappe.throw(_("check in for employee {0} is already marked").format(doc.employee))
       
#         elif(doc.type == "checkout"):
            
#             frappe.db.sql("update tabAttendance set time = %s where name = %s", (doc.time, documents[0].name))
#             frappe.db.commit()

#             frappe.throw(_("Already marked check out for employee {0}, time has been updated").format(doc.employee))
    
#     set_employee_name(doc)


# def check_leave_record(doc):

#     leave_record = frappe.db.sql("""select leave_type, half_day, half_day_date from `tabLeave Application`
#         where employee = %s and %s between from_date and to_date and status = 'Approved'
#         and docstatus = 1""", (doc.employee, doc.attendance_date), as_dict=True)
#     if leave_record:
#         for d in leave_record:
#             if d.half_day_date == getdate(doc.attendance_date):
#                 doc.status = 'Half Day'
#                 frappe.msgprint(_("Employee {0} on Half day on {1}").format(doc.employee, doc.attendance_date))
#             else:
#                 doc.status = 'On Leave'
#                 doc.leave_type = d.leave_type
#                 frappe.msgprint(_("Employee {0} is on Leave on {1}").format(doc.employee, doc.attendance_date))

#     if doc.status == "On Leave" and not leave_record:
#         frappe.throw(_("No leave record found for employee {0} for {1}").format(doc.employee, doc.attendance_date))


# def pass_validate(doc, method):
#     Attendance.validate = validate(doc)
		