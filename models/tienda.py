# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
    _name = 'co.tienda'
    _description = 'CO Tienda'

    _columns = {
        'name' : fields.char('Tienda'),
        'address' : fields.char('Dirección'),
    }

tienda()
