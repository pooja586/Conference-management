import frappe

#send_email for conference invitation
@frappe.whitelist()
def send_invitation_emails(Name,Attendee,Agenda,Venue):
	url="http://localhost:8000/desk#Calendar/Event"

	msg = frappe.render_template("templates/email/conference_booking.html", {"Name":Name,"Attendee":Attendee,"Agenda": Agenda,"Venue": Venue,"base_url":url})	
	frappe.sendmail(
		recipients=Attendee,
		sender=frappe.session.user,
		subject="Conference Invitation",
		message=msg
	)
	
# For displaying conferences on calendar
@frappe.whitelist()
def get_conference(start=None,end=None,filters=None):
	import json
	filters=json.loads(filters)
 	if not frappe.has_permission("Conference booking","read"):
		raise frappe.PermissionError
	cal=frappe.db.sql("""select timestamp(date, from_time) as start_date,
			timestamp(date, to_time) as end_date,name,workflow_state
			from `tabConference booking`
			where workflow_state='Booked' and timestamp(date,from_time) between %(start)s 
			and %(end)s or timestamp(date,to_time) between %(start)s and %(end)s """,{
			"start":start,
			"end":end
			},as_dict=True)
	return cal







