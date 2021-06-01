# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Hospital2(models.Model):
    _name = 'hospital.hospital'
    _description = 'An Erp for Hospital Management'

    d_name = fields.Char('Doctor', copy=True)
    appointment_num = fields.Integer('Appointment Number')
    note = fields.Text('Appointment Description')

    @api.constrains('appointment_num')
    def _check_doctor_appointment_days(self):
        for check in self:
            if check.appointment_num > 30:
                raise ValidationError(_('doctor must not have more than 30 appointment request in same day.'))
