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


class trainingcatalogue(models.Model):
    _name = 'training.catalogue'
    _description = 'Training Catalogue'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'x_name'
    _order = 'create_date DESC'

    x_training_cost = fields.Monetary(string='Training Cost', index=True, tracking=True, store=True,
                                      currency_field='x_currency_id')

    x_image = fields.Binary(string='Image', store=True)

    x_name = fields.Char(string='Name', store=True, index=True, tracking=True)

    x_training_type = fields.Selection(
        [('Technical', 'Technical'), ('Managerial', 'Managerial'), ('IT', 'IT'), ('Languages', 'Languages'),
         ('Diploma', 'Diploma'), ('Seminars And Conferences', 'Seminars And Conferences')],
        string="Training Type", store=True, 
        index=True, tracking=True)

    x_training_code = fields.Char(string='Training Code', store=True, index=True, tracking=True)

    x_training_level = fields.Selection(
        [('Basic', 'Basic'), ('Advanced', 'Advanced'), ('Specialist', 'Specialist')],
        string="Training Level", store=True, 
        index=True, tracking=True)

    x_notes = fields.Text(string="Notes", tracking=True, store=True)

    x_responsible_id = fields.Many2one('hr.employee', string="Responsible", store=True,
                                           tracking=True, index=True)

    x_currency_id = fields.Many2one('res.currency', string="Currency", store=True,
                                           tracking=True, index=True)

    active = fields.Boolean(string='Active',index=True,default=True,tracking=True)