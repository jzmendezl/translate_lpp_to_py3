from LPPListener import LPPListener
from LPPParser import LPPParser
import re

class Translate(LPPListener):
  def __init__(self):
    self.variables = {}

  def remove_lastChild(self, ctx):
    return ctx.removeLastChild()
  def convert_vars(self, string):
    # list_str = re.findall(r'([\w+][\w+]*)\[(\d+(?:,\d+)*)\]', string)
    # print('list_str', list_str)
    #
    # if len(list_str) == 1:
    #   return string
    # else:
    # for i in range(0, len(list_str)):
    len_arr = re.findall(r'\[([^\]]*)\]', string)
    # len_arr = re.findall(r'\[([^\]]*)\]', list_str[i])
    # print('len_arr', len_arr)
    if len(len_arr) == 0:
      return string
    else:
      parm = len_arr[0].split(',')
      # print('parm', parm)
      parm = [int(i) for i in parm]
      output = ''
      for e in parm:
        output += f'[{e}]'

      string = re.sub(r'\[([^\]]*)\]', output, string)
      return string
  def crear_matriz(self, *dimensiones):
    if len(dimensiones) < 2:
      raise ValueError("La matriz debe tener al menos dos dimensiones.")

    matriz = [[[0 for _ in range(dimensiones[-1])] for _ in range(dimensiones[-2])]]

    for dim in reversed(dimensiones[:-2]):
      matriz = [[[matriz[i] for _ in range(dim)] for i in range(len(matriz))] for _ in range(dimensiones[-1])]

    return matriz

  def enterPrograma(self, ctx:LPPParser.ProgramaContext):
    print(f"import sys")
    print(f"import math")
    print(f"import random")
    print(f"import numpy as np")
    print(f"\n\n")
    if ctx.declaracionesTipos() is not None:
      if ctx.declaracionesTipos().getChildCount() > 0:
        self.enterDeclaracionesTipos(ctx.getChild(0))
    if ctx.declaracionesVariables() is not None:
      if ctx.declaracionesVariables().getChildCount() > 0:
        self.enterDeclaracionesVariables(ctx.getChild(1))
    if ctx.declaracionesSubprogramas() is not None:
      if ctx.declaracionesSubprogramas().getChildCount() > 0:
        self.enterDeclaracionesSubprogramas(ctx.getChild(2))
    if ctx.sentenciasPrograma() is not None:
      if ctx.sentenciasPrograma().getChildCount() > 0:
        self.enterSentenciasPrograma(ctx.getChild(3))

  def enterDeclaracionesTipos(self, ctx:LPPParser.DeclaracionesTiposContext):
    if ctx.getText() != '':
      if ctx.declaracionRegistro() is not None:
        if ctx.declaracionRegistro().getChildCount() > 0:
          self.enterDeclaracionRegistro(ctx.getChild(0))
      if ctx.declaracionTipo() is not None:
        if ctx.declaracionTipo().getChildCount() > 0:
          self.enterDeclaracionTipo(ctx.getChild(1))

  def enterDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
    to_print = ''
    to_print += f"class {ctx.getChild(1).getText()}:"
    to_print += f"\n\tdef __init__(self):"
    num_children = ctx.getChild(2).getChildCount()
    for i in range(0, num_children-1):
      if self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "list":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = []"
      elif self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "str":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = ''"
      elif self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "int":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = 0"
      elif self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "float":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = 0.0"
      elif self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "bool":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = False"
      elif self.enterTipo(ctx.getChild(2).getChild(i).getChild(0)) == "char":
        to_print += f"\n\t\tself.{ctx.getChild(2).getChild(i).getChild(1).getText()} = ''"
    # to_print += f"\n\n"
    print(to_print)

  def enterDeclaracionesVariables(self, ctx:LPPParser.DeclaracionesVariablesContext):
    # print('DV', ctx.getText())
    if ctx.declaracionVariables() is not None:
      for child in ctx.getChildren():
        self.enterDeclaracionVariables(child)
  def enterDeclaracionVariables(self, ctx: LPPParser.DeclaracionesVariablesContext):
    if ctx.getChild(0).getText().lower() == 'entero':
      len_entero = self.enterListaIDs(ctx.getChild(1))
      if len(len_entero) == 1:
        print(f"{ctx.getChild(1).getText()} = 0")
      else:
        for i in len_entero:
          print(f"{i} = 0")
    elif ctx.getChild(0).getText().lower() == 'real':
      len_real = self.enterListaIDs(ctx.getChild(1))
      if len(len_real) == 1:
        print(f"{ctx.getChild(1).getText()} = 0.0")
      else:
        for i in len_real:
          print(f"{i} = 0.0")
    elif ctx.getChild(0).getText().lower() == 'caracter':
      print(f"{ctx.getChild(1).getText()} = ''")
    elif ctx.getChild(0).getText().lower() == 'cadena':
      print(f"{ctx.getChild(1).getText()} = ''")
    elif ctx.getChild(0).getText().lower() == 'booleano':
      print(f"{ctx.getChild(1).getText()} = bool()")
    elif ctx.getChild(0).getText().lower() == 'arreglo':
      len_arr = ctx.getChild(0).getChild(2).getText()
      list_len_arr = len_arr.split(',')
      if len(list_len_arr) == 1:
        print(f"{ctx.getChild(1).getText()} = np.empty({list_len_arr[0]})")
      else:
        print(f"{ctx.getChild(1).getText()} = np.empty(({len_arr}))")
    elif ctx.getChild(0).getText() == 'ID':
      print(f"{ctx.getChild(1).getText()} = {ctx.getChild(0).getText()}()")

  def enterListaIDs(self, ctx: LPPParser.ListaIDsContext):
    len_ID = ctx.getText().split(',')
    return len_ID

  def enterDeclaracionesSubprogramas(self, ctx:LPPParser.DeclaracionesSubprogramasContext):
    if ctx.getText() != '':
      if ctx.declaracionFuncion() is not None:
        if ctx.declaracionFuncion().getChildCount() > 0:
          self.enterDeclaracionFuncion(ctx.getChild(0))
      if ctx.declaracionProcedimiento() is not None:
        if ctx.declaracionProcedimiento().getChildCount() > 0:
          self.enterDeclaracionProcedimiento(ctx.getChild(1))

  def enterDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
    params = []
    name_fun = ''
    if ctx.parametros() is not None:
      name_fun += f"{ctx.getChild(1).getText()}"
      for i in range(0, ctx.getChild(3).getChildCount()):
        if i % 2 == 0:
          params.append(f"{self.enterParametro(ctx.getChild(3).getChild(i))}")
      params = ', '.join(params)
      print(f"def {name_fun}({params}):")

      if ctx.declaracionesVariables() is not None and ctx.declaracionesVariables().getChildCount() > 0:
        self.enterDeclaracionesVariables(ctx.getChild(7))
      if ctx.sentenciasSubprograma() is not None:
        self.enterSentenciasSubprograma(ctx.getChild(8))

    else:
      name_fun += f"{ctx.getChild(1).getText()}"
      print(f"def {name_fun}():")
      if ctx.declaracionesVariables() is not None and ctx.declaracionesVariables().getChildCount() > 0:
        self.enterDeclaracionesVariables(ctx.getChild(4))
      if ctx.sentenciasSubprograma() is not None:
        self.enterSentenciasSubprograma(ctx.getChild(5))

  def enterSentenciasSubprograma(self, ctx:LPPParser.SentenciasSubprogramaContext):
    # print('SSP', ctx.getText())
    if ctx.sentencias() is not None:
      self.enterSentencias(ctx.getChild(1))

  def enterSentencias(self, ctx:LPPParser.SentenciasContext):
    if ctx.sentencia() is not None:
      for child in ctx.getChildren():
        self.enterSentencia(child)


  def enterSentencia(self, ctx:LPPParser.SentenciaContext):
    # print('SENTENCIA', ctx.getText())
    if ctx.escriba() is not None:
      self.enterEscriba(ctx.getChild(0))
      # return (self.enterEscriba(ctx.getChild(0)))
    elif ctx.lea() is not None:
      self.enterLea(ctx.getChild(0))
    elif ctx.asignar() is not None:
      self.enterAsignar(ctx.getChild(0))
    elif ctx.llamar() is not None:
      self.enterLlamar(ctx.getChild(0))
    elif ctx.si() is not None:
      self.enterSi(ctx.getChild(0))
    elif ctx.caso() is not None:
      self.enterCaso(ctx.getChild(0))
    elif ctx.mientras() is not None:
      self.enterMientras(ctx.getChild(0))
    elif ctx.para() is not None:
      self.enterPara(ctx.getChild(0))
    elif ctx.repita() is not None:
      self.enterRepita(ctx.getChild(0))
    elif ctx.retorne() is not None:
      return self.enterRetorne(ctx.getChild(0))


  def enterTipo(self, ctx:LPPParser.TipoContext):
    if ctx.ENTERO() != None:
      return 'int'
    elif ctx.REAL() != None:
      return 'float'
    elif ctx.CARACTER() != None:
      return 'char'
    elif ctx.CADENA() != None:
      return 'str'
    elif ctx.BOOLEANO() != None:
      return 'bool'
    elif ctx.ARREGLO() != None:
      return 'list'
    elif ctx.ID() != None:
      self.variables[ctx.ID().getText()] = ctx.ID().getText()
      return 'ID'


  def enterAsignar(self, ctx:LPPParser.AsignarContext):
    lado_izq = self.enterExpr(ctx.getChild(0))
    lado_der = ctx.getChild(2).getText()
    print(f"{lado_izq} = {lado_der}")


  def enterParametro(self, ctx:LPPParser.ParametroContext):
    return ctx.getChild(1).getText()

  def enterRetorne(self, ctx:LPPParser.RetorneContext):
    print(f"return {self.enterExpr(ctx.getChild(1))} \n\n")

  def enterExpr(self, ctx:LPPParser.ExprContext):
    if ctx.ID() is not None:
      # print('ID', ctx.getText(), ctx.ID().getText())
      return ctx.getText()
    elif ctx.DESIGUAL() is not None:
      return f"{ctx.getChild(0).getText()} != {ctx.getChild(2).getText()}"
    # elif ctx.DIV() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.MULT() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.SUMA() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.RESTA() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.MAYOR() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.MENOR() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.MAYOR_IGUAL() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.MENOR_IGUAL() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    # elif ctx.IGUAL() is not None:
    #   return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.DIV_ENTEROS() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MOD() is not None:
      return f"{ctx.getChild(0).getText()} % {ctx.getChild(2).getText()}"
    elif ctx.PODER() is not None:
      return f"{ctx.getChild(0).getText()} ** {ctx.getChild(2).getText()}"
    elif ctx.literal() is not None:
      # print('es literal', self.enterLiteral(ctx.literal()))
      return self.enterLiteral(ctx.literal())
    else:
      return ctx.getChild(0).getText()

  def enterEscriba(self, ctx:LPPParser.EscribaContext):
    # print('ESCRIBA', ctx.getText())
    if ctx.listaExpr() is not None:
      expresiones = self.enterListaExpr(ctx.getChild(1))
      # print('expresiones', expresiones)
      exp_to_print = ''
      for i, expr in enumerate(expresiones):
        if i == len(expresiones) - 1:
          exp_to_print += f"{expr}"
        else:
          exp_to_print += f"{expr}, "
      # print('exp_to_print', exp_to_print)
      print(f"print({exp_to_print})")

  def enterListaExpr(self, ctx:LPPParser.ListaExprContext):
    expressions = ctx.expr()
    list_expr = []
    for expr in expressions:
      list_expr.append(self.enterExpr(expr))
    return list_expr
  def enterLlamar(self, ctx:LPPParser.LlamarContext):
    if ctx.procedimientoLibreriaEstandar() is not None:
      self.enterProcedimientoLibreriaEstandar(ctx.getChild(1))
    elif ctx.ID() is not None:
      if ctx.getChildCount() > 2:
        lst_expr = self.enterListaExpr(ctx.getChild(3))
        print(f"{ctx.getChild(1).getText()}({lst_expr})")
      else:
        print(f"{ctx.getChild(1).getText()}()")

  def enterProcedimientoLibreriaEstandar(self, ctx:LPPParser.ProcedimientoLibreriaEstandarContext):
    if ctx.PROC_NUEVA_LINEA() is not None:
      print(f"print()")


  def enterLiteral(self, ctx:LPPParser.LiteralContext):
    if ctx.LITERAL_CADENA() is not None:
      # print('es cadena', ctx.LITERAL_CADENA().getText())
      return ctx.LITERAL_CADENA().getText()
    elif ctx.LITERAL_ENTERO() is not None:
#       print('es entero', ctx.LITERAL_ENTERO().getText())
      return ctx.LITERAL_ENTERO().getText()
    elif ctx.LITERAL_REAL() is not None:
#       print('es real', ctx.LITERAL_REAL().getText())
      return ctx.LITERAL_REAL().getText()
    elif ctx.LITERAL_CARACTER() is not None:
#       print('es caracter', ctx.LITERAL_CARACTER().getText())
      return ctx.LITERAL_CARACTER().getText()
    elif ctx.VERDADERO() is not None:
      # print('es verdadero', ctx.VERDADERO().getText())
      return 'True'
    elif ctx.FALSO() is not None:
      # print('es falso', ctx.FALSO().getText())
      return 'False'

  def enterLea(self, ctx:LPPParser.LeaContext):
    if ctx.LEA() is not None:
      for child in ctx.getChild(1).getChildren():
        if child.getText() != 'lea' and child.getText() != ',':
          print(f"{child.getText()} = input()")

  def enterSi(self, ctx:LPPParser.SiContext):
    print(f"{ctx.getChildCount()}")
    to_print = ''
    snt_if = ''
    snt_else = ''
    snt_elif = ''

    if ctx.SI() is not None:
      print(f"if {self.enterExpr(ctx.getChild(1))}:")
      # print(f"\t{self.enterSentencias(ctx.getChild(3))}")
      snt_if += self.enterExpr(ctx.getChild(1))
      to_print += f"if {snt_if}:"

    elif ctx.sino() is not None:
      snt_else += self.enterSino(ctx.getChild(4))
      to_print += f"{snt_else}"

    return to_print

  def enterSino(self, ctx:LPPParser.SinoContext):
    snt_sino = ''
    exp_sino_si = ''
    snt_sino_si = ''
    if ctx.SINO() is not None:
      snt_sino += self.enterSentencias(ctx.getChild(1))
      return f"else:\n\t{snt_sino}"
    if ctx.si() is not None:
      exp_sino_si += self.enterExpr(ctx.getChild(1))
      snt_sino_si += self.enterSentencias(ctx.getChild(3))
      return f"elif {exp_sino_si}:\n\t{snt_sino_si}"
    
  def enterMientras(self, ctx:LPPParser.MientrasContext):
    if ctx.MIENTRAS() is not None:
      print(f"while {self.enterExpr(ctx.getChild(1))}:")
      self.enterSentencia(ctx.getChild(4))

  def enterPara(self, ctx:LPPParser.ParaContext):
    if ctx.PARA() is not None:
      print(f"for {self.enterExpr(ctx.getChild(1))} in range({self.enterExpr(ctx.getChild(3))}, {self.enterExpr(ctx.getChild(5))}):")
      self.enterSentencias(ctx.getChild(7))

  def enterRepita(self, ctx:LPPParser.RepitaContext):
    if ctx.REPITA() is not None:
      print(f"while True:")
      self.enterSentencia(ctx.getChild(1))
      print(f"if {self.enterExpr(ctx.getChild(4))}:")
      print(f"\tbreak")
      print(f"else:")
      self.enterSentencia(ctx.getChild(7))