from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
import flask.views


class ViewAll(flask.views.MethodView):
    def get(self):
        if not session.get('username'):
            abort(401)
        return flask.render_template('view_recipes.html')


class Add(flask.views.MethodView):
    def get(self):
        if not session.get('username'):
            abort(401)
        return flask.render_template('add_recipe.html')

    def post(self):
        e = (request.form['recipe_name']
             , request.form['ingredients']
             , request.form['steps'])
        #        return redirect(url_for('show_entries'))
        print(e)
        flash('%s added!  Enter another, or use the navigation above on the left.' % request.form['recipe_name'])
        return flask.render_template('add_recipe.html')
