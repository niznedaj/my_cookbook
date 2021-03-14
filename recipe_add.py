import flask
import flask.views


class Recipe_add(flask.views.MethodView):
    def get(self):
        return flask.render_template('add_recipe.html')

    def post(self):
        flask.flash('Recipe added!  Enter another, or use the navigation above on the left.')
        return flask.render_template('add_recipe.html')
