# -*- coding: utf-8 -*-

from odoo import models, fields, api

class customer_validation(models.Model):
    _inherit = 'res.partner'

    stage = fields.Selection([
        ('new', 'New'),
        ('confirm', 'Confirm'),
        ('approved', 'Approved'),
    ], default='new')

    @api.one
    def reset_new(self):
        self.write({'stage': 'new'})

    @api.one
    def confirm(self):
        self.write({'stage': 'confirm'})

    @api.one
    def approved(self):
        self.write({'stage': 'approved'});
