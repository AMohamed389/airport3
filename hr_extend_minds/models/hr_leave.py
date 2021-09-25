# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests
from datetime import date

import logging

_logger = logging.getLogger(__name__)


class hrleaveextend(models.Model):

    _inherit = 'hr.leave'

    x_sector_name = fields.Char(related="employee_id.x_sector_name", index=True)
    x_public_administration_name = fields.Char(related="employee_id.x_public_administration_name", index=True)
    x_administration_name = fields.Char(related="employee_id.x_administration_name", index=True)
    x_section_name = fields.Char(related="employee_id.x_section_name", index=True)
    x_staff_id = fields.Char(related="employee_id.x_staff_id", index=True)
    x_issuer = fields.Char(string="Source", index=True, tracking=True)


    def write(self, vals):

        for _rec in self:
            _rec.validate_fl()

        result = super(hrleaveextend, self).write(vals)
        _logger.info(str("hr_leave write result : ") + str(result))
        return result
                


    def validate_fl(self):
        
        _leave_type_rec = self.env['hr.leave.type'].browse(self.holiday_status_id.id)
        _leave_code = _leave_type_rec.code
        _employee = self.employee_id
        _number_of_days = self.number_of_days

        if not _employee or not _leave_type_rec:
            return False
        
        # _emp_rec = self.env['hr.employee'].browse(_employee)
        # if not _emp_rec:
        #     return False

        #_logger.info("hrleaveextend validate_fl _emp_rec : " + str(_emp_rec))
        
        _todays_date = date.today()
        _current_year = _todays_date.year

        _employee_leaves = self.get_total_leaves_days(_leave_code=_leave_code)
        _total_number_of_days = _employee_leaves['total_number_of_days']
        
        if _total_number_of_days > 60:
            raise ValidationError("Year {0} consumed > 60 days for leave {1} !.".format(str(date.today().year), _leave_type_rec.name))

    # def validate_first_six_months(self):


    def get_total_leaves_days(self, _current_year=date.today().year, _request_date_from=str(date.today().year) + "-01-01", _request_date_to=str(date.today().year) + "-12-31", _leave_code=False):
        
        if not _leave_code:
            return _leave_code
        
        _leave_type_rec = self.env['hr.leave.type'].search([('code','=',_leave_code)],limit=1)
        _logger.info("hrleaveextend get_total_leaves_days _leave_type_rec : " + str(_leave_type_rec))

        if not _leave_type_rec:
            return _leave_type_rec

        _dict = {}
        _total_duration_days = 0
        _leaves_recs = self.env['hr.leave'].search([('request_date_from','>=',_request_date_from),
                        ('request_date_to','<=',_request_date_to),('state','=','validate'),
                        ('holiday_status_id','=',_leave_type_rec.id),
                        ('employee_id','=',self.employee_id.id)])
        
        _logger.info("hrleaveextend get_total_leaves_days _leaves_recs : " + str(_leaves_recs))

        for _rec in _leaves_recs:
            _dict[_rec.holiday_status_id.code] = {
                'request_date_from':_rec.request_date_from,
                'request_date_to':_rec.request_date_to,
                'number_of_days':_rec.number_of_days
            }
            _total_duration_days = _total_duration_days + _rec.number_of_days
        
        _dict['total_number_of_days'] = _total_duration_days
        _dict['employee_id'] = self.employee_id.id

        _logger.info("hrleaveextend get_total_leaves_days _dict : " + str(_dict))

        return _dict