from flask import (
    Blueprint, render_template, request, redirect, url_for
    )
from models import db, Todo
from flask_sqlalchemy import sqlalchemy
from settings import get_value

todo_blueprint = Blueprint('todo', __name__, url_prefix='/todo')


@todo_blueprint.route("/")
def todo():
    return render_template('todo/index.html', todo=Todo.query.all(), OUR_APP_NAME=get_value('OUR_APP_NAME'),
        SECTION_NAME=get_value('SECTION_NAME'))


@todo_blueprint.route('/add', methods=['GET', 'POST'])
def todo_add():
    if request.method == 'POST':
        name = request.form['name']
        body = request.form['body']
        active = request.form['active']
        time = request.form['time']
        date = request.form['date']
        newTodo = Todo(name=name, body=body, date=date, active=active)
        db.session.add(newTodo)
        db.session.commit()
        return redirect('/todo/add')
    return render_template('todo/add.html')


@todo_blueprint.route('/delete/<todo_id>', methods=['GET', 'POST'])
def todo_delete(todo_id):

    if request.method == 'POST':
        #Appointments.query.filter(Appointments.id == ids).delete()
        Todo.query.filter(Todo.id == todo_id).delete()
        # db.session.delete(todo)
        db.session.commit()
        return redirect('/todo')
    


@todo_blueprint.route('/update', methods=['GET', 'POST'])
def todo_update():
    # if request.method == 'POST': #this block is only entered when the form is submitted
    #     name = request.form['todo_name']
    #     old_name = request.form['old_todo_name']
    #     try:
    #         t = todo.query.get(old_name)
    #         t.name = name
    #         db.session.commit()
    #     except sqlalchemy.exc.IntegrityError:
    #         # return redirect('/todo/')
    #         render_template('todo_message.html', 
    #             message="you cannot modify to an already existing todo",
    #             redirect_url="/todo/", OUR_APP_NAME=get_value('OUR_APP_NAME'), 
    #             SECTION_NAME=get_value('SECTION_NAME'))
    
    #     return redirect('/todo/')


    todo = Todo.query.get(todo_id)
    if request.method == 'GET':
        return render_template(
            'new-task.html',
            todo=todo
        )
    else:
        
        description = request.form['description']
        todo.description = description
        db.session.commit()
        return redirect('/todo')


@todo_blueprint.route('/edit/<todo_name>', methods=['GET', 'POST'])
def todo_edit(todo_name):
    m = todoturers.query.get(todo_name)
    return render_template(
        'todo/edit.html', todo=todo_name, OUR_APP_NAME=get_value('OUR_APP_NAME'), 
        SECTION_NAME=get_value('SECTION_NAME'))



