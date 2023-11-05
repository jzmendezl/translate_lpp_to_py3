from LPPListener import LPPListener
from LPPParser import LPPParser
import re

class Translate(LPPListener):
  file = open("output.py", "w")
  prog = ""
  indent = 0
  variables = dict()
  opr = {
    "^": " ** ",
    "div": " // ",
    "mod": " % ",
    "=": " == ",
    "<>": " != ",
    "y": " and ",
    "o": " or ",
    "no": " not ",
    "<-": " = ",
  }
  types = {
    "entero": "int",
    "real": "float",
    "booleano": "bool",
    "cadena": "str",
    "caracter": "str",
  }
  exp = []
  in_asignar = False
  in_para = False
  flag_hasta = False
  flag_arr = False
  size_arr = ""
  type_arr = ""
  flag_reg = False
  flag_repita = False
  size_cad = 0


  def indentation(self):
    return self.indent*"\t"

  def enterPrograma(self, ctx:LPPParser.ProgramaContext):
    self.prog += "import sys\n"
    self.prog += "import numpy as np\n"
    self.prog += "\n"
    self.prog += "def main():\n"
    self.indent += 1

  def exitPrograma(self, ctx:LPPParser.ProgramaContext):
    self.prog += "\n\n"
    self.indent = 0
    self.prog += "if __name__ == \"__main__\":\n"
    self.indent += 1
    self.prog += self.indentation() + "main()\n"
    print(self.prog)

  def enterDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
    self.prog += self.indentation() + "class " + ctx.ID().getText() + ":\n"
    self.indent += 1
    self.prog += self.indentation() + "def __init__(self):\n"
    self.indent += 1
    self.flag_reg = True

  def exitDeclaracionRegistro(self, ctx: LPPParser.DeclaracionRegistroContext):
    self.indent -= 1
    self.indent -= 1
    self.prog += "\n\n"
    self.flag_reg = False

  def enterTipo(self, ctx:LPPParser.TipoContext):
    if ctx.getChild(0).getText().lower() == "arreglo":
      self.flag_arr = True
      self.size_arr += ctx.getChild(2).getText().lower() + ","
      self.type_arr = ctx.getChild(5).getText().lower()

  def enterDeclaracionVariables(self, ctx:LPPParser.DeclaracionVariablesContext):
    if ctx.tipo().getChild(0).getText().lower() == "entero":
      if self.flag_reg:
        len_int = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_int)):
          self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower().split(',')[i] + " = 0\n"
      else:
        len_int = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_int)):
          self.prog += self.indentation() + ctx.listaIDs().getText().lower().split(',')[i] + " = 0\n"
    elif ctx.tipo().getChild(0).getText().lower() == "real":
      if self.flag_reg:
        len_real = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_real)):
          self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower().split(',')[i] + " = 0.0\n"
      else:
        len_real = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_real)):
          self.prog += self.indentation() + ctx.listaIDs().getText().lower().split(',')[i] + " = 0.0\n"
    elif ctx.tipo().getChild(0).getText().lower() == "booleano":
      if self.flag_reg:
        len_bool = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_bool)):
          self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower().split(',')[i] + " = False\n"
      else:
        len_bool = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_bool)):
          self.prog += self.indentation() + ctx.listaIDs().getText().lower().split(',')[i] + " = False\n"
    elif ctx.tipo().getChild(0).getText().lower() == "cadena":
      if self.flag_reg:
        len_cad = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_cad)):
          self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower().split(',')[i] + " = \"\"\n"
      else:
        len_cad = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_cad)):
          self.prog += self.indentation() + ctx.listaIDs().getText().lower().split(',')[i] + " = \"\"\n"
    elif ctx.tipo().getChild(0).getText().lower() == "caracter":
      if self.flag_reg:
        len_car = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_car)):
          self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower().split(',')[i] + " = \"\"\n"
      else:
        len_car = ctx.listaIDs().getText().split(',')
        for i in range(0, len(len_car)):
          self.prog += self.indentation() + ctx.listaIDs().getText().lower().split(',')[i] + " = \"\"\n"
    elif ctx.tipo().getChild(0).getText().lower() == "arreglo":
      self.flag_arr = True
    else:
      if self.flag_reg:
        self.prog += self.indentation() + 'self.' + ctx.listaIDs().getText().lower() + f" = {ctx.getChild(0).getText().lower()}()\n"
      else:
        self.prog += self.indentation() + ctx.listaIDs().getText().lower() + f" = {ctx.getChild(0).getText().lower()}()\n"


  def exitDeclaracionVariables(self, ctx:LPPParser.DeclaracionVariablesContext):
    if ctx.tipo().getChild(0).getText().lower() == "arreglo":
      self.flag_arr = False
      if self.flag_arr:
        pass
      else:
        self.prog += self.indentation() + f"{ctx.getChild(1).getText().lower()} = np.empty(({self.size_arr}), dtype={self.types.get(self.type_arr)})\n"
        self.size_arr = ""
        self.type_arr = ""


  def enterDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
    self.prog += "\n"
    self.prog += self.indentation() + "def " + ctx.ID().getText().lower()
    self.indent += 1
    if ctx.parametros() is None:
      self.prog += "():\n"

  def exitDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
    self.prog += "\n\n"

  def enterParametros(self, ctx:LPPParser.ParametrosContext):
    if ctx.parametro() != None:
      self.prog += "("

  def exitParametros(self, ctx:LPPParser.ParametrosContext):
    if ctx.parametro() != None:
      self.prog += "):\n"
    else:
      self.prog += "):\n"

  def enterParametro(self, ctx:LPPParser.ParametroContext):
    if ctx.ID() != None:
      self.prog += ctx.ID().getText().lower()

  def enterRetorne(self, ctx:LPPParser.RetorneContext):
    self.prog += self.indentation() + "return "

  def exitRetorne(self, ctx:LPPParser.RetorneContext):
    self.prog += "\n"
    self.indent -= 1

  def enterExpr(self, ctx:LPPParser.ExprContext):
    if ctx.getChildCount() == 1:
      if ctx.getText().lower() == 'verdadero':
        self.prog += 'True'
      elif ctx.getText().lower() == 'falso':
        self.prog += 'False'
      elif ctx.literal() != None:
        self.prog += ctx.literal().getText()
      else:
        self.prog += ctx.getText().lower()
    elif ctx.literal() != None:
      self.prog += ctx.literal().getText()
    elif ctx.ID() != None:
      self.prog += ctx.ID().getText().lower()
    elif ctx.RESTA() != None:
      self.prog += ctx.RESTA().getText()


  def exitExpr(self, ctx:LPPParser.ExprContext):
    if self.in_para:
      self.prog += " in range("
      self.in_para = False

  def enterOpenPar(self, ctx:LPPParser.OpenParContext):
    self.prog += "("

  def exitClosePar(self, ctx:LPPParser.CloseParContext):
    self.prog += ")"

  def enterExponente(self, ctx:LPPParser.ExponenteContext):
    symbol = ctx.getText()
    if symbol in self.opr:
      symbol = self.opr.get(symbol)
    self.prog += " " + symbol + " "

  def enterSymbolAssing(self, ctx:LPPParser.SymbolAssingContext):
    self.prog += ' = '

  def enterAsignar(self, ctx:LPPParser.AsignarContext):
    self.prog += self.indentation()

  def exitAsignar(self, ctx:LPPParser.AsignarContext):
    self.prog += "\n"

  def enterPunto(self, ctx:LPPParser.PuntoContext):
    self.prog += ctx.getText()

  def enterEscriba(self, ctx:LPPParser.EscribaContext):
    self.prog += self.indentation() + "print("

  def exitEscriba(self, ctx:LPPParser.EscribaContext):
    self.prog += ", end=\"\", sep=\"\")\n"

  def enterLlamar(self, ctx:LPPParser.LlamarContext):
    if ctx.procedimientoLibreriaEstandar() is not None:
      self.prog += self.indentation() + "print()\n"
    elif ctx.ID() is not None:
      if ctx.getChildCount() > 2:
        self.prog += self.indentation() + f"{ctx.getChild(1).getText().lower()}("
      else:
        self.prog += self.indentation() + f"{ctx.getChild(1).getText().lower()}()"

  def exitLlamar(self, ctx:LPPParser.LlamarContext):
    if ctx.ID() is not None:
      if ctx.getChildCount() > 2:
        self.prog += ")\n"
    self.prog += "\n"

  def enterComa(self, ctx:LPPParser.ComaContext):
    if self.in_asignar:
      self.prog += "]["
    else:
      self.prog += ","

  def enterOpenBra(self, ctx:LPPParser.OpenBraContext):
    self.prog += "["
    self.in_asignar = True

  def exitCloseBra(self, ctx:LPPParser.CloseBraContext):
    self.prog += "]"
    self.in_asignar = False

  def enterLea(self, ctx:LPPParser.LeaContext):
    self.prog += self.indentation()

  def exitLea(self, ctx:LPPParser.LeaContext):
    self.prog += " = input().split()\n"

  def enterSi(self, ctx:LPPParser.SiContext):
    self.prog += self.indentation() + "if "

  def enterSino(self, ctx:LPPParser.SinoContext):
    self.indent -= 1
    self.prog += self.indentation() + "else:\n"
    self.indent += 1

  def exitSino(self, ctx:LPPParser.SinoContext):
    self.indent -= 1

  def enterEntonces(self, ctx:LPPParser.EntoncesContext):
    self.prog += ":\n"
    self.indent += 1

  def enterPara(self, ctx:LPPParser.ParaContext):
    self.prog += self.indentation() + "for "
    self.indent += 1
    self.in_para = True
    self.flag_hasta = True

  def exitPara(self, ctx:LPPParser.ParaContext):
    self.indent -= 2
    self.flag_hasta = False

  def enterHasta(self, ctx:LPPParser.HastaContext):
    if self.flag_repita:
      self.prog += self.indentation() + "if ("
    else:
      self.prog += ", "

  def exitHasta(self, ctx:LPPParser.HastaContext):
    if self.flag_repita:
      self.prog += "):\n"
      self.indent += 1
      self.prog += self.indentation() + "break\n"
    else:
      if ctx.expr() is not None:
        self.prog += " + 1):\n"
        self.indent += 1

  def enterDeclaracionProcedimiento(self, ctx:LPPParser.DeclaracionProcedimientoContext):
    self.prog += "\n"
    self.prog += self.indentation() + "def " + ctx.ID().getText().lower()
    self.indent += 1
    if ctx.parametros() is None:
      self.prog += "():\n"

  def exitDeclaracionProcedimiento(self, ctx:LPPParser.DeclaracionProcedimientoContext):
    self.indent -= 1
    self.prog += "\n\n"

  def enterMientras(self, ctx:LPPParser.MientrasContext):
    self.prog += self.indentation() + "while "

  def exitMientras(self, ctx:LPPParser.MientrasContext):
    self.indent -= 1

  def enterHaga(self, ctx:LPPParser.HagaContext):
    self.prog += ":\n"
    self.indent += 1


  def enterRepita(self, ctx:LPPParser.RepitaContext):
    self.prog += self.indentation() + "while True:\n"
    self.indent += 1
    self.flag_repita = True

  def exitRepita(self, ctx:LPPParser.RepitaContext):
    self.indent -= 1
    self.flag_repita = False











