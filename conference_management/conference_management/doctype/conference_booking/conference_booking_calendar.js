

frappe.views.calendar["Conference booking"] = {
	field_map: {
 		"start": "start_date",
 		"end": "end_date",
 		"id": "name",
 		"allDay": "allDay",
 		"name":"name",
 		// "child_name": "name",
 		"title":"name",
 		// "allDay": "allDay",
 		"Conference":"conference"
},
style_map: {
 	"0": "info", 
 	"1": "standard", 
 	"2": "pink"
},

gantt: true,
gantt_scale: "hours",
/*filters: [
		{
			"fieldtype": "Link",
			"fieldname": "conference",
			"options": "Conference",
			"label": __("Conference")
		},
	],*/
get_events_method: "conference_management.api.get_conference"

}