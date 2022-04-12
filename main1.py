
from flask import  Flask,request

app= Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route('/<name>')
def print_name(name):
    return f"Welcome {name}"

#@app.route('/hello',methods=["GET","POST"])
#def hello():
 #   try:
  #      stu_name = request.args.get("StudentName")
   #     numb = request.args.get("RollNo")
    #    return f"Student name is {stu_name} and roll number id {numb}",210
    #except Exception as e:
     #   return f"Error Occured with message : {e}",401

if __name__ =="__main__":
    app.run(port=8080,debug=True)