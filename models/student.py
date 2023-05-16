from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"

    _description = "A school student"

    name = fields.Char(string='Name', required=True)

    age = fields.Integer(string="Age")

    is_graduated = fields.Boolean(string="Is graduated ?")

    note = fields.Text(string="Notes")

    gender = fields.Selection([('Male','male'),('Female','female'),('Other','other')], string="Gender")


