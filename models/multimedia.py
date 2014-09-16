# -*- coding: utf-8 -*-

from openerp.osv import osv, field


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'

    _columns = {
        'title' : fields.char('Título'),
        'release_date' : fields.date('Fecha de publicación'),
        'code' : fields.char('Código'),
        'categoria_id' : fields.many2one('co.categoria', 'Categoría'),
        'medio_ids' : fields.many2many(
            'co.tipo.medio,
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id'),
    }

multimedia()
