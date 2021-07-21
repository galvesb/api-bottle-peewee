from bottle import route
import controller

def routes(application):
    route("/cadastro-mes/", "POST", controller.cadastro_mes)
    route("/lista-meses/", "GET", controller.list_mes)
    route("/deleta-mes/<mes_id>", "DELETE", controller.deleta_mes)