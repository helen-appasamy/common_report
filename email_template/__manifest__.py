# -*- coding: utf-8 -*-
{
    'name': 'Auto email generation',
    'version': '14.0',
    'summary': 'Sending an email daily about the pending orders available to the approval person accordingly',
    'description': """Auto email generation for the approval person""",
    'depends': ['base', 'contacts', 'purchase', 'mail',],
    'data': [
            "data/email_template.xml",
            "data/schedule_action.xml",
            "views/no_of_count.xml",
            "report/excel_report.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
