# This file is part sale_pos_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['SaleTicketReport']
__metaclass__ = PoolMeta


class SaleTicketReport(JasperReport):
    __name__ = 'sale_pos.sale_ticket'

    @classmethod
    def execute(cls, ids, data):
        if len(ids) > 1:
            pdfs = []
            for id in ids:
                report = super(SaleTicketReport, cls).execute([id], data)
                pdfs.append(report[1])
                dprint = report[1]

            merged = cls.merge_pdfs(pdfs)
            return ('pdf', bytearray(merged), dprint, 'sale_ticket')
        else:
            return super(SaleTicketReport, cls).execute(ids, data)
