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


class employeetraining(models.Model):
    _name = 'employee.training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'x_employee_id'
    _order = 'create_date DESC'

    x_assign_date = fields.Date(string='Assign Date', index=True, tracking=True)

    x_employee_id = fields.Many2one('hr.employee', string="Employee", store=True,
                                           tracking=True, index=True
                                       #, default=lambda self: self._get_employee_id()
                                            )

    x_end_date = fields.Date(string='End Date', index=True, tracking=True)

    x_training = fields.Many2one('training.catalogue', string="Training", store=True,
                                     tracking=True, index=True)

    x_training_type = fields.Selection(string="Training Type",related='x_training.x_training_type')

    x_training_code = fields.Char(string="Training Code", related='x_training.x_training_code')

    x_training_grade = fields.Selection(
        [('Fair', 'Fair'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')],
        string="Training Grade", store=True, 
        index=True, tracking=True)

    x_notes = fields.Text(string="Notes", tracking=True, store=True)

    state = fields.Selection(
        [('New', 'New'), ('Submit', 'Submit'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled')],
        string="Status", store=True, 
        index=True, tracking=True, default='New')

    x_start_date = fields.Date(string='Start Date', index=True, tracking=True)

    active = fields.Boolean(string='Active',index=True,default=True,tracking=True)


    #def _get_employee_id(self):
        #_logger.info('Maged _get_employee_id default_x_employee_id ! ' + str(self._context.get('default_x_employee_id')))
        #if self._context.get('default_x_employee_id'):
            #return int(self._context.get('default_x_employee_id'))

    def default_get(self, fields):
        res = super(employeetraining, self).default_get(fields)

        try:
            if self._context and self._context is not None and self._context.get('default_x_employee_id'):
                _logger.info('Maged default_get default_x_employee_id ! ' + str(self._context.get('default_x_employee_id')))
                res['x_employee_id'] = int(self._context.get('default_x_employee_id'))
                return res
        except:
            pass

        #res['x_notes'] = 'test'

        return res