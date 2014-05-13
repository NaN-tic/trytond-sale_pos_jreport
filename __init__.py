#This file is part sale_pos_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .sale import *


def register():
    Pool.register(
        SaleTicketReport,
        module='sale_pos_jreport', type_='report')
