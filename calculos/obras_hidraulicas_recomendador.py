#!/usr/bin/env python
# -*- coding: utf-8 -*-

NUMENTRADAS = 4
NUMSALIDAS = 7
CABECERA = (u'CBR', u'D m\xe1x', u'Tama\xf1o escollera', u'Altura ca\xedda', u'Rt', u'Elong', u'R CBR perf', u'R perf cono', u'Abertura poro', u'K vert', u'Producto recomendado')
TABLA = [(u'[0..6)', u'[100..\u221e]', u'[300..\u221e]', u'[1..\u221e]', u'34', u'50', u'6,49', u'8', u'60', u'40', u'NT 58'), (u'[6..\u221e]', u'[100..\u221e]', u'[300..\u221e]', u'[1..\u221e]', u'39', u'50', u'6,91', u'6', u'60', u'40', u'NT 69'), (u'[0..6)', u'[100..\u221e]', u'[300..\u221e]', u'[0..1)', u'31', u'50', u'5,26', u'10', u'60', u'40', u'NT 46'), (u'[6..\u221e]', u'[100..\u221e]', u'[300..\u221e]', u'[0..1)', u'31', u'50', u'5,26', u'10', u'60', u'40', u'NT 46'), (u'[0..6)', u'[100..\u221e]', u'[0..300)', u'[1..\u221e]', u'23', u'50', u'3,93', u'10', u'60', u'40', u'NT 35'), (u'[6..\u221e]', u'[100..\u221e]', u'[0..300)', u'[1..\u221e]', u'25', u'50', u'4,49', u'10', u'60', u'40', u'NT 40'), (u'[0..6)', u'[100..\u221e]', u'[0..300)', u'[0..1)', u'15', u'50', u'2,57', u'20', u'60', u'40', u'NT 23'), (u'[6..\u221e]', u'[100..\u221e]', u'[0..300)', u'[0..1)', u'20', u'50', u'3,31', u'15', u'60', u'40', u'NT 30'), (u'[0..6)', u'[0..100)', u'[300..\u221e]', u'[1..\u221e]', u'31', u'50', u'5,26', u'10', u'60', u'40', u'NT 46'), (u'[6..\u221e]', u'[0..100)', u'[300..\u221e]', u'[1..\u221e]', u'34', u'50', u'6,49', u'8', u'60', u'40', u'NT 58'), (u'[0..6)', u'[0..100)', u'[300..\u221e]', u'[0..1)', u'25', u'50', u'4,49', u'10', u'60', u'40', u'NT 40'), (u'[6..\u221e]', u'[0..100)', u'[300..\u221e]', u'[0..1)', u'31', u'50', u'5,26', u'10', u'60', u'40', u'NT 46'), (u'[0..6)', u'[0..100)', u'[0..300)', u'[1..\u221e]', u'15', u'50', u'2,57', u'20', u'60', u'40', u'NT 23'), (u'[6..\u221e]', u'[0..100)', u'[0..300)', u'[1..\u221e]', u'15', u'50', u'2,57', u'20', u'60', u'40', u'NT 23'), (u'[0..6)', u'[0..100)', u'[0..300)', u'[0..1)', u'13', u'50', u'2,26', u'21', u'60', u'40', u'NT 21'), (u'[6..\u221e]', u'[0..100)', u'[0..300)', u'[0..1)', u'15', u'50', u'2,57', u'20', u'60', u'40', u'NT 23')]
RANGOS = {u'CBR': (0, 2147483647), u'Altura ca\xedda': (0, 2147483647), u'D m\xe1x': (0, 2147483647), u'Tama\xf1o escollera': (0, 2147483647)}