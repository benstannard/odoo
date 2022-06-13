from odoo import models, fields

class LumberPackage(models.Model):
    _name = 'lumber.package'
    _description = 'A lumber package purchase'

    date = fields.Date(required=True)
    name = fields.Text(required=True)
    kind = fields.Selection(
            string='Type',
            selection=[('boards', 'Boards'), ('dimensional', 'Dimensional'), ('timber', 'Timber')])
    thickness = fields.Float(require=True)
    width = fields.Float(require=True)
    length = fields.Float(require=True)
    quantiy = fields.Integer(require=True)
    price = fields.Float(require=True)
