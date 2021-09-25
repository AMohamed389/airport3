# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import datetime
from datetime import date
import logging
_logger = logging.getLogger(__name__)


class taxation(models.Model):
    _inherit = 'hr.payslip'


    def get_salary_m_taxes(self, emp_id, netgross):

        emp_rec = self.env['hr.contract'].search([('employee_id', '=', int(emp_id))])
        dt_start = emp_rec.date_start
        _logger.info('dt_start maged ! "%s"' % (str(dt_start)))

        today = date.today()
        _logger.info('today maged ! "%s"' % (str(today)))

        start_month = datetime.strptime(str(dt_start), "%Y-%m-%d").month
        _logger.info('start_month maged ! "%s"' % (str(start_month)))
        start_year = datetime.strptime(str(dt_start), "%Y-%m-%d").year
        _logger.info('start_year maged ! "%s"' % (str(start_year)))

        current_month = today.month
        _logger.info('current_month maged ! "%s"' % (str(current_month)))
        current_year = today.year
        _logger.info('current_year maged ! "%s"' % (str(current_year)))

        net_salary_flag = emp_rec.net_salary_flag

        if net_salary_flag == True:
            return taxation.reversePaySlip(self, emp_id, netgross)

        else:
            return taxation.EgyPayroll(self, emp_id, netgross)

    def sum_inputs_codes(self, payslip_id, code, contract_id):

        _logger.info('self.id maged ! "%s"' % (str(payslip_id)))
        _logger.info('code maged ! "%s"' % (str(code)))
        _logger.info('contract_id maged ! "%s"' % (str(contract_id)))

        inputs = self.env['hr.payslip.input'].search([('payslip_id','=',payslip_id)])
        _logger.info('inputs maged ! "%s"' % (str(inputs)))

        result = 0.0

        for input in inputs:
            if input[0]['code'] == code and int(input[0]['contract_id'])  == contract_id:
                result = result + input[0]['amount']

        _logger.info('result maged ! "%s"' % (str(result)))

        return result

    def SalaryTaxTo600Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (15000 / 12):
            _logger.info('salary <= (15000 / 12) ==> maged !')
            tax0 = salary * 0
            _logger.info('tax0 = salary * 0 ==> maged ! "%s"' % (str(tax0)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
            _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

            if 0 <= salary_after_deduct_tax <= (15000 / 12):
                _logger.info('(0 / 12) <= salary_after_deduct_tax <= (15000 / 12) ==> maged 1 !')
                tax2_5 = salary_after_deduct_tax * 0.025
                _logger.info('tax2_5 = salary_after_deduct_tax * 0.025 ==> maged ! "%s"' % (str(tax2_5)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                return result
            else:
                tax2_5 = (15000/12) * 0.025
                _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                _logger.info('tax2_5 ==> maged ! "%s"' % (str(tax2_5)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))


            if 0 <= salary_after_deduct_tax <= (15000 / 12):
                _logger.info('0 <= salary_after_deduct_tax <= (15000 / 12) ==> maged !')
                tax10= salary_after_deduct_tax * 0.1
                _logger.info('tax10 = salary_after_deduct_tax * 0.1 ==> maged ! "%s"' % (str(tax10)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                return result
            else:
                tax10 = (15000 / 12) * 0.1
                _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                _logger.info('tax10 ==> maged ! "%s"' % (str(tax10)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                if 0 <= salary_after_deduct_tax <= (15000 / 12):
                    _logger.info('0 <= salary_after_deduct_tax <= (15000 / 12) ==> maged !')
                    tax15 = salary_after_deduct_tax * 0.15
                    _logger.info('tax15 = salary_after_deduct_tax * 0.15 ==> maged ! "%s"' % (str(tax15)))
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                        str(result)))
                    return result
                else:
                    tax15 = (15000 / 12) * 0.15
                    _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                    salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                    _logger.info('tax15 ==> maged ! "%s"' % (str(tax15)))
                    _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                    if 0 <= salary_after_deduct_tax <= (140000 / 12):
                        _logger.info('0 <= salary_after_deduct_tax <= (140000 / 12) ==> maged !')
                        tax20 = salary_after_deduct_tax * 0.2
                        _logger.info('tax20 = salary_after_deduct_tax * 0.20 ==> maged ! "%s"' % (str(tax20)))
                        result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                        _logger.info(
                            'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                str(result)))
                        return result
                    else:
                        tax20 = (140000 / 12) * 0.2
                        _logger.info('(140000 / 12) ==> maged ! "%s"' % (str((140000 / 12))))
                        salary_after_deduct_tax = salary_after_deduct_tax - (140000 / 12)
                        _logger.info('tax20 ==> maged ! "%s"' % (str(tax20)))
                        _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                        if 0 <= salary_after_deduct_tax <= (200000 / 12):
                            _logger.info('0 <= salary_after_deduct_tax <= (200000 / 12) ==> maged !')
                            tax22_5 = salary_after_deduct_tax * 0.225
                            _logger.info('tax22_5 = salary_after_deduct_tax * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
                            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                            _logger.info(
                                'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                    str(result)))
                            return result
                        else:
                            tax22_5 = (200000 / 12) * 0.225
                            _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
                            salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
                            _logger.info('tax22_5 ==> maged ! "%s"' % (str(tax22_5)))
                            _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                            if salary_after_deduct_tax >= (200001 / 12):
                                _logger.info('salary_after_deduct_tax >= (200001 / 12) ==> maged !')
                                tax25 = salary_after_deduct_tax * 0.25
                                _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                                _logger.info(
                                    'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                        str(result)))
                                return result
                            else:
                                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                                return result

    def SalaryTaxFrom601To700Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (30000 / 12):
            _logger.info('salary <= (30000 / 12) ==> maged !')
            tax2_5 = salary * 0.025
            _logger.info('tax2_5 = salary * 0.025 ==> maged ! "%s"' % (str(tax2_5)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            tax2_5 = (30000 / 12) * 0.025
            _logger.info('(30000 / 12) ==> maged ! "%s"' % (str((30000 / 12))))
            salary_after_deduct_tax = salary_after_deduct_tax - (30000 / 12)
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (30000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

            if 0 <= salary_after_deduct_tax <= (15000 / 12):
                _logger.info('(0 / 12) <= salary_after_deduct_tax <= (15000 / 12) ==> maged 1 !')
                tax10 = salary_after_deduct_tax * 0.1
                _logger.info('tax10 = salary_after_deduct_tax * 0.1 ==> maged ! "%s"' % (str(tax10)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info(
                    'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                return result
            else:
                tax10 = (15000 / 12) * 0.1
                _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                _logger.info('tax10 ==> maged ! "%s"' % (str(tax10)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                if 0 <= salary_after_deduct_tax <= (15000 / 12):
                    _logger.info('0 <= salary_after_deduct_tax <= (15000 / 12) ==> maged !')
                    tax15 = salary_after_deduct_tax * 0.15
                    _logger.info('tax10 = salary_after_deduct_tax * 0.15 ==> maged ! "%s"' % (str(tax15)))
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                    return result
                else:
                    tax15 = (15000 / 12) * 0.15
                    _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                    salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                    _logger.info('tax15 ==> maged ! "%s"' % (str(tax15)))
                    _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))


                    if 0 <= salary_after_deduct_tax <= (140000 / 12):
                        _logger.info('0 <= salary_after_deduct_tax <= (140000 / 12) ==> maged !')
                        tax20 = salary_after_deduct_tax * 0.2
                        _logger.info('tax20 = salary_after_deduct_tax * 0.20 ==> maged ! "%s"' % (str(tax20)))
                        result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                        _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                str(result)))
                        return result

                    else:

                        tax20 = (140000 / 12) * 0.2
                        _logger.info('(140000 / 12) ==> maged ! "%s"' % (str((140000 / 12))))
                        salary_after_deduct_tax = salary_after_deduct_tax - (140000 / 12)
                        _logger.info('tax20 ==> maged ! "%s"' % (str(tax20)))
                        _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                        if 0 <= salary_after_deduct_tax <= (200000 / 12):
                            _logger.info('0 <= salary_after_deduct_tax <= (200000 / 12) ==> maged !')
                            tax22_5 = salary_after_deduct_tax * 0.225
                            _logger.info('tax22_5 = salary_after_deduct_tax * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
                            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                            return result

                        else:
                            tax22_5 = (200000 / 12) * 0.225
                            _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
                            salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
                            _logger.info('tax22_5 ==> maged ! "%s"' % (str(tax22_5)))
                            _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                            if salary_after_deduct_tax >= (200001 / 12):
                                _logger.info('salary_after_deduct_tax >= (200001 / 12) ==> maged !')
                                tax25 = salary_after_deduct_tax * 0.25
                                _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                                _logger.info(
                                    'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                        str(result)))

                                return result
                            else:
                                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                                return result

    def SalaryTaxFrom701To800Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (45000 / 12):
            _logger.info('salary <= (45000 / 12) ==> maged !')
            tax10 = salary * 0.1
            _logger.info('tax10 = salary * 0.1 ==> maged ! "%s"' % (str(tax10)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            tax2_5 = (45000 / 12) * 0.1
            _logger.info('(45000 / 12) ==> maged ! "%s"' % (str((45000 / 12))))
            salary_after_deduct_tax = salary_after_deduct_tax - (45000 / 12)
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (30000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

            if 0 <= salary_after_deduct_tax <= (15000 / 12):
                _logger.info('(0 / 12) <= salary_after_deduct_tax <= (15000 / 12) ==> maged 1 !')
                tax15 = salary_after_deduct_tax * 0.15
                _logger.info('tax10 = salary_after_deduct_tax * 0.15 ==> maged ! "%s"' % (str(tax15)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
                return result

            else:
                tax15 = (15000 / 12) * 0.15
                _logger.info('(15000 / 12) ==> maged ! "%s"' % (str((15000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (15000 / 12)
                _logger.info('tax15 ==> maged ! "%s"' % (str(tax15)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                if 0 <= salary_after_deduct_tax <= (140000 / 12):
                    _logger.info('0 <= salary_after_deduct_tax <= (140000 / 12) ==> maged !')
                    tax20 = salary_after_deduct_tax * 0.2
                    _logger.info('tax20 = salary_after_deduct_tax * 0.20 ==> maged ! "%s"' % (str(tax20)))
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                        str(result)))
                    return result

                else:

                    tax20 = (140000 / 12) * 0.2
                    _logger.info('(140000 / 12) ==> maged ! "%s"' % (str((140000 / 12))))
                    salary_after_deduct_tax = salary_after_deduct_tax - (140000 / 12)
                    _logger.info('tax20 ==> maged ! "%s"' % (str(tax20)))
                    _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                    if 0 <= salary_after_deduct_tax <= (200000 / 12):
                        _logger.info('0 <= salary_after_deduct_tax <= (200000 / 12) ==> maged !')
                        tax22_5 = salary_after_deduct_tax * 0.225
                        _logger.info('tax22_5 = salary_after_deduct_tax * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
                        result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                        _logger.info(
                            'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                str(result)))
                        return result

                    else:
                        tax22_5 = (200000 / 12) * 0.225
                        _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
                        salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
                        _logger.info('tax22_5 ==> maged ! "%s"' % (str(tax22_5)))
                        _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                        if salary_after_deduct_tax >= (200001 / 12):
                            _logger.info('salary_after_deduct_tax >= (200001 / 12) ==> maged !')
                            tax25 = salary_after_deduct_tax * 0.25
                            _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                            _logger.info(
                                'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                    str(result)))

                            return result
                        else:
                            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                            return result

    def SalaryTaxFrom801To900Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (60000 / 12):
            _logger.info('salary <= (60000 / 12) ==> maged !')
            tax15 = salary * 0.15
            _logger.info('tax15 = salary * 0.15 ==> maged ! "%s"' % (str(tax15)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            tax2_5 = (60000 / 12) * 0.15
            _logger.info('(60000 / 12) ==> maged ! "%s"' % (str((60000 / 12))))
            salary_after_deduct_tax = salary_after_deduct_tax - (60000 / 12)
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (30000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

            if 0 <= salary_after_deduct_tax <= (140000 / 12):
                _logger.info('0 <= salary_after_deduct_tax <= (140000 / 12) ==> maged !')
                tax20 = salary_after_deduct_tax * 0.2
                _logger.info('tax20 = salary_after_deduct_tax * 0.20 ==> maged ! "%s"' % (str(tax20)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                    str(result)))
                return result

            else:

                tax20 = (140000 / 12) * 0.2
                _logger.info('(140000 / 12) ==> maged ! "%s"' % (str((140000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (140000 / 12)
                _logger.info('tax20 ==> maged ! "%s"' % (str(tax20)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                if 0 <= salary_after_deduct_tax <= (200000 / 12):
                    _logger.info('0 <= salary_after_deduct_tax <= (200000 / 12) ==> maged !')
                    tax22_5 = salary_after_deduct_tax * 0.225
                    _logger.info('tax22_5 = salary_after_deduct_tax * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    _logger.info(
                        'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                            str(result)))
                    return result

                else:
                    tax22_5 = (200000 / 12) * 0.225
                    _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
                    salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
                    _logger.info('tax22_5 ==> maged ! "%s"' % (str(tax22_5)))
                    _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                    if salary_after_deduct_tax >= (200001 / 12):
                        _logger.info('salary_after_deduct_tax >= (200001 / 12) ==> maged !')
                        tax25 = salary_after_deduct_tax * 0.25
                        _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                        result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                        _logger.info(
                            'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                                str(result)))

                        return result
                    else:
                        result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                        return result

    def SalaryTaxFrom901To1000Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (200000 / 12):
            _logger.info('salary <= (200000 / 12) ==> maged !')
            tax20 = salary * 0.2
            _logger.info('tax20 = salary * 0.2 ==> maged ! "%s"' % (str(tax20)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            tax20 = (200000 / 12) * 0.2
            _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
            salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))


            if 0 <= salary_after_deduct_tax <= (200000 / 12):
                _logger.info('0 <= salary_after_deduct_tax <= (200000 / 12) ==> maged !')
                tax22_5 = salary_after_deduct_tax * 0.225
                _logger.info('tax22_5 = salary_after_deduct_tax * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info(
                    'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                        str(result)))
                return result

            else:
                tax22_5 = (200000 / 12) * 0.225
                _logger.info('(200000 / 12) ==> maged ! "%s"' % (str((200000 / 12))))
                salary_after_deduct_tax = salary_after_deduct_tax - (200000 / 12)
                _logger.info('tax22_5 ==> maged ! "%s"' % (str(tax22_5)))
                _logger.info('salary_after_deduct_tax ==> maged ! "%s"' % (str(salary_after_deduct_tax)))

                if salary_after_deduct_tax >= (200001 / 12):
                    _logger.info('salary_after_deduct_tax >= (200001 / 12) ==> maged !')
                    tax25 = salary_after_deduct_tax * 0.25
                    _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    _logger.info(
                        'result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (
                            str(result)))

                    return result
                else:
                    result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                    return result

    def SalaryTaxFrom1001Layer(self,salary):

        tax0 = 0.0
        tax2_5 = 0.0
        tax10 = 0.0
        tax15 = 0.0
        tax20 = 0.0
        tax22_5 = 0.0
        tax25 = 0.0
        result = 0.0
        personal_exempt = (1 / 12) * 9000
        salary = salary - personal_exempt
        salary_after_deduct_tax = salary

        if salary <= (400000 / 12):
            _logger.info('salary <= (400000 / 12) ==> maged !')
            tax22_5 = salary * 0.225
            _logger.info('tax22_5 = salary * 0.225 ==> maged ! "%s"' % (str(tax22_5)))
            result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
            _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))
            return result

        else:
            tax20 = (400000 / 12) * 0.225
            _logger.info('(400000 / 12) ==> maged ! "%s"' % (str((400000 / 12))))
            salary_after_deduct_tax = salary_after_deduct_tax - (400000 / 12)
            _logger.info('salary_after_deduct_tax = salary_after_deduct_tax - (400000 / 12) ==> maged ! "%s"' % (str(salary_after_deduct_tax)))


            if salary_after_deduct_tax >= 0:
                _logger.info('salary_after_deduct_tax >= 0 ==> maged !')
                tax25 = salary_after_deduct_tax * 0.25
                _logger.info('tax25 = salary_after_deduct_tax * 0.25 ==> maged ! "%s"' % (str(tax25)))
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                _logger.info('result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25 ==> maged ! "%s"' % (str(result)))

                return result
            else:
                result = tax0 + tax2_5 + tax10 + tax15 + tax20 + tax22_5 + tax25
                return result

    def EgyPayroll(self, emp_id, netgross):

        salary = netgross

        result = 0.0

        # personal_exempt = (1 / 12) * 9000
        # salary = salary - personal_exempt
        annual_netgross_salary = 12 * salary

        if annual_netgross_salary < 0:
            return result
        elif 0 <= annual_netgross_salary <= 600000:
            result = taxation.SalaryTaxTo600Layer(self, salary)
            return result
        elif 600001 <= annual_netgross_salary <= 700000:
            result = taxation.SalaryTaxFrom601To700Layer(self, salary)
            return result
        elif 700001 <= annual_netgross_salary <= 800000:
            result = taxation.SalaryTaxFrom701To800Layer(self, salary)
            return result
        elif 800001 <= annual_netgross_salary <= 900000:
            result = taxation.SalaryTaxFrom801To900Layer(self, salary)
            return result
        elif 900001 <= annual_netgross_salary <= 1000000:
            result = taxation.SalaryTaxFrom901To1000Layer(self, salary)
            return result
        elif annual_netgross_salary >= 1000001:
            result = taxation.SalaryTaxFrom1001Layer(self, salary)
            return result

    def reversePaySlip(self, emp_id, netSalary):

        emp_rec = self.env['hr.contract'].search([('employee_id', '=', int(emp_id))])
        dt_start = emp_rec.date_start
        salary = netSalary
        _logger.info('dt_start maged ! "%s"' % (str(dt_start)))
        _logger.info('salary maged ! "%s"' % (str(salary)))
        result = 0.0

        today = date.today()
        _logger.info('today maged ! "%s"' % (str(today)))

        start_month = datetime.strptime(str(dt_start), "%Y-%m-%d").month
        _logger.info('start_month maged ! "%s"' % (str(start_month)))
        start_year = datetime.strptime(str(dt_start), "%Y-%m-%d").year
        _logger.info('start_year maged ! "%s"' % (str(start_year)))

        current_month = today.month
        _logger.info('current_month maged ! "%s"' % (str(current_month)))
        current_year = today.year
        _logger.info('current_year maged ! "%s"' % (str(current_year)))


        if salary <= 2000:
            return result
        elif 2000 < salary <= 43572.92:
            result = taxation.SalaryTaxTo600ReverseLayer(self,salary)
            return result
        elif 43572.92 < salary <= 45812.50:
            result = taxation.SalaryTaxFrom601To700ReverseLayer(self,salary)
            return result
        elif 45812.50 < salary <= 51875.00:
            result = taxation.SalaryTaxFrom701To800ReverseLayer(self,salary)
            return result
        elif 51875.00 < salary <= 57937.50:
            result = taxation.SalaryTaxFrom801To900ReverseLayer(self,salary)
            return result
        elif 57937.50 < salary <= 63937.50:
            result = taxation.SalaryTaxFrom901To1000ReverseLayer(self,salary)
            return result
        elif salary > 63937.50:
            result = taxation.SalaryTaxFrom1001Layer(self,salary)
            return result

    def SalaryTaxTo600ReverseLayer(self,salary):

        grossSalaryPartialy = 0.0

        if 2000 < salary <= 3218.75:
            grossSalaryPartialy = salary - 50
            percent = 0.975
            return (grossSalaryPartialy/percent)

        elif 3218.75 < salary <= 4343.75:
            grossSalaryPartialy = salary - 293.75
            percent = 0.9
            return (grossSalaryPartialy / percent)

        elif 4343.75 < salary <= 5406.25:
            grossSalaryPartialy = salary - 518.75
            percent = 0.85
            return (grossSalaryPartialy / percent)

        elif 5406.25 < salary <= 14739.58:
            grossSalaryPartialy = salary - 806.25
            percent = 0.8
            return (grossSalaryPartialy / percent)

        elif 14739.58 < salary <= 27656.25:
            grossSalaryPartialy = salary - 1241.66651666667
            percent = 0.775
            return (grossSalaryPartialy / percent)

        elif 27656.25 < salary <= 39593.75:
            grossSalaryPartialy = salary - 2093.746667
            percent = 0.75
            return (grossSalaryPartialy / percent)
        else:
            return 0.0

    def SalaryTaxFrom601To700ReverseLayer(self,salary):

        return salary

    def SalaryTaxFrom601To700ReverseLayer(self,salary):

        return salary

    def SalaryTaxFrom701To800ReverseLayer(self,salary):

        return salary

    def SalaryTaxFrom801To900ReverseLayer(self,salary):

        return salary

    def SalaryTaxFrom901To1000ReverseLayer(self,salary):

        return salary

    def SalaryTaxFrom1001Layer(self,salary):

        return salary





