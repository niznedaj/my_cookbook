import flask.views
import settings
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
# Views
from main import Main
from login import Login
import recipes

# create the application
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, settings.db_name),
    SECRET_KEY=settings.secret_key,
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET", "POST"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET", "POST"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/recipes/add/',
                 view_func=recipes.Add.as_view('add_recipe'),
                 methods=["GET", "POST"])
app.add_url_rule('/recipes/view_all/',
                 view_func=recipes.ViewAll.as_view('view_recipes'),
                 methods=["GET", "POST"])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


app.debug = True
app.run()
