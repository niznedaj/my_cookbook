import flask
import flask.views


class RecipeViewAll(flask.views.MethodView):
    def get(self):
        return flask.render_template('view_recipes.html')
