from odoo import models, fields
class libarary(models.Model):
	_name ="libarary.books"
	_rec_name ="book"

	requester =fields.Char(required=True)
	book =fields.Char(required=True)
	description =fields.Text()
	rantbook_date =fields.Datetime()
	quantity =fields.Integer()