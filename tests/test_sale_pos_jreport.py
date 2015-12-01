# This file is part of the sale_pos_jreport module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SalePosJreportTestCase(ModuleTestCase):
    'Test Sale Pos Jreport module'
    module = 'sale_pos_jreport'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SalePosJreportTestCase))
    return suite