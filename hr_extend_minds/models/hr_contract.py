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


class hr_contract(models.Model):
    _inherit = 'hr.contract'
    

    bonus = fields.Monetary(string="Bonus", index=True, tracking=True)
    bonus_text = fields.Char(string="Bonus Text", index=True, tracking=True)
    basic_text = fields.Char(string="Basic Text", index=True, tracking=True)
    equal_degree = fields.Selection([('الأولى', 'الأولى'),
                                    ('الثانية', 'الثانية'),
                                    ('الثالثة', 'الثالثة'),
                                    ('الرابعة', 'الرابعة'),
                                    ('الخامسة', 'الخامسة'),
                                    ('السادسة', 'السادسة'),
                                    ('عالية', 'عالية'),
                                    ('ممتازة', 'ممتازة'),
                                    ('مدير عام', 'مدير عام'),
                                    ('عقد مؤقت', 'عقد مؤقت'),
                                    ('أجر مقابل عمل', 'أجر مقابل عمل'),
                                     ], string="Equal Degree", index=True, tracking=True)
    
    sector = fields.Char(related="employee_id.x_sector_name", string="Sector")
    public_administration = fields.Char(related="employee_id.x_public_administration_name", string="Public Administration")
    administration = fields.Char(related="employee_id.x_administration_name", string="Administration")
    section = fields.Char(related="employee_id.x_section_name", string="Section")
    receiving_work_date = fields.Date(related="employee_id.x_receiving_work_date", string="Receive Work Date")
    qualitative_group_id = fields.Many2one(related="employee_id.x_qualitative_group_id", string="Qualitative Group")
    

    


    