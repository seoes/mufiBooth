# 첫 번째 Flask Server
from flask import Flask, render_template, make_response, session
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from kiosk.mufiKiosk import kiosk
from web.mufiWeb import web
from webserver.WebServer import server
from markupsafe import escape
from datetime import timedelta

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
app.config['RESTFUL_JSON'] = {'ensure_ascii' : False}
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'mufiHome'
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(minutes=5)


api = Api(app)  # Flask 객체에 Api 객체 등록


api.add_namespace(kiosk,'/kiosk')

api.add_namespace(web,'/web')

api.add_namespace(server,'/webserver')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)