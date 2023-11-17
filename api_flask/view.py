from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from .models.movies import Movies
from .schemas.movies import MoviesSchema
from . import db
import json

views = Blueprint('views', __name__)
movies_schema = MoviesSchema()


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    filmes = Movies.find_by_user_id(current_user.id)

    return render_template("home.html", filmes=filmes)

@views.route('/add_movie', methods=['GET', 'POST'])
@login_required
def add_movie():
    filmes = Movies.find_by_user_id(current_user.id)

    return render_template("add_filme.html", filmes=filmes)

"""def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            #new_note = Note(data=note, user_id=current_user.id)
            #db.session.add(new_note)
            #db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)"""