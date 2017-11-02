from flask import Flask
from flask import render_template

from algorithm.mysorts import MySorts


app = Flask(__name__)


class Human():
    def somemethod(self):
        return self


@app.route('/<name>')
def user(name):
    arr=[23,43,546,78,1,324]
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


if __name__ == '__main__':
    app.run()