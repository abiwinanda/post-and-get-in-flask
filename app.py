from flask import Flask, jsonify, request

# initialize the app
app = Flask(__name__)

# create in memory data
students = [
    {
        'name': 'Abi',
        'region': 'Bali',
        'subjects': [
            'SKD',
            'PCD',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Tafwida',
        'region': 'Bandung',
        'subjects': [
            'VLSI',
            'DSKC',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Hanif',
        'region': 'Bogor',
        'subjects': [
            'Robotik',
            'PCD',
            'DSKC'
        ]
    }
]

# in a server perspective:
# POST - used to received data
# GET - used to send data back only

# /students - get all students
@app.route('/students', methods=['GET'])
def return_all_students():
    return jsonify(students)

# /students/<string:name> - get a student with spesific name
@app.route('/students/<string:name>', methods=['GET'])
def get_student_with_name(name):
    # get a student with spesific name using lambda expression
    student = list(filter(lambda x: x['name'].lower() == name.lower(), students))

    # check if student exist
    if len(student) != 0:
        return jsonify(student[0]), 200
    else:
        error_response = {
            'error_message': 'student with name ' + name + ' does not exist'
        }
        return jsonify(error_response), 404

# /students/<string:name>/subjects - get all subjects of particular student
@app.route('/students/<string:name>/subjects', methods=['GET'])
def get_subjects_of_student_with_name(name):
    # get a student with spesific name using lambda expression
    student = list(filter(lambda x: x['name'].lower() == name.lower(), students))

    # check if student dose not exist
    if len(student) == 0:
        error_response = {
            'error_message': 'student with name ' + name + ' does not exist'
        }
        return jsonify(error_response), 404

    subjects = student[0]['subjects']
    return jsonify(subjects), 200

# /students/create - create a new student
#
# Parameters:
# string:name            = name of the new student
# string:region          = region of where the new student come from
# list<string>: subjects = list of subject the new student have taken
@app.route('/students/create', methods=['POST'])
def create_new_student():
    # get the body data of the request
    body_data = request.get_json()

    # create a new student
    new_student = {
        'name': body_data['name'],
        'region': body_data['region'],
        'subjects': body_data['subjects']
    }
    students.append(new_student)

    return jsonify(new_student), 201

# run the app at port 5000
app.run(port=5000, debug=True)
