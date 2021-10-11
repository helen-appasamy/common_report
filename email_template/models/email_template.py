# -*- coding: utf-8 -*-
from odoo import fields, models

class email_template(models.Model):
    _inherit= 'mail.template'

class approval_levels(models.Model):
    _inherit= 'res.company'

    approval_level1 = fields.Many2one('res.users', string='Approval_Level1')
    approval_level2 = fields.Many2one('res.users', string='Approval_Level2')
