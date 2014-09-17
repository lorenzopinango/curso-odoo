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


suscriptor()