# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class solicitud(osv.osv):
    _name = 'co.solicitud'
    _description = 'CO Solicitud'
    _rec_name = 'code'
    _order = 'requested_date desc'

    _columns = {
        'code': fields.char('Código', required=True),
        'suscriptor_id' : fields.many2one('co.suscriptor', 'Afiliado', required=True),
        'multimedia_id' : fields.many2one('co.multimedia', 'Multimedia', required=True),
        'medio_id' : fields.many2one('co.tipo.medio', 'Tipo de medio', required=True),
        'tienda_id' : fields.many2one('co.tienda', 'Origen', required=True),
        'requested_date' : fields.date('Fecha solicitada', required=True),
        'qty_days' : fields.integer('Duración (en días)', required=True),
    }

solicitud()
