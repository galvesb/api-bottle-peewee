from bottle import request, response
import json

from peewee import Select
from models import Mes


def atualiza_mes(mes_id):

    data = request.json

    nome_mes = data["nome_mes"]

    mes = Mes.select().where(Mes.id == mes_id).count()
    
    if not mes:
        response.status = 400
        return {response.status: "Mês não existe"}

    update_mes = Mes.update({Mes.nome_mes : nome_mes}).where(Mes.id == mes_id)
    update_mes.execute()

    response.status = 200

    return {response.status : "Mês atualizado"}

def deleta_mes(mes_id):
    mes = Mes.select().where(Mes.id == mes_id).count()
    
    if not mes:
        response.status = 400
        return {response.status: "Mês não existe"}

    response.status = 200
    
    exclui_mes = Mes.delete().where(Mes.id == mes_id)
    exclui_mes.execute()

    return {response.status: "Mês deletado"}

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