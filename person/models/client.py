from odoo import models, fields


class CustomClient(models.Model):
    _name = 'custom.client'
    _description = 'Model of a client'
    _inherit = 'abstract.person'

    photo = fields.Char(string="photo")

    postalcode = fields.Char(string="postalcode")