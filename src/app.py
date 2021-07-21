from bottle import app, route, run
from urls import routes
from models import Mes

try:
    f = open('database.db','r')
    f.close()
except:
    Mes.create_table()

application = app()
routes(application)

run(application, host='0.0.0.0', port=3333, reloader=True, debug=True)

