from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Збереження завдань у пам'яті (можна замінити на базу даних)
days_of_week = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
tasks = {day: [] for day in days_of_week}

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks, days=days_of_week)

@app.route('/add_task', methods=['POST'])
def add_task():
    day = request.form.get('day')
    task = request.form.get('task')
    if day in tasks and task:
        tasks[day].append({"text": task, "done": False})
    return redirect(url_for('home'))

@app.route('/toggle_task', methods=['POST'])
def toggle_task():
    day = request.form.get('day')
    task_index = int(request.form.get('task_index'))
    if day in tasks and 0 <= task_index < len(tasks[day]):
        tasks[day][task_index]["done"] = not tasks[day][task_index]["done"]
    return redirect(url_for('home'))

@app.route('/clear_tasks', methods=['POST'])
def clear_tasks():
    day = request.form.get('day')
    if day in tasks:
        tasks[day] = []
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)