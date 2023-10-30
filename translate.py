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

  # def enterAsignar(self, ctx:LPPParser.AsignarContext):
  #   # self.variables[ctx.getChild(0).getText()] = ctx.getChild(2).getText()
  #   for key, value in self.variables.items():
  #     if value == 'verdadero':
  #       self.variables[key] = 'True'
  #     elif value == 'falso':
  #       self.variables[key] = 'False'
  #
  #   # if ctx.getChild(2).getText() == 'verdadero':
  #   #   print(f"{ctx.getChild(0).getText()} = True")
  #   # elif ctx.getChild(2).getText() == 'falso':
  #   #   print(f"{ctx.getChild(0).getText()} = False")
  #   # else:
  #   #   print(f"{ctx.getChild(0).getText()} = {ctx.getChild(2).getText()}\n")
  #   # if ctx.getChild(2).getText() == 'verdadero':
  #   #   print(f"{ctx.getChild(0).getText()} = True")
  #   # elif ctx.getChild(2).getText() == 'falso':
  #   #   print(f"{ctx.getChild(0).getText()} = False")
  #   # else:
  #   #   print(f"{ctx.getChild(0).getText()} = {ctx.getChild(2).getText()}\n")
  #
  #   if ctx.getChild(0).getChildCount() > 1:
  #     if ctx.getChild(0).getChild(1).getText() == '[':
  #       param = ctx.getChild(0).getChild(2).getText()
  #       param = param.split(',')
  #       if len(param) == 1:
  #         if ctx.getChild(2).getText() == 'verdadero':
  #           self.variables[f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}]"] = "True"
  #           print(f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}] = True")
  #         elif ctx.getChild(2).getText() == 'falso':
  #           self.variables[f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}]"] = "False"
  #           print(f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}] = False")
  #         else:
  #           # print(f"ACA: {ctx.getChild(0).getChild(0).getText()}")
  #           self.variables[f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}]"] = ctx.getChild(2).getText()
  #           print(f"{ctx.getChild(0).getChild(0).getText()}[{param[0]}] = {ctx.getChild(2).getText()}\n")
  #         # print(f"{ctx.getChild(0).getText()}[{param[0]}] = {ctx.getChild(2).getText()}")
  #       else:
  #         param_new = ''
  #         key = f"{ctx.getChild(0).getChild(0).getText()}"
  #
  #         for i in range(0, len(param)):
  #             param_new += f"[{param[i]}]"
  #         if ctx.getChild(2).getText() == 'verdadero':
  #           self.variables[f"{key}{param_new}"] = "True"
  #           print(f"{ctx.getChild(0).getChild(0).getText()}{param_new} = True")
  #         elif ctx.getChild(2).getText() == 'falso':
  #           self.variables[f"{key}{param_new}"] = "False"
  #           print(f"{ctx.getChild(0).getChild(0).getText()}{param_new} = False")
  #         else:
  #           self.variables[f"{key}{param_new}"] = ctx.getChild(2).getText()
  #           print(f"{ctx.getChild(0).getChild(0).getText()}{param_new} = {ctx.getChild(2).getText()}\n")
  #         # print(f"{ctx.getChild(0).getChild(0).getText()}{param_new} = {ctx.getChild(2).getText()}")
  #
  #       # print(f"ACA> {ctx.getChild(0).getChild(2).getText()}")
  #     else:
  #       print(f"{ctx.getChild(0).getText()} = {ctx.getChild(2).getText()}\n")
  #   else:
  #     print(f"{ctx.getChild(0).getText()} = {ctx.getChild(2).getText()}\n")

  def enterAsignar(self, ctx:LPPParser.AsignarContext):
    lado_izq = self.enterExpr(ctx.getChild(0))
    # print('lado_izq', lado_izq)
    # print(f"IZQ {ctx.getChild(0).getText()}")

    # lado_izq = ctx.getChild(0).getText()
    lado_der = ctx.getChild(2).getText()
    return f"{lado_izq} = {lado_der}"

  def enterDeclaracionVariables(self, ctx:LPPParser.DeclaracionesVariablesContext):
    # print(f"len_arr {len_arr}")
    if self.enterTipo(ctx.getChild(0)) == "list":
      # print(ctx.getChild(0).getChild(2).getText())
      len_arr = ctx.getChild(0).getChild(2).getText()
      len_arr = len_arr.split(',')
      if len(len_arr) == 1:
        print(f"{ctx.getChild(1).getText()} = [0] * {len_arr[0]}\n")
      else:
        dim = '[0],'
        dimensiones = len_arr
        # for i in range(0, len(len_arr)):
        #   print(f"{ctx.getChild(1).getText()} = [{(i + 1) * dim}] * {len_arr[0]}\n")
        matriz = f"[[[0 for _ in range({dimensiones[-1]})] for _ in range({dimensiones[-2]})]]"
        print(f"{ctx.getChild(1).getText()} = {matriz}\n")

    elif self.enterTipo(ctx.getChild(0)) == "ID":
      print(f"{ctx.getChild(1).getText()} = {ctx.getChild(0).getText()}()\n")


  def enterDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
    print(f"class {ctx.getChild(1).getText()}:")
    print(f"\tdef __init__(self):")
    num_children = ctx.getChild(3).getChildCount()
    for i in range(0, num_children-1):
      self.remove_lastChild(ctx.getChild(3).getChild(i))
      if self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "list":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = []")
      elif self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "str":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = ''")
      elif self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "int":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = 0")
      elif self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "float":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = 0.0")
      elif self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "bool":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = False")
      elif self.enterTipo(ctx.getChild(3).getChild(i).getChild(0)) == "char":
        print(f"\t\tself.{ctx.getChild(3).getChild(i).getChild(1).getText()} = ''")
    print('\n')

  def enterParametro(self, ctx:LPPParser.ParametroContext):
    # print(f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()}")
    return ctx.getChild(1).getText()

  def enterDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
    params = []

    for i in range(0, ctx.getChild(3).getChildCount()):
      if i % 2 == 0:
        params.append(f"{self.enterParametro(ctx.getChild(3).getChild(i))}")
    params = ', '.join(params)
    print(f"def {ctx.getChild(1).getText()}({params}):")
    expr = self.enterSentencia(ctx.getChild(9).getChild(2).getChild(0))
    # print(f"\t{expr}")
    print(f"\t return {expr}")
    print('\n')

  def enterRetorne(self, ctx:LPPParser.RetorneContext):
    expr = self.enterExpr(ctx.getChild(1))
    # print(f"return {expr}")
    return expr

  # def enterSentenciasPrograma(self, ctx:LPPParser.SentenciasProgramaContext):
  #   if ctx.sentencias() is not None:
  #     print('SP', self.enterSentencias(ctx.getChild(2)))
  #     return self.enterSentencias(ctx.getChild(2))
  # def enterSentencias(self, ctx:LPPParser.SentenciasContext):
  #   if ctx.sentencia() is not None:
  #     # print('SS', self.enterSentencia(ctx.getChild(0)))
  #     return self.enterSentencia(ctx.getChild(0))
  #   # for i in range(0, ctx.getChildCount()):
  #   #   self.enterSentencia(ctx.getChild(i))
  def enterSentencia(self, ctx:LPPParser.SentenciaContext):
    if ctx.escriba() is not None:
      print(self.enterEscriba(ctx.getChild(0)))
      # return (self.enterEscriba(ctx.getChild(0)))
    elif ctx.lea() is not None:
      return (self.enterLea(ctx.getChild(0)))
    elif ctx.asignar() is not None:
      print(self.enterAsignar(ctx.getChild(0)))
    elif ctx.llamar() is not None:
      return (self.enterLlamar(ctx.getChild(0)))
    elif ctx.si() is not None:
      return (self.enterSi(ctx.getChild(0)))
    elif ctx.caso() is not None:
      return (self.enterCaso(ctx.getChild(0)))
    elif ctx.mientras() is not None:
      return (self.enterMientras(ctx.getChild(0)))
    elif ctx.para() is not None:
      return (self.enterPara(ctx.getChild(0)))
    elif ctx.repita() is not None:
      return (self.enterRepita(ctx.getChild(0)))
    elif ctx.retorne() is not None:
      return (self.enterRetorne(ctx.getChild(0)))
    # if ctx.getChild(0).getChild(0).getText() == "retorne":
    #   return self.enterRetorne(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "si":
    #   return self.enterSi(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "mientras":
    #   return self.enterMientras(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "para":
    #   return self.enterPara(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "imprimir":
    #   return self.enterImprimir(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "leer":
    #   return self.enterLeer(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "asignar":
    #   return self.enterAsignar(ctx.getChild(0))
    # elif ctx.getChild(0).getChild(0).getText() == "llamar":
    #   return self.enterLlamar(ctx.getChild(0))

  def enterExpr(self, ctx:LPPParser.ExprContext):

    # print('ctx', ctx.)

    if ctx.ID() is not None:
      # print('ID', ctx.getText(), ctx.ID().getText())
      return ctx.getText()
    elif ctx.DESIGUAL() is not None:
      return f"{ctx.getChild(0).getText()} != {ctx.getChild(2).getText()}"
    elif ctx.DIV() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MULT() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.SUMA() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.RESTA() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MAYOR() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MENOR() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MAYOR_IGUAL() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.MENOR_IGUAL() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
    elif ctx.IGUAL() is not None:
      return f"{ctx.getChild(0).getText()} {ctx.getChild(1).getText()} {ctx.getChild(2).getText()}"
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
    if ctx.listaExpr() is not None:
      expresiones = self.enterListaExpr(ctx.getChild(1))
      exp_to_print = ''
      for i, expr in enumerate(expresiones):
        if i == len(expresiones) - 1:
          exp_to_print += f"{expr}"
        else:
          exp_to_print += f"{expr}, "
      return f"print({exp_to_print})"
    # if ctx.ESCRIBA() is not None:
    #   len_parm = ctx.getChild(1).getChildCount()
    #   parm = ''
    #   for i in range(0, len_parm):
    #     if i % 2 == 0:
    #       parm += f"{self.convert_vars(ctx.getChild(1).getChild(i).getText())}"
    #
    #   return f"print({parm})"
      # print(f"print({self.convert_vars(ctx.getChild(1).getText())})")
    # len_parm = ctx.getChild(1).getChildCount()
    # parm = ''
    # for i in range(0, len_parm):
    #   # if i % 2 == 0:
    #   parm += f"{self.convert_vars(ctx.getChild(1).getChild(i).getText())}"
    #
    # print(f"print({parm})")
    # # print(f"print({self.convert_vars(ctx.getChild(1).getText())})")

  def enterListaExpr(self, ctx:LPPParser.ListaExprContext):
    expressions = ctx.expr()
    # expressions = ctx.expr()
    # print('len_exp', len(expressions))
    list_expr = []
    for expr in expressions:
      # print('expressions', expr.getText())
      list_expr.append(self.enterExpr(expr))
    return list_expr
  def enterLlamar(self, ctx:LPPParser.LlamarContext):
    if ctx.NL() is not None:
      return
    elif ctx.ID() is not None:
      print(f"{ctx.getChild(0).getText()}({ctx.getChild(2).getText()})")

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
    if ctx.SI() is not None:
      print(f"if {self.enterExpr(ctx.getChild(1))}:")
      print(f"\t{self.enterSentencias(ctx.getChild(4))}")
      if ctx.getChildCount() == 9:
        print(f"else:")
        self.enterSentencia(ctx.getChild(5))
      elif ctx.getChildCount() > 9:
        print(f"else if {self.enterExpr(ctx.getChild(7))}:")
        self.enterSentencia(ctx.getChild(8))
        print(f"else:")
        self.enterSentencia(ctx.getChild(9))



