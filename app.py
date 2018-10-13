from flask import Flask, jsonify, request

# initialize the app
app = Flask(__name__)

# create in memory data
students = [
    {
        'name': 'Abi',
        'region': 'Bali',
        'subject': [
            'SKD',
            'PCD',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Tafwida',
        'region': 'Bandung',
        'subject': [
            'VLSI',
            'DSKC',
            'ARSIKOMPAR'
        ]
    },
    {
        'name': 'Hanif',
        'region': 'Bogor',
        'subject': [
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
    return jsonify(student[0])

# run the app at port 5000
app.run(port=5000, debug=True)
