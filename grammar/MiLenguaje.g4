grammar MiLenguaje;

programa : (registro)* (variables)* (sub_rutinas)* body;

registro : 'registro' ID (variables)* 'fin' 'registro';

variables : 'arreglo' TOP (parametos)* TCP 'de' T ID
    | T ID (TCM ID)*
    ;

parametos : TOP T (TCM T)* TCP;

T : 'entero'
  | 'real'
  | 'booleano'
  | 'cadena' TOB 'tkn_integer' TCB
  | 'caracter'
  | 'var'
  | ID
  ;

sub_rutinas : (funciones)*
    | (procedimiento)*
    | ;

funciones : 'funcion' ID (parametos)* TCN T (variables)* 'inicio' (sentencias)* (retorno)? 'fin';

retorno : 'retorne' expresion;

procedimiento : 'procedimiento' ID (parametos)* (variables)* (sentencias)* 'fin'
   ;

body : 'inicio' (sentencias)* 'fin'
  ;

sentencias : ciclos
  | condicional
  | asignacion
  | esc_lec
  | casos
  | llamada
  | ;

ciclos : 'mientras' expresion 'haga' sentencias 'fin' 'mientras'
  | 'repita' sentencias 'hasta' expresion
  | 'para' asignacion 'hasta' expresion 'haga' sentencias 'fin' 'para'
  ;

condicional : 'si' expresion 'entonces' sentencias (condicional_1)* 'fin' 'si'
   ;

condicional_1 : 'sino' sentencias;

asignacion : 'id' (asignacion_1)* TAN expresion
   ;

asignacion_1 : TPD ID
   | TOB (expresion)* TCB asignacion_2
   | ;

asignacion_2 : TPD ID
     | ;

esc_lec : 'escriba' expresion (TCM expresion)*
   | 'lea' ID (TPD ID)* (TCM ID)*
   ;

llamada : 'llamar' 'nueva_linea'
    | ID (TOP expresion TCP)*
    ;

casos : 'caso' ID asignacion_1 casos_op
   ;

casos_op : valor (TCM valor)*  TCN (sentencias)* ('sino' sentencias)* 'fin' 'caso';

valor : 'tkn_integer'
    | 'tkn_real'
    | 'tkn_char'
    | 'tkn_str'
    | 'verdadero'
    | 'falso'
    ;

expresion : 'Te' OP_E
    | 'tkn_opening_par' EXP 'tkn_closing_par' OP_E
    ;

OP_E : OP_A EXP
     | OP_L EXP
     | OP_R OP_EA OP_EL
     | ;

OP_EA : 'tkn_opening_par' 'Te' OP_AOP 'tkn_closing_par' OP_AOP
      | 'Te' OP_AOP
      ;

OP_AOP : OP_A OP_EA
       | ;

OP_EL : OP_L EXP
       | ;

Te : 'tkn_minus' Te
    | VAL
    | 'id' Te_id
    ;

Te_id : ARGS
       | AC
       ;


COMMENT       : '/*' .*? '*/' -> skip ;
LINE_COMMENT   : '//' ~[\r\n]* -> skip ;
WS    : [ \t\r\n]+ -> skip ;
MULOP  : ( '*' | '/' );
SUMOP  : ('+' | '-') ;
RL : [0-9]+( | [.][0-9]+);


EXP_C : 'tkn_opening_par' EXP_C 'tkn_closing_par' EXP_C_1
      | EXP OP_R EXP
      ;

EXP_C_1 : OP_L 'tkn_opening_par' EXP OP_R 'EXP' 'tkn_closing_par' EXP_C_1
        | ;

OP_R : ( '<' | '<=' | '>=' | '>' | '==' | '!=' ) ;

OP_L : 'o'
      | 'y'
      ;

EPSILON : ;
