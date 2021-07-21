from bottle import request, response
import json
from models import Mes

def list_mes():
    meses = Mes.select().where(Mes.nome_mes != "")
    payload = []

    for mes in meses.dicts():
        payload.append(mes)

    response.status = 200

    return {response.status: payload}

def cadastro_mes():
    data = request.json
    mes = data["nome_mes"]
    cadastro_mes = Mes(nome_mes=mes)

    consulta_mes = Mes.select().where(Mes.nome_mes == mes).count()
    
    if consulta_mes > 0:
        response.status = 400
        return {response.status: "Já existe esse mes"}      

    try:
        cadastro_mes.save()
        response.status = 200
        return {response.status: "Mes Criado"}
    except:
        response.status = 500
        return {response.status: "Erro na aplicação"}