# -*- coding: utf-8 -*-
#!/usr/bin/env python

{
    'name' : 'Curso OpenErp',
    'description' : 'Este módulo es para aprender OpenErp',
    'author' : 'Lorenzo Piñango',
    'version' : 'dia1',
    'depends' : ['base', 'mail', ],
    'data' : [
        'security/curso_odoo_security.xml',
        'views/curso_odoo_view.xml',
        'views/multimedia_view.xml',
        'views/tipo_medio_view.xml',
        'views/tipo_suscripcion_view.xml',
        'views/suscriptor_view.xml',
        'views/tienda_view.xml',
        'views/suscripcion_view.xml',
        'views/solicitud_view.xml',
        'views/categoria_view.xml',
        'security/menu_security.xml',
        'security/ir.model.access.csv',
        'data/suscripcion_data.xml',
        'reports/listado_multimedia_report.xml',
        
    ],
    'demo' : [],
}