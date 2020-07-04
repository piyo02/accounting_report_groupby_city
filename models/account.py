# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2017-Today Sitaram
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class AccountReportByCiity(models.TransientModel):
    _name = 'account.account.report'

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date(string="End Date", required=True)
    city_ids = fields.Many2many("vit.kota", string='Kota')

    
    @api.multi
    def print_accounting_report_by_city(self):
        groupby_dict = {}

        for city in self.city_ids:
            partners = self.env['res.partner'].search([('kota_id.name', '=', city.name)])
        
            for partner in partners:
                invoices = self.env['account.invoice'].search([ ('date_invoice', '>=', self.start_date), ('date_invoice', '<=', self.end_date), ('state', '=', 'open'), ['partner_id.name', '=', partner.display_name] ])
                groupby_dict[city.name] = invoices

        final_dict = {}
        for city in groupby_dict.keys():
            temp = []
            for invoice in groupby_dict[city]:
                temp_2 = []
                temp_2.append(invoice.partner_id.name)
                temp_2.append(invoice.date_invoice)
                temp_2.append(invoice.number)
                temp_2.append(invoice.date_due)
                temp_2.append(invoice.origin)
                temp_2.append(invoice.amount_total_signed )
                temp_2.append(invoice.residual_signed )
                temp.append(temp_2)
            final_dict[city] = temp
        datas = {
            'ids': self.ids,
            'model': 'account.account.report',
            'form': final_dict,
            'start_date': self.start_date,
            'end_date': self.end_date,

        }
        return self.env['report'].get_action(self,'accounting_report_groupby_city.city_temp', data=datas)
