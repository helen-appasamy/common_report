# -*- coding: utf-8 -*-
from odoo import fields, models

class ApprovalCountExcel(models.AbstractModel):
    _name = 'report.email_template.report_approval_count'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("State Level Counts")
        format1 = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcenter'})
        sheet.write(0, 0, 'State', format1)
        sheet.write(0, 1, 'Count', format1)
        sheet.write(1, 0, 'To Approve', format2)
        for obj in lines:
            sheet.write(1, 1, obj.approve_count, format2)
        sheet.write(2, 0, 'Sent', format2)
        for obj in lines:
            sheet.write(2, 1, obj.sent_count, format2)
        sheet.write(3, 0, 'Draft', format2)
        for obj in lines:
            sheet.write(3, 1, obj.draft_count, format2)
