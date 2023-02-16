from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def main():
    with open('text.txt', 'r',encoding='utf-8') as file:
        resultData=list()
        for line in file.readlines():   
            resultData.append(tuple(line.split('\n')[0].split(';')))
    return render_template('base.html',date = resultData)


@app.route('/index/<x>/<y>')
def index(x,y):
    return f'Cool! sum = {int(x)+int(y)}'

if __name__ == '__main__':
    app.run()

@app.route('/bootcamp')
def about():
    return render_template('bootcamp.html')
