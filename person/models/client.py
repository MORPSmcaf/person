from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomClient(models.Model):
    _name = 'custom.client'
    _description = 'Model of a client'
    _inherit = 'abstract.person'

    photo = fields.Binary(string="Photo")
    postalcode = fields.Char(string="Postal Code")

    @api.constrains('postalcode')
    def _check_postalcode(self):
        for record in self:
            if record.postalcode and len(record.postalcode) != 6:
                raise ValidationError("Postal Code must be exactly 6 characters long")
