from pickle import TRUE
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user 
from .models import Note
from .models import UserFoodWaste, UserClicks
from . import db 
import json
from dataclasses import dataclass
import jsonpickle
import time
import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        form = request.form.get('food_waste_data')
        if form == "food_waste_data":
            fruit = request.form.get('fruit')
            veggies = request.form.get('veggies')
            dairy = request.form.get('dairy')
            meat = request.form.get('meat')
            poultry = request.form.get('poultry')
            fish_seafood = request.form.get('fish_seafood')
            takeout = request.form.get('takeout')
            other = request.form.get('other')
            # getting js date
            todaysDate = datetime.datetime.now()
            timeTuple = todaysDate.timetuple()
            js_date = int(time.mktime(timeTuple)) 

            new_note = UserFoodWaste(fruit=fruit, veggies=veggies, 
                                        dairy=dairy, meat=meat, poultry=poultry, 
                                        fish_seafood=fish_seafood, takeout=takeout, other=other,
                                        user_id=current_user.id, js_date=js_date) 

            db.session.add(new_note)
            db.session.commit()
            flash('Food data recorded!', category='success')
        
        form = request.form.get('food_waste_CLICK')
        if form == "food_waste_CLICK":
            foodwCLICK = request.form.get('foodwCLICK')
            new_note = UserClicks(foodwCLICK=foodwCLICK, user_id=current_user.id) 
            db.session.add(new_note)
            db.session.commit()
            flash('Showing your general food waste', category='success')
        
        form = request.form.get('money_spent_CLICK')
        if form == "money_spent_CLICK":
            monwCLICK = request.form.get('monwCLICK')
            new_note = UserClicks(monwCLICK=monwCLICK, user_id=current_user.id) 
            db.session.add(new_note)
            db.session.commit()
            flash('Showing your general money spent', category='success')

        form = request.form.get('daily_progress_CLICK')
        if form == "daily_progress_CLICK":
            progCLICK = request.form.get('progCLICK')
            new_note = UserClicks(progCLICK=progCLICK, user_id=current_user.id) 
            db.session.add(new_note)
            db.session.commit()
            flash('Showing your progress over time', category='success')

        form = request.form.get('green_o_meter_CLICK')
        if form == "green_o_meter_CLICK":
            gomCLICK = request.form.get('gomCLICK')
            new_note = UserClicks(gomCLICK=gomCLICK, user_id=current_user.id) 
            db.session.add(new_note)
            db.session.commit()
            flash('Showing your Green-O-Meter', category='success')

    return render_template("home.html", user=current_user)

@views.route('/food-waste-click')
def fun_foodwCLICK():
    new_note = UserClicks(foodwCLICK=1, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({})

@views.route('/money-waste-click')
def fun_monwCLICK():
    new_note = UserClicks(monwCLICK=1, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({})

@views.route('/daily-waste-click')
def fun_progCLICK():
    new_note = UserClicks(progCLICK=1, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({})

@views.route('/gom-click')
def fun_gomCLICK():
    new_note = UserClicks(gomCLICK=1, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({})

@views.route('/user-data')
@login_required
def user_data():
    user_data = UserFoodWaste.query.filter_by(user_id=current_user.id).all()
    return jsonpickle.encode(user_data)


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
    