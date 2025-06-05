from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Todo
from datetime import datetime, date
import calendar

@app.route('/')
@app.route('/<int:year>/<int:month>')
def index(year=None, month=None):
    # Get current month and year if not specified
    today = datetime.now()
    if year is None:
        year = today.year
    if month is None:
        month = today.month
    
    # Create calendar for the specified month
    cal = calendar.monthcalendar(year, month)
    
    # Get all todos for the current month
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)
    
    todos = Todo.query.filter(Todo.date >= start_date, Todo.date < end_date).all()
    
    # Organize todos by date
    todos_by_date = {}
    for todo in todos:
        if todo.date not in todos_by_date:
            todos_by_date[todo.date] = []
        todos_by_date[todo.date].append(todo)
    
    # Calculate previous and next month
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
        
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    return render_template('calendar.html', 
                         calendar=cal,
                         month=month,
                         year=year,
                         month_name=calendar.month_name[month],
                         todos_by_date=todos_by_date,
                         date=date,
                         prev_month=prev_month,
                         prev_year=prev_year,
                         next_month=next_month,
                         next_year=next_year)

@app.route('/day/<int:year>/<int:month>/<int:day>')
def day_view(year, month, day):
    selected_date = date(year, month, day)
    incomplete = Todo.query.filter_by(date=selected_date, complete=False).all()
    complete = Todo.query.filter_by(date=selected_date, complete=True).all()
    
    return render_template('day.html', 
                         date=selected_date,
                         incomplete=incomplete,
                         complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo_text = request.form['todoitem']
    todo_date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    todo = Todo(text=todo_text, complete=False, date=todo_date)
    db.session.add(todo)
    db.session.commit()
    
    return redirect(url_for('day_view', 
                          year=todo_date.year,
                          month=todo_date.month,
                          day=todo_date.day))

@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    
    return redirect(url_for('day_view',
                          year=todo.date.year,
                          month=todo.date.month,
                          day=todo.date.day))

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for('day_view',
                          year=todo.date.year,
                          month=todo.date.month,
                          day=todo.date.day))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    if request.method == 'POST':
        todo.text = request.form['new_todoitem']
        db.session.commit()
        return redirect(url_for('day_view',
                              year=todo.date.year,
                              month=todo.date.month,
                              day=todo.date.day))
    else:
        return render_template('update.html', todo=todo)