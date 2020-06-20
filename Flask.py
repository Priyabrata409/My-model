from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def login():
    if request.method=="POST":

       age=request.form["age"]
       salary=request.form["sal"]
       with open("lucky.pkl","rb") as f:
           b=pickle.load(f)
       cls=b[0]
       sc=b[1]
       if cls.predict(sc.transform([[age,salary]]))==1:
          return render_template("login.html",user="The client is able to purchase a SUV")
       else:
           return  render_template("login.html",user="The client is  not able to purchase a SUV")
    else:
       return render_template("login.html",defa="Please Enter your Age and Salary")

if __name__ == "__main__":
    app.run(debug=True)