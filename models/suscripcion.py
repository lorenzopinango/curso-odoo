# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

TIPOS = [
    ('oro', 'Plan ORO'),
    ('plata', 'Plan PLATA'),
    ('bronce', 'Plan BRONCE')
]


class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'
    _rec_name = 'code'
    _order = 'date_start desc'

    _columns = {
        'code' : fields.char('Código'),
        'type' : fields.selection(TIPOS, 'Tipo de suscripción', required=True),
        'date_start' : fields.date('Inicio suscripción', required=True),
        'date_end' : fields.date('Fin suscripción', required=True),
        'active' : fields.boolean('Activo', required=True),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado', required=True),
    }

    _defaults = {
        'active' : True,
        'date_start' : datetime.now().strftime('%Y-%m-%d'),
    }

    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
        return super(suscripcion, self).create(cr, uid, values, context=context)

suscripcion()

