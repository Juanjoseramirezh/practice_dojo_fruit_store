from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)

    #REQUEST - QUANTITY FRUIT SELECT
    strawberry_from_form = int(request.form['strawberry'])
    raspberry_from_form = int(request.form['raspberry'])
    apple_from_form = int(request.form['apple'])

    #REQUEST - FROM PERSONAL FORM
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_fomr = request.form['student_id']

    return render_template("checkout.html",strawberry_on_template = strawberry_from_form, raspberry_on_template = raspberry_from_form, apple_on_template = apple_from_form, first_name_on_template = first_name_from_form, last_name_on_template = last_name_from_form, student_id_on_template = strawberry_from_form)

@app.route('/pay', methods = ['GET']) # CUAL METODO? 
def pay():
    return render_template("pay.html")


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    