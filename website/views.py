from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user 
from .models import Note
from .models import UserFoodWaste
from . import db 
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        grain = request.form.get('grain')
        fruit_fresh = request.form.get('fruit_fresh')
        fruit_proc = request.form.get('fruit_proc')
        veggie_fresh= request.form.get('veggie_fresh')
        veggie_proc = request.form.get('veggie_proc')
        milk = request.form.get('milk') 
        dairy = request.form.get('dairy')
        meat = request.form.get('meat')
        poultry = request.form.get('poultry')
        fish_seafood = request.form.get('fish_seafood')
        eggs = request.form.get('eggs')
        nuts = request.form.get('nuts')
        sweet = request.form.get('sweet')
        fats_oils = request.form.get('fats_oils')


        new_note = UserFoodWaste(grain=grain, fruit_fresh=fruit_fresh, fruit_proc=fruit_proc, veggie_fresh=veggie_fresh, 
                                    veggie_proc=veggie_proc, milk=milk, dairy=dairy, meat=meat, poultry=poultry, 
                                    fish_seafood=fish_seafood, eggs=eggs, nuts=nuts, sweet=sweet, fats_oils=fats_oils,
                                    user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Food data recorded!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = UserFoodWaste.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

# TEST
# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('Note is too short!', category='error')
#         else: 
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)


# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
    
#     return jsonify({})
    