# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
    _rec_name = 'name'
    _order = 'identification asc'

    _columns = {
        'name' : fields.char('Nombre y Apellido', required=True),
        'identification' : fields.char('Cédula', required=True),
        'address' : fields.text('Dirección'),
    }

    _sql_constraints = [
        ('identification_uniq', 'unique(identification)', u'El número de cédula o pasaporte no se puede repetir.'),
    ]

suscriptor()