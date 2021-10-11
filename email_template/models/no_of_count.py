# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class no_of_count(models.Model):
    _inherit= 'purchase.order'

    approve_count= fields.Integer(string="Approve Count", compute="_compute_state_count")
    draft_count= fields.Integer(string="Draft Count", compute="_compute_state_count")
    sent_count= fields.Integer(string="Sent Count", compute="_compute_state_count")

    @api.depends('state')
    def _compute_state_count(self):
        data_obj = self.env['purchase.order']
        for data in self:
            approve_data = data_obj.search_count([('state','in',['to approve'])])
            data.approve_count =approve_data
            draft_data = data_obj.search_count([('state','in',['draft'])])
            data.draft_count =draft_data
            sent_data = data_obj.search_count([('state','in',['sent'])])
            data.sent_count =sent_data

    def action_send_email(self):
        count = self.env.ref('email_template.template_for_the_state_count')
        if count:
            count.send_mail(self.id, force_send=True, raise_exception=True)
