
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IDENTIFICADOR NUMERO RESERVADO SIMBOLO_ESPECIAL STRING bloque : SIMBOLO_ESPECIAL declaraciones SIMBOLO_ESPECIAL\n     declaraciones : declaracion declaraciones \n                      | declaracion\n     declaracion : operacion \n                    | asignacion \n                    | funcion \n                    | inclusion \n                    | retorno \n     operacion : valor SIMBOLO_ESPECIAL valor \n     valor : IDENTIFICADOR\n                | NUMERO\n     asignacion : RESERVADO IDENTIFICADOR SIMBOLO_ESPECIAL valor SIMBOLO_ESPECIAL \n                    | RESERVADO IDENTIFICADOR SIMBOLO_ESPECIAL\n                    | IDENTIFICADOR SIMBOLO_ESPECIAL operacion SIMBOLO_ESPECIAL \n                    | IDENTIFICADOR SIMBOLO_ESPECIAL valor \n     funcion : RESERVADO RESERVADO SIMBOLO_ESPECIAL SIMBOLO_ESPECIAL bloque \n                | RESERVADO SIMBOLO_ESPECIAL argumentos SIMBOLO_ESPECIAL SIMBOLO_ESPECIAL \n                | RESERVADO SIMBOLO_ESPECIAL argumentos SIMBOLO_ESPECIAL bloque\n     argumentos : argumento SIMBOLO_ESPECIAL argumentos \n                    | argumento\n     argumento : asignacion\n                    | STRING\n                    | referencia\n                    | incremento\n                    | IDENTIFICADOR\n     referencia : SIMBOLO_ESPECIAL IDENTIFICADOR\n     incremento : IDENTIFICADOR SIMBOLO_ESPECIAL\n     retorno : RESERVADO valor SIMBOLO_ESPECIAL\n     inclusion : RESERVADO RESERVADO\n    '
    
_lr_action_items = {'SIMBOLO_ESPECIAL':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,22,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[2,14,-3,-4,-5,-6,-7,-8,16,19,21,-11,-1,-2,24,25,27,35,-9,-10,38,-13,42,43,-21,-22,-23,-24,44,-28,45,16,2,47,25,-26,48,27,-27,-14,-16,-12,-17,-18,-19,]),'$end':([1,14,],[0,-1,]),'RESERVADO':([2,4,5,6,7,8,9,11,13,14,17,19,22,23,25,35,37,43,45,46,47,48,49,],[11,11,-4,-5,-6,-7,-8,17,-11,-1,-29,26,-9,-10,-13,-28,-15,26,-14,-16,-12,11,-18,]),'IDENTIFICADOR':([2,4,5,6,7,8,9,11,13,14,16,17,19,21,22,23,25,26,27,35,37,43,44,45,46,47,48,49,],[12,12,-4,-5,-6,-7,-8,18,-11,-1,23,-29,34,23,-9,-10,23,40,41,-28,-15,34,23,-14,-16,-12,12,-18,]),'NUMERO':([2,4,5,6,7,8,9,11,13,14,16,17,21,22,23,25,35,37,44,45,46,47,48,49,],[13,13,-4,-5,-6,-7,-8,13,-11,-1,13,-29,13,-9,-10,13,-28,-15,13,-14,-16,-12,13,-18,]),'STRING':([19,43,],[31,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bloque':([0,38,42,],[1,46,49,]),'declaraciones':([2,4,48,],[3,15,3,]),'declaracion':([2,4,48,],[4,4,4,]),'operacion':([2,4,21,44,48,],[5,5,36,36,5,]),'asignacion':([2,4,19,43,48,],[6,6,30,30,6,]),'funcion':([2,4,48,],[7,7,7,]),'inclusion':([2,4,48,],[8,8,8,]),'retorno':([2,4,48,],[9,9,9,]),'valor':([2,4,11,16,21,25,44,48,],[10,10,20,22,37,39,37,10,]),'argumentos':([19,43,],[28,50,]),'argumento':([19,43,],[29,29,]),'referencia':([19,43,],[32,32,]),'incremento':([19,43,],[33,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> bloque","S'",1,None,None,None),
  ('bloque -> SIMBOLO_ESPECIAL declaraciones SIMBOLO_ESPECIAL','bloque',3,'p_expression_bloque','prueba.py',46),
  ('declaraciones -> declaracion declaraciones','declaraciones',2,'p_expression_declaraciones','prueba.py',51),
  ('declaraciones -> declaracion','declaraciones',1,'p_expression_declaraciones','prueba.py',52),
  ('declaracion -> operacion','declaracion',1,'p_expression_declaracion','prueba.py',57),
  ('declaracion -> asignacion','declaracion',1,'p_expression_declaracion','prueba.py',58),
  ('declaracion -> funcion','declaracion',1,'p_expression_declaracion','prueba.py',59),
  ('declaracion -> inclusion','declaracion',1,'p_expression_declaracion','prueba.py',60),
  ('declaracion -> retorno','declaracion',1,'p_expression_declaracion','prueba.py',61),
  ('operacion -> valor SIMBOLO_ESPECIAL valor','operacion',3,'p_expression_operacion','prueba.py',66),
  ('valor -> IDENTIFICADOR','valor',1,'p_expression_valor','prueba.py',71),
  ('valor -> NUMERO','valor',1,'p_expression_valor','prueba.py',72),
  ('asignacion -> RESERVADO IDENTIFICADOR SIMBOLO_ESPECIAL valor SIMBOLO_ESPECIAL','asignacion',5,'p_expression_asignacion','prueba.py',77),
  ('asignacion -> RESERVADO IDENTIFICADOR SIMBOLO_ESPECIAL','asignacion',3,'p_expression_asignacion','prueba.py',78),
  ('asignacion -> IDENTIFICADOR SIMBOLO_ESPECIAL operacion SIMBOLO_ESPECIAL','asignacion',4,'p_expression_asignacion','prueba.py',79),
  ('asignacion -> IDENTIFICADOR SIMBOLO_ESPECIAL valor','asignacion',3,'p_expression_asignacion','prueba.py',80),
  ('funcion -> RESERVADO RESERVADO SIMBOLO_ESPECIAL SIMBOLO_ESPECIAL bloque','funcion',5,'p_expression_funcion','prueba.py',85),
  ('funcion -> RESERVADO SIMBOLO_ESPECIAL argumentos SIMBOLO_ESPECIAL SIMBOLO_ESPECIAL','funcion',5,'p_expression_funcion','prueba.py',86),
  ('funcion -> RESERVADO SIMBOLO_ESPECIAL argumentos SIMBOLO_ESPECIAL bloque','funcion',5,'p_expression_funcion','prueba.py',87),
  ('argumentos -> argumento SIMBOLO_ESPECIAL argumentos','argumentos',3,'p_expression_argumentos','prueba.py',92),
  ('argumentos -> argumento','argumentos',1,'p_expression_argumentos','prueba.py',93),
  ('argumento -> asignacion','argumento',1,'p_expression_argumento','prueba.py',98),
  ('argumento -> STRING','argumento',1,'p_expression_argumento','prueba.py',99),
  ('argumento -> referencia','argumento',1,'p_expression_argumento','prueba.py',100),
  ('argumento -> incremento','argumento',1,'p_expression_argumento','prueba.py',101),
  ('argumento -> IDENTIFICADOR','argumento',1,'p_expression_argumento','prueba.py',102),
  ('referencia -> SIMBOLO_ESPECIAL IDENTIFICADOR','referencia',2,'p_expression_referencia','prueba.py',107),
  ('incremento -> IDENTIFICADOR SIMBOLO_ESPECIAL','incremento',2,'p_expression_incremento','prueba.py',112),
  ('retorno -> RESERVADO valor SIMBOLO_ESPECIAL','retorno',3,'p_expression_retorno','prueba.py',117),
  ('inclusion -> RESERVADO RESERVADO','inclusion',2,'p_expression_inclusion','prueba.py',122),
]
