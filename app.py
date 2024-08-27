# fichier main.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all() #Récupérer toute la db Task -> tasks
    return render_template('index.html', tasks=tasks) #Afficher index avec les infos de tasks

@app.route('/add', methods=['POST'])
def add():
    task_description = request.form['task'] #Récup form html 'task' -> task_desc
    db.session.add(Task(description=task_description)) #Ajouter à Task dans description le task descr 
    db.session.commit()
    return redirect(url_for('index')) #redirection sur la même page (actualisation de la page)

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    db.session.delete(Task.query.get_or_404(task_id))
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

