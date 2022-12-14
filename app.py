from flask import Flask, request

app = Flask(__name__)

students = [
     {"name": "anya", "grade": 10, "age": 21},
     {"name": "siya", "grade": 20, "age": 16},
    {"name": "sam", "grade": 40, "age": 20},
]

@app.get("/students") #endpoint to access 
def get_students():
     return {"students": students}

@app.post("/students") 
def create_students():
    request_data = request.get_json()
    new_student = {"name": "Shruti", "grade": 25, "age": 20}
    students.append(request_data)
    return students, 200


@app.patch("/students")
def patch_students():
    request_data = request.get_json()
    global students
    new_list = []
    for student in students:
         if student["grade"] > 15:
            new_list.append(student)
 
    old_length = len(students) 
    students = new_list
    if len(new_list) == old_length:
      return {"message": "no changes in the list", "new_list": new_list}, 200 
    else:
      return{"message": " some changes occured in the list", "new_list": new_list}, 200
    

@app.delete("/students")
def delete_students():
    request_data = request.get_json()
    for student in students:
            if student["age"] > 18:
               students.remove(student)
    return students, 200
        