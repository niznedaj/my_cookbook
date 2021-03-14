import flask
import flask.views


class Recipe_view_all(flask.views.MethodView):
    def get(self):
        return flask.render_template('view_recipes.html')

