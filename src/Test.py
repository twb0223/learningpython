from flask import Flask, jsonify, render_template

from algorithm.mysorts import MySorts

app = Flask(__name__)

class Human():
    def somemethod(self):
        return self


tasks = [{
    'id': 1,
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done': False
}, {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find a good Python tutorial on the web',
    'done': False
}]


@app.route('/<name>')
def user(name):
    arr = [23, 43, 546, 78, 1, 324]
    MySorts.insert_sort(arr)
    mydict = {"key": "This is a Flask Program"}
    mylist = arr
    myintvar = 0
    myobj = Human()

    return render_template(
        'index.html',
        name=name,
        mydict=mydict,
        mylist=mylist,
        myintvar=myintvar,
        myobj=myobj)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()
