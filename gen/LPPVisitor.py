# Generated from C:/Users/Kira/PycharmProjects/pythonProject/grammar/LPP.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LPPParser import LPPParser
else:
    from LPPParser import LPPParser

# This class defines a complete generic visitor for a parse tree produced by LPPParser.

class LPPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPPParser#programa.
    def visitPrograma(self, ctx:LPPParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionesTipos.
    def visitDeclaracionesTipos(self, ctx:LPPParser.DeclaracionesTiposContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionRegistro.
    def visitDeclaracionRegistro(self, ctx:LPPParser.DeclaracionRegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionTipo.
    def visitDeclaracionTipo(self, ctx:LPPParser.DeclaracionTipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionesSubprogramas.
    def visitDeclaracionesSubprogramas(self, ctx:LPPParser.DeclaracionesSubprogramasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionProcedimiento.
    def visitDeclaracionProcedimiento(self, ctx:LPPParser.DeclaracionProcedimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:LPPParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#parametros.
    def visitParametros(self, ctx:LPPParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#parametro.
    def visitParametro(self, ctx:LPPParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionesVariables.
    def visitDeclaracionesVariables(self, ctx:LPPParser.DeclaracionesVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#declaracionVariables.
    def visitDeclaracionVariables(self, ctx:LPPParser.DeclaracionVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#tipo.
    def visitTipo(self, ctx:LPPParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#listaIDs.
    def visitListaIDs(self, ctx:LPPParser.ListaIDsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#listaEnteros.
    def visitListaEnteros(self, ctx:LPPParser.ListaEnterosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#sentenciasSubprograma.
    def visitSentenciasSubprograma(self, ctx:LPPParser.SentenciasSubprogramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#sentenciasPrograma.
    def visitSentenciasPrograma(self, ctx:LPPParser.SentenciasProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#sentencias.
    def visitSentencias(self, ctx:LPPParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#sentencia.
    def visitSentencia(self, ctx:LPPParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#escriba.
    def visitEscriba(self, ctx:LPPParser.EscribaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#lea.
    def visitLea(self, ctx:LPPParser.LeaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#asignar.
    def visitAsignar(self, ctx:LPPParser.AsignarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#symbolAssing.
    def visitSymbolAssing(self, ctx:LPPParser.SymbolAssingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#llamar.
    def visitLlamar(self, ctx:LPPParser.LlamarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#procedimientoLibreriaEstandar.
    def visitProcedimientoLibreriaEstandar(self, ctx:LPPParser.ProcedimientoLibreriaEstandarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#si.
    def visitSi(self, ctx:LPPParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#entonces.
    def visitEntonces(self, ctx:LPPParser.EntoncesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#sino.
    def visitSino(self, ctx:LPPParser.SinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#caso.
    def visitCaso(self, ctx:LPPParser.CasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#opcionCaso.
    def visitOpcionCaso(self, ctx:LPPParser.OpcionCasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#listaExprOpcion.
    def visitListaExprOpcion(self, ctx:LPPParser.ListaExprOpcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#exprOpcion.
    def visitExprOpcion(self, ctx:LPPParser.ExprOpcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#rangoExpr.
    def visitRangoExpr(self, ctx:LPPParser.RangoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#casoSino.
    def visitCasoSino(self, ctx:LPPParser.CasoSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#mientras.
    def visitMientras(self, ctx:LPPParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#haga.
    def visitHaga(self, ctx:LPPParser.HagaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#para.
    def visitPara(self, ctx:LPPParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#hasta.
    def visitHasta(self, ctx:LPPParser.HastaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#repita.
    def visitRepita(self, ctx:LPPParser.RepitaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#retorne.
    def visitRetorne(self, ctx:LPPParser.RetorneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#abrir.
    def visitAbrir(self, ctx:LPPParser.AbrirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#acceso.
    def visitAcceso(self, ctx:LPPParser.AccesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#cerrar.
    def visitCerrar(self, ctx:LPPParser.CerrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#escribir.
    def visitEscribir(self, ctx:LPPParser.EscribirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#leer.
    def visitLeer(self, ctx:LPPParser.LeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#listaExpr.
    def visitListaExpr(self, ctx:LPPParser.ListaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#coma.
    def visitComa(self, ctx:LPPParser.ComaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#expr.
    def visitExpr(self, ctx:LPPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#openPar.
    def visitOpenPar(self, ctx:LPPParser.OpenParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#closePar.
    def visitClosePar(self, ctx:LPPParser.CloseParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#openBra.
    def visitOpenBra(self, ctx:LPPParser.OpenBraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#closeBra.
    def visitCloseBra(self, ctx:LPPParser.CloseBraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#exponente.
    def visitExponente(self, ctx:LPPParser.ExponenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#punto.
    def visitPunto(self, ctx:LPPParser.PuntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#funcionLibreriaEstandar.
    def visitFuncionLibreriaEstandar(self, ctx:LPPParser.FuncionLibreriaEstandarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPPParser#literal.
    def visitLiteral(self, ctx:LPPParser.LiteralContext):
        return self.visitChildren(ctx)



del LPPParser