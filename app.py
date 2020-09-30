from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)
from movies.kickass import kickass_search as kickass
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

global magnet
@app.route("/<string:query>")
def home(query):

    return render_template('index.html',movies=kickass(query))

@app.route("/m")
def magnet():
    magnet = request.args.get("magnet")
    return render_template('magnet.html',magnet=magnet)

if __name__=='__main__':
    app.debug=True
    app.run()
    
