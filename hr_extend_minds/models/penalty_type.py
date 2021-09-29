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


class penaltytype(models.Model):
    _name = 'penalty.type'
    _description = 'Penalty Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'x_name'
    _order = 'create_date DESC'

    x_name = fields.Char(string='Name', store=True, index=True, tracking=True)

    x_code = fields.Char(string='Penalty Code', store=True, index=True, tracking=True)

    x_notes = fields.Text(string="Notes", tracking=True, store=True)

    active = fields.Boolean(string='Active',index=True,default=True,tracking=True)