# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from openerp.exceptions import UserError

class University(models.Model):
    _name = 'university.submission'
    # _description = 'university.university'
    _rec_name ='student_name'
    student_name = fields.Char(string='Student Name', required=True)
    parent_name = fields.Char(string='Parent Name', required=True)

    # desc = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    request_Date = fields.Date(string="request Date", default=datetime.today())
    level = fields.Selection(string="Student Academic Level",  selection=[('bsc', 'Bachelor'), ('Msc', 'Masters'), ('Phd', 'Doctorate')], required=True)
    accepted = fields.Boolean()
    sequence = fields.Char(string="Request sequence", compute='seq_compute' , store=True)

    @api.constrains('student_name','parent_name')
    def name_const(self):
        for rec in self:
            result = self.env['university.submission'].search([('parent_name','=',rec.parent_name),('student_name','=',rec.student_name),('id','!=',rec.id)])
            if len(result.ids) != 0:
                raise UserError(_('name must be unique'))

    @api.onchange('student_name','parent_name')
    def desc_change(self):
        for rec in self:
            if rec.parent_name and rec.student_name:
                rec.description = (rec.description or "") +" registration of "+ (rec.student_name or "") + " " + (rec.parent_name or "")

    # @api.depends('id')
    def seq_compute(self):
        for rec in self:

            num = 1
            # print(len(self.env['university.submission'].search([('id','<',rec.id)]).ids))
            num = num + len(self.env['university.submission'].search([('id','<',rec.id)]).ids)
            rec.sequence = 'Request -' + str(datetime.today().year) + "-" + str(num)

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    # @api.model
    # def create(self,values):
    #     print(values)
    #     dupe=self.pool.get('university.submission').search([('parent_name','=',values.get('parent_name')),
    #                                                 ('student_name','=',values.get('student_name'))])
    #     print(len(dupe))
    #     if len(dupe)
    #                 # rec.get('parent_name')==values.get('parent_name') and rec.get('student_name')==values.get('student_name'):
    #         raise ValidationError("name already exists")
    #
    #     else:
    #         return  super(University, self).create(values)