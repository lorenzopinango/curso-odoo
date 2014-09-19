# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

TIPOS = [
    ('oro', 'Plan ORO'),
    ('plata', 'Plan PLATA'),
    ('bronce', 'Plan BRONCE')
]

class tipo_suscripcion(osv.osv):
    _name = 'co.tipo.suscripcion'
    _description = 'CO Tipo Suscripcion'

    _columns = {
        'name' : fields.char('Nombre', required=True),
        'medio_ids' : fields.many2many(
            'co.tipo.medio',
            'tipo_suscripcion_medio_rel',
            'tipo_id',
            'medio_id'),
    }

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'El nombre no puede repetirse'),
    ]

tipo_suscripcion()

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'
    _rec_name = 'code'
    _order = 'date_start desc'

    _columns = {
        'code' : fields.char('Código', help="El código se genera luego de guardar..."),
        'type' : fields.many2one('co.tipo.suscripcion', 'Tipo de suscripción', required=True),
        'date_start' : fields.date('Inicio suscripción', required=True),
        'date_end' : fields.date('Fin suscripción', required=True),
        'active' : fields.boolean('Activo', required=True),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado', required=True),
    }

    _defaults = {
        'active' : True,
        'date_start' : datetime.now().strftime('%Y-%m-%d'),
    }

    def _check_dates(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        for s in self.browse(cr, uid, ids, context=context):
            if s.date_end <= s.date_start:
                return False
        return True

    _constraints = [
        (_check_dates, 'Fecha de inicio debe ser menor a la fecha final', ['date_start', 'date_end']),
    ]

    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}
            
        values.update({
            'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
        return super(suscripcion, self).create(cr, uid, values, context=context)

suscripcion()

class suscriptor(osv.osv):
    _inherit = 'co.suscriptor'

    _columns = {
        'suscripcion_ids' : fields.one2many(
            'co.suscripcion', 'suscriptor_id'),
    }

suscriptor()