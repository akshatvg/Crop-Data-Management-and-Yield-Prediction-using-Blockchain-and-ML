from flask import Flask, jsonify, Response, request
import sys, os
sys.path.insert(0, './addon')
sys.path.insert(0, './config')
sys.path.insert(0, './prediction')
import getCondition
import devfest_0
app = Flask(__name__)

# @app.route('/pos',methods=['post','get'])
# def index():
#     lat=request.args.get('lat')
#     lng=request.args.get('lng')
#     crop=request.args.get('crop')
#     return jsonify(getCondition.exec(12.97535830000   0002,79.1604862))

@app.route('/',methods=['post','get'])
def latlng():
    lat=request.args.get('lat')
    lng=request.args.get('lng')
    crop=request.args.get('crop')
    if(crop not in ['rice','bajra','maize']): return ''
    if(not float(lat) or not float(lng)): return ''
    cond=getCondition.exec(float(lat),float(lng))
    print(cond)
    yieldAmount=devfest_0.predict(crop,cond[0],cond[1])

    yieldType=0 #0->low;1->normal;2->bumper
    if(yieldAmount>3000): yieldType=2
    elif(yieldAmount>300): yieldType=1
    return jsonify({'yield':yieldAmount, 'type': yieldType})
# print(getCondition.exec(12.975358300000002,79.1604862))



@app.after_request
def setcores(response):
    response.headers['Access-Control-Allow-Origin']='*'
    # response.headers['Access-Control-Allow-Headers']='Content-Type'
    response.headers["Access-Control-Allow-Headers"]= "authorization, Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    response.headers['Access-Control-Allow-Methods']='GET, PUT, POST, DELETE, PATCH, OPTIONS'
    response.headers["Access-Control-Allow-Credentials"]= "true"
    return response
    
debug=False
if('HEROKU' not in os.environ):
    debug=True

if __name__ == '__main__':
    app.run(debug=debug)
