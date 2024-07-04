from flask import Flask,render_template,request,redirect,url_for,jsonify

app=Flask(__name__)

# #url routing or flask app routing 

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>welcome to your first flask web application framework</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h1>welcome to the index page of project</h2>"

# #varaible rule

@app.route('/success/<int:score>')
def success(score):
    return "The Student Passed the exam and his marks are:" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Student failed the exam and his marks are:" + str(score)


#creating a simple form 
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        res=''
        if average_marks>=50:
            res='success'
        else:
            res='fail'
        return redirect(url_for(res,score=average_marks))


        # return render_template('form.html',score=average_marks)

@app.route("/api",methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)["a"])
    b_val=float(dict(data)["b"])
     
    return jsonify(a_val+b_val)
if __name__ == "__main__":
    app.run(debug=True)
