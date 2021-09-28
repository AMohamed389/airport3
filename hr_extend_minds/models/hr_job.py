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


class hr_job(models.Model):
    _inherit = 'hr.job'

    x_qualitative_group_id = fields.Many2one('qualitative_group',string="Qualitative Group", index=True, tracking=True)
    
    x_job_degree_id = fields.Many2one('job_degree', string="Degree", index=True, tracking=True)
    
    x_is_limited = fields.Boolean(string="Is Limited ?", index=True, tracking=True)