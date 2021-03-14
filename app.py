import flask.views
import settings

# Views
from main import Main

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET", "POST"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET", "POST"])


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404


app.debug = True
app.run()
