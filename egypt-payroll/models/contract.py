# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import datetime
from datetime import date
import logging
_logger = logging.getLogger(__name__)


class hrContractExtend(models.Model):

    _inherit = "hr.contract"

    insurance_wage = fields.Monetary('Insurance Wage', digits=(16, 2), track_visibility="always",help="Employee's monthly insurance wage.",index=True,store=True)

    net_salary_flag = fields.Boolean(name="Is Net Salary ?", index=True, store=True, default=False, help="Is Net Salary ?", track_visibility='always')
