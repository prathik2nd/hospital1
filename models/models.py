# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char('Hospital Name')
    address = fields.Text('Address')
    phone = fields.Char('Phone No')
    email = fields.Char('Email ID')

class Patients(models.Model):
    _name = 'hospital.patients'
    _description = 'patients'

    name = fields.Char('Patient Name')   
    address = fields.Text('Address')
    age = fields.Integer('Age')
    dob = fields.Date('Date of Birth')
    phone = fields.Char('Phone No')
    email = fields.Char('Email ID')

class Department(models.Model):
    _name ='hospital.department'
    _description ='hospital.department'

    name = fields.Char('Department Name')   
    desc = fields.Char('Description')


class LabTest(models.Model):
    _name = 'hospital.labtest'
    _description = 'labtest'

    name = fields.Char('Test Name')
    descri = fields.Char('Description')
    rate = fields.Integer('Test Rate')


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'doctor'

    name = fields.Char('Doctor Name')  
    dept_id = fields.Many2one('hospital.department','Department')
    address = fields.Char('Address')
    phone = fields.Char('Phone')
    email = fields.Char('Email ID')

class Medicine(models.Model):
    _name ='hospital.medicine'
    _description = 'medicine'

    name = fields.Char('Medicine Name')
    descri = fields.Char('Description')
    rate = fields.Integer('Rate')


class Registration(models.Model):
    _name = 'hospital.registration'
    _description = 'registration'


    name =fields.Char('Registration No')
    patient_id = fields.Many2one('hospital.patients','Patient Name')  
    dept_id = fields.Many2one('hospital.department','Department')
    doct_id = fields.Many2one('hospital.doctor','Doctor')
    cdate = fields.Date('Registration Date')
    phone = fields.Char('Phone')
    email = fields.Char('Email ID')
    tests = fields.Many2many('hospital.labtest', string='Test')
    state = fields.Selection([
        ('draft', 'Draft'),        
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

class Invoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'invoice'
    
    name = fields.Char('Invoice No')
    patient_id = fields.Many2one('hospital.patients','Patient Name')
    cdate = fields.Date('Date')
    remarks = fields.Char('Remarks')
    Madiname = fields.Many2many('hospital.medicine','medi_id','Medicine Name')



class QuotationOrder(models.Model):
    _name = 'quotation.order'
    _description = 'quotation.order'

    name = fields.Char('Customer Name')
    order_ids = fields.One2many('quotation.order.line', 'order_id', string='Order Line')
    cdate = fields.Date('Date')
    note = fields.Text('Terms and conditions')
    mulval= fields.Many2many('quotation.order.line', 'order_id', string='Products')

class QuotationOrderLine(models.Model):
    _name = 'quotation.order.line'
    _description = 'quotation.order.line'

    name = fields.Char('Product Name')
    order_id  = fields.Many2one('quotation.order',string='Q_Order')
    product_id = fields.Char('Product id')
    price = fields.Char('Price')
    qty = fields.Char('Quantity')






