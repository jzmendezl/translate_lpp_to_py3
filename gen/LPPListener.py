# Generated from C:/Users/Kira/PycharmProjects/pythonProject/grammar/LPP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LPPParser import LPPParser
else:
    from LPPParser import LPPParser

# This class defines a complete listener for a parse tree produced by LPPParser.
class LPPListener(ParseTreeListener):

    # Enter a parse tree produced by LPPParser#programa.
    def enterPrograma(self, ctx:LPPParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LPPParser#programa.
    def exitPrograma(self, ctx:LPPParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionesTipos.
    def enterDeclaracionesTipos(self, ctx:LPPParser.DeclaracionesTiposContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionesTipos.
    def exitDeclaracionesTipos(self, ctx:LPPParser.DeclaracionesTiposContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionRegistro.
    def enterDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionRegistro.
    def exitDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionTipo.
    def enterDeclaracionTipo(self, ctx:LPPParser.DeclaracionTipoContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionTipo.
    def exitDeclaracionTipo(self, ctx:LPPParser.DeclaracionTipoContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionesSubprogramas.
    def enterDeclaracionesSubprogramas(self, ctx:LPPParser.DeclaracionesSubprogramasContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionesSubprogramas.
    def exitDeclaracionesSubprogramas(self, ctx:LPPParser.DeclaracionesSubprogramasContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionProcedimiento.
    def enterDeclaracionProcedimiento(self, ctx:LPPParser.DeclaracionProcedimientoContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionProcedimiento.
    def exitDeclaracionProcedimiento(self, ctx:LPPParser.DeclaracionProcedimientoContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionFuncion.
    def enterDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionFuncion.
    def exitDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
        pass


    # Enter a parse tree produced by LPPParser#parametros.
    def enterParametros(self, ctx:LPPParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LPPParser#parametros.
    def exitParametros(self, ctx:LPPParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LPPParser#parametro.
    def enterParametro(self, ctx:LPPParser.ParametroContext):
        pass

    # Exit a parse tree produced by LPPParser#parametro.
    def exitParametro(self, ctx:LPPParser.ParametroContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionesVariables.
    def enterDeclaracionesVariables(self, ctx:LPPParser.DeclaracionesVariablesContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionesVariables.
    def exitDeclaracionesVariables(self, ctx:LPPParser.DeclaracionesVariablesContext):
        pass


    # Enter a parse tree produced by LPPParser#declaracionVariables.
    def enterDeclaracionVariables(self, ctx:LPPParser.DeclaracionVariablesContext):
        pass

    # Exit a parse tree produced by LPPParser#declaracionVariables.
    def exitDeclaracionVariables(self, ctx:LPPParser.DeclaracionVariablesContext):
        pass


    # Enter a parse tree produced by LPPParser#tipo.
    def enterTipo(self, ctx:LPPParser.TipoContext):
        pass

    # Exit a parse tree produced by LPPParser#tipo.
    def exitTipo(self, ctx:LPPParser.TipoContext):
        pass


    # Enter a parse tree produced by LPPParser#listaIDs.
    def enterListaIDs(self, ctx:LPPParser.ListaIDsContext):
        pass

    # Exit a parse tree produced by LPPParser#listaIDs.
    def exitListaIDs(self, ctx:LPPParser.ListaIDsContext):
        pass


    # Enter a parse tree produced by LPPParser#listaEnteros.
    def enterListaEnteros(self, ctx:LPPParser.ListaEnterosContext):
        pass

    # Exit a parse tree produced by LPPParser#listaEnteros.
    def exitListaEnteros(self, ctx:LPPParser.ListaEnterosContext):
        pass


    # Enter a parse tree produced by LPPParser#sentenciasSubprograma.
    def enterSentenciasSubprograma(self, ctx:LPPParser.SentenciasSubprogramaContext):
        pass

    # Exit a parse tree produced by LPPParser#sentenciasSubprograma.
    def exitSentenciasSubprograma(self, ctx:LPPParser.SentenciasSubprogramaContext):
        pass


    # Enter a parse tree produced by LPPParser#sentenciasPrograma.
    def enterSentenciasPrograma(self, ctx:LPPParser.SentenciasProgramaContext):
        pass

    # Exit a parse tree produced by LPPParser#sentenciasPrograma.
    def exitSentenciasPrograma(self, ctx:LPPParser.SentenciasProgramaContext):
        pass


    # Enter a parse tree produced by LPPParser#sentencias.
    def enterSentencias(self, ctx:LPPParser.SentenciasContext):
        pass

    # Exit a parse tree produced by LPPParser#sentencias.
    def exitSentencias(self, ctx:LPPParser.SentenciasContext):
        pass


    # Enter a parse tree produced by LPPParser#sentencia.
    def enterSentencia(self, ctx:LPPParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LPPParser#sentencia.
    def exitSentencia(self, ctx:LPPParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LPPParser#escriba.
    def enterEscriba(self, ctx:LPPParser.EscribaContext):
        pass

    # Exit a parse tree produced by LPPParser#escriba.
    def exitEscriba(self, ctx:LPPParser.EscribaContext):
        pass


    # Enter a parse tree produced by LPPParser#lea.
    def enterLea(self, ctx:LPPParser.LeaContext):
        pass

    # Exit a parse tree produced by LPPParser#lea.
    def exitLea(self, ctx:LPPParser.LeaContext):
        pass


    # Enter a parse tree produced by LPPParser#asignar.
    def enterAsignar(self, ctx:LPPParser.AsignarContext):
        pass

    # Exit a parse tree produced by LPPParser#asignar.
    def exitAsignar(self, ctx:LPPParser.AsignarContext):
        pass


    # Enter a parse tree produced by LPPParser#llamar.
    def enterLlamar(self, ctx:LPPParser.LlamarContext):
        pass

    # Exit a parse tree produced by LPPParser#llamar.
    def exitLlamar(self, ctx:LPPParser.LlamarContext):
        pass


    # Enter a parse tree produced by LPPParser#procedimientoLibreriaEstandar.
    def enterProcedimientoLibreriaEstandar(self, ctx:LPPParser.ProcedimientoLibreriaEstandarContext):
        pass

    # Exit a parse tree produced by LPPParser#procedimientoLibreriaEstandar.
    def exitProcedimientoLibreriaEstandar(self, ctx:LPPParser.ProcedimientoLibreriaEstandarContext):
        pass


    # Enter a parse tree produced by LPPParser#si.
    def enterSi(self, ctx:LPPParser.SiContext):
        pass

    # Exit a parse tree produced by LPPParser#si.
    def exitSi(self, ctx:LPPParser.SiContext):
        pass


    # Enter a parse tree produced by LPPParser#sino.
    def enterSino(self, ctx:LPPParser.SinoContext):
        pass

    # Exit a parse tree produced by LPPParser#sino.
    def exitSino(self, ctx:LPPParser.SinoContext):
        pass


    # Enter a parse tree produced by LPPParser#caso.
    def enterCaso(self, ctx:LPPParser.CasoContext):
        pass

    # Exit a parse tree produced by LPPParser#caso.
    def exitCaso(self, ctx:LPPParser.CasoContext):
        pass


    # Enter a parse tree produced by LPPParser#opcionCaso.
    def enterOpcionCaso(self, ctx:LPPParser.OpcionCasoContext):
        pass

    # Exit a parse tree produced by LPPParser#opcionCaso.
    def exitOpcionCaso(self, ctx:LPPParser.OpcionCasoContext):
        pass


    # Enter a parse tree produced by LPPParser#listaExprOpcion.
    def enterListaExprOpcion(self, ctx:LPPParser.ListaExprOpcionContext):
        pass

    # Exit a parse tree produced by LPPParser#listaExprOpcion.
    def exitListaExprOpcion(self, ctx:LPPParser.ListaExprOpcionContext):
        pass


    # Enter a parse tree produced by LPPParser#exprOpcion.
    def enterExprOpcion(self, ctx:LPPParser.ExprOpcionContext):
        pass

    # Exit a parse tree produced by LPPParser#exprOpcion.
    def exitExprOpcion(self, ctx:LPPParser.ExprOpcionContext):
        pass


    # Enter a parse tree produced by LPPParser#rangoExpr.
    def enterRangoExpr(self, ctx:LPPParser.RangoExprContext):
        pass

    # Exit a parse tree produced by LPPParser#rangoExpr.
    def exitRangoExpr(self, ctx:LPPParser.RangoExprContext):
        pass


    # Enter a parse tree produced by LPPParser#casoSino.
    def enterCasoSino(self, ctx:LPPParser.CasoSinoContext):
        pass

    # Exit a parse tree produced by LPPParser#casoSino.
    def exitCasoSino(self, ctx:LPPParser.CasoSinoContext):
        pass


    # Enter a parse tree produced by LPPParser#mientras.
    def enterMientras(self, ctx:LPPParser.MientrasContext):
        pass

    # Exit a parse tree produced by LPPParser#mientras.
    def exitMientras(self, ctx:LPPParser.MientrasContext):
        pass


    # Enter a parse tree produced by LPPParser#para.
    def enterPara(self, ctx:LPPParser.ParaContext):
        pass

    # Exit a parse tree produced by LPPParser#para.
    def exitPara(self, ctx:LPPParser.ParaContext):
        pass


    # Enter a parse tree produced by LPPParser#repita.
    def enterRepita(self, ctx:LPPParser.RepitaContext):
        pass

    # Exit a parse tree produced by LPPParser#repita.
    def exitRepita(self, ctx:LPPParser.RepitaContext):
        pass


    # Enter a parse tree produced by LPPParser#retorne.
    def enterRetorne(self, ctx:LPPParser.RetorneContext):
        pass

    # Exit a parse tree produced by LPPParser#retorne.
    def exitRetorne(self, ctx:LPPParser.RetorneContext):
        pass


    # Enter a parse tree produced by LPPParser#abrir.
    def enterAbrir(self, ctx:LPPParser.AbrirContext):
        pass

    # Exit a parse tree produced by LPPParser#abrir.
    def exitAbrir(self, ctx:LPPParser.AbrirContext):
        pass


    # Enter a parse tree produced by LPPParser#acceso.
    def enterAcceso(self, ctx:LPPParser.AccesoContext):
        pass

    # Exit a parse tree produced by LPPParser#acceso.
    def exitAcceso(self, ctx:LPPParser.AccesoContext):
        pass


    # Enter a parse tree produced by LPPParser#cerrar.
    def enterCerrar(self, ctx:LPPParser.CerrarContext):
        pass

    # Exit a parse tree produced by LPPParser#cerrar.
    def exitCerrar(self, ctx:LPPParser.CerrarContext):
        pass


    # Enter a parse tree produced by LPPParser#escribir.
    def enterEscribir(self, ctx:LPPParser.EscribirContext):
        pass

    # Exit a parse tree produced by LPPParser#escribir.
    def exitEscribir(self, ctx:LPPParser.EscribirContext):
        pass


    # Enter a parse tree produced by LPPParser#leer.
    def enterLeer(self, ctx:LPPParser.LeerContext):
        pass

    # Exit a parse tree produced by LPPParser#leer.
    def exitLeer(self, ctx:LPPParser.LeerContext):
        pass


    # Enter a parse tree produced by LPPParser#listaExpr.
    def enterListaExpr(self, ctx:LPPParser.ListaExprContext):
        pass

    # Exit a parse tree produced by LPPParser#listaExpr.
    def exitListaExpr(self, ctx:LPPParser.ListaExprContext):
        pass


    # Enter a parse tree produced by LPPParser#expr.
    def enterExpr(self, ctx:LPPParser.ExprContext):
        pass

    # Exit a parse tree produced by LPPParser#expr.
    def exitExpr(self, ctx:LPPParser.ExprContext):
        pass


    # Enter a parse tree produced by LPPParser#funcionLibreriaEstandar.
    def enterFuncionLibreriaEstandar(self, ctx:LPPParser.FuncionLibreriaEstandarContext):
        pass

    # Exit a parse tree produced by LPPParser#funcionLibreriaEstandar.
    def exitFuncionLibreriaEstandar(self, ctx:LPPParser.FuncionLibreriaEstandarContext):
        pass


    # Enter a parse tree produced by LPPParser#literal.
    def enterLiteral(self, ctx:LPPParser.LiteralContext):
        pass

    # Exit a parse tree produced by LPPParser#literal.
    def exitLiteral(self, ctx:LPPParser.LiteralContext):
        pass



del LPPParser