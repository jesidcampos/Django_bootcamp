from django.http import HttpResponse
import datetime

def saludo(request,edad, agno):
    #EdadActual = 18
    periodo = agno - 2019
    edadfutura = edad + periodo
    documento = """
    <html>
    <body>
        <h1>
            En el año {0} tendrás {1} años
        <h1>
    </body>
    </html>
    """.format(agno, edadfutura)     
    return HttpResponse(documento)