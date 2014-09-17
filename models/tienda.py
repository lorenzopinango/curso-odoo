# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
    _name = 'co.tienda'
    _description = 'CO Tienda'
    _rec_name = 'name'

    _columns = {
        'name' : fields.char('Tienda', required=True),
        'address' : fields.char('Dirección'),
    }

tienda()
