#This file is part sale_pos_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['SaleTicketReport']
__metaclass__ = PoolMeta


class SaleTicketReport(JasperReport):
    __name__ = 'sale.sale_ticket'
