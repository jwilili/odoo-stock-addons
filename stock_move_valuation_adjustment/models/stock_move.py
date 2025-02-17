# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class StockMove(models.Model):

    _inherit = "stock.move"

    valuation_adjustment_line_ids = fields.One2many(
        "stock.valuation.adjustment.lines", "move_id"
    )
