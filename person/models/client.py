from odoo import models, fields

class Person_inher(models.Model):
    #_name = 'person.inherit'
    _description = 'Model of a client'
    _inherit = 'person.person'

    # Additional fields specific to clients
    # client_since = fields.Date(string='Client Since')
    photo = fields.Char(string="photo")
