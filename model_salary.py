import joblib
import math

def salary_prediction(year):
    lr_load = joblib.load("./lr.joblib")
    salary = "belum ada"
    prediction = lr_load.predict([[year]])
    for pred in prediction :
        salary = pred
    return_salary = "$" + formatgaji(math.ceil(salary))
    return return_salary

def formatgaji (gaji) : 
    temp = "{:,}".format(gaji)
    return temp
