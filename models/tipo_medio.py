# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tipo_medio(osv.osv):
    _name = 'co.tipo.medio'
    _description = 'CO Tipo Medio'

    _columns = {
        'name' : fields.char('Nombre', required=True),
    }

tipo_medio()
