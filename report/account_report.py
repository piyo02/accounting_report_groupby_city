# from odoo import models, fields, api


# class TrialBalanceReport(models.TransientModel):
#     """ Here, we just define class fields.
#     For methods, go more bottom at this file.

#     The class hierarchy is :
#     * TrialBalanceReport
#     ** TrialBalanceReportAccount
#     *** TrialBalanceReportPartner
#             If "show_partner_details" is selected
#     """

#     _name = 'report_trial_balance_qweb'
#     _inherit = 'report_qweb_abstract'

#     # Filters fields, used for data computation
#     date_from = fields.Date()
#     date_to = fields.Date()
#     fy_start_date = fields.Date()
#     only_posted_moves = fields.Boolean()
#     hide_account_at_0 = fields.Boolean()
#     foreign_currency = fields.Boolean()
#     company_id = fields.Many2one(comodel_name='res.company')
#     filter_account_ids = fields.Many2many(comodel_name='account.account')
#     filter_partner_ids = fields.Many2many(comodel_name='res.partner')
#     filter_journal_ids = fields.Many2many(comodel_name='account.journal')
#     show_partner_details = fields.Boolean()
#     hierarchy_on = fields.Selection(
#         [('computed', 'Computed Accounts'),
#          ('relation', 'Child Accounts'),
#          ('none', 'No hierarchy')],
#         string='Hierarchy On',
#         required=True,
#         default='computed',
#         help="""Computed Accounts: Use when the account group have codes
#         that represent prefixes of the actual accounts.\n
#         Child Accounts: Use when your account groups are hierarchical.\n
#         No hierarchy: Use to display just the accounts, without any grouping.
#         """, period_balance=fields.Float(digits=(16, 2))
#     )
#     limit_hierarchy_level = fields.Boolean('Limit hierarchy levels')
#     show_hierarchy_level = fields.Integer('Hierarchy Levels to display',
#                                           default=1)
#     hide_parent_hierarchy_level = fields.Boolean(
#         'Do not display parent levels', default=False)
#     # General Ledger Report Data fields,
#     # used as base for compute the data reports
#     general_ledger_id = fields.Many2one(
#         comodel_name='report_general_ledger_qweb'
#     )

#     # Data fields, used to browse report data
#     account_ids = fields.One2many(
#         comodel_name='report_trial_balance_qweb_account',
#         inverse_name='report_id'
#     )