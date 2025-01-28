# Copyright 2013 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

POSTLOGISTICS_TYPES = [
    ("label_layout", "Label Layout"),
    ("output_format", "Output Format"),
    ("resolution", "Output Resolution"),
    ("basic", "Basic Service"),
    ("additional", "Additional Service"),
    ("delivery", "Delivery Instructions"),
    ("partner_option", "Partner Option"),
]


class DeliveryCarrierTemplateOption(models.Model):
    _inherit = "delivery.carrier.template.option"

    type = fields.Selection(
        selection=POSTLOGISTICS_TYPES,
        string="PostLogistics option type",
    )
