from bottle import route
import controller

def routes(application):
    route("/cadastro-mes/", "POST", controller.cadastro_mes)