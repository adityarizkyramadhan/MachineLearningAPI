from flask import Flask,render_template,request
import model_salary as m 

setup = Flask(__name__,template_folder="templates")

@setup.route('/',methods=['GET','POST'])
def index():
    ps = 0
    if request.method == 'POST' :
        years = request.form['year']
        predict_salary = m.salary_prediction(years)
        ps = predict_salary
    return render_template("index.html", p = ps)


if __name__ == '__main__':
    app.run(debug=True)


