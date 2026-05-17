from flask import Flask, render_template

jinja = Flask(__name__, template_folder='../templates')
TEXT = 'Привет это тестовое приложение для знакомства с фласком и щаблонизатором Джинджа'

students = [
    {'name': 'Kostya', 'age':25},
    {'name': 'Nikita', 'age': 28},
    {'name': 'Dima', 'age': 22},
]


@jinja.route('/')
def base():
    return render_template('base.html', dis_text=TEXT, students=students)




if __name__ == '__main__':
    jinja.run()