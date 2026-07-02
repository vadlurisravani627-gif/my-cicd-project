from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory student storage
students = [
    {"id": 1, "name": "Sravani", "roll": "21CS001", "branch": "CSE AI&ML", "cgpa": "9.2"},
    {"id": 2, "name": "Rahul", "roll": "21CS002", "branch": "CSE", "cgpa": "8.5"},
    {"id": 3, "name": "Priya", "roll": "21CS003", "branch": "ECE", "cgpa": "8.9"},
]

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Management System</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
                min-height: 100vh;
                color: white;
                padding: 30px;
            }
            h1 {
                text-align: center;
                color: #00d4ff;
                font-size: 36px;
                margin-bottom: 5px;
            }
            .subtitle {
                text-align: center;
                color: #a0a0a0;
                margin-bottom: 30px;
                font-size: 14px;
            }
            .badge {
                text-align: center;
                margin-bottom: 30px;
            }
            .badge span {
                background: #00d4ff;
                color: #000;
                padding: 6px 20px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: bold;
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
            }
            .form-card {
                background: rgba(255,255,255,0.1);
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 30px;
                backdrop-filter: blur(10px);
            }
            .form-card h2 {
                color: #00d4ff;
                margin-bottom: 20px;
            }
            .form-row {
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                margin-bottom: 15px;
            }
            input {
                flex: 1;
                min-width: 150px;
                padding: 10px 15px;
                border-radius: 8px;
                border: 1px solid rgba(255,255,255,0.3);
                background: rgba(255,255,255,0.1);
                color: white;
                font-size: 14px;
            }
            input::placeholder { color: #a0a0a0; }
            button {
                padding: 10px 25px;
                border-radius: 8px;
                border: none;
                cursor: pointer;
                font-size: 14px;
                font-weight: bold;
            }
            .btn-add {
                background: #00d4ff;
                color: #000;
            }
            .btn-search {
                background: #7c3aed;
                color: white;
            }
            .btn-delete {
                background: #ef4444;
                color: white;
                padding: 5px 12px;
                font-size: 12px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th {
                background: rgba(0, 212, 255, 0.2);
                color: #00d4ff;
                padding: 12px;
                text-align: left;
                font-size: 14px;
            }
            td {
                padding: 12px;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                font-size: 14px;
                color: #e0e0e0;
            }
            tr:hover { background: rgba(255,255,255,0.05); }
            .total {
                text-align: right;
                color: #a0a0a0;
                font-size: 13px;
                margin-top: 10px;
            }
            .pipeline {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                flex-wrap: wrap;
                margin-top: 30px;
                font-size: 12px;
            }
            .step {
                background: rgba(0, 212, 255, 0.2);
                border: 1px solid #00d4ff;
                border-radius: 6px;
                padding: 6px 12px;
                color: #00d4ff;
            }
            .arrow { color: #00d4ff; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Student Management System</h1>
            <p class="subtitle">Deployed via CI/CD Pipeline — GitHub Actions + Docker + Render</p>
            <div class="badge"><span>✅ Live & Auto-Deployed</span></div>

            <!-- Add Student -->
            <div class="form-card">
                <h2>➕ Add Student</h2>
                <div class="form-row">
                    <input type="text" id="name" placeholder="Student Name" />
                    <input type="text" id="roll" placeholder="Roll Number" />
                    <input type="text" id="branch" placeholder="Branch" />
                    <input type="text" id="cgpa" placeholder="CGPA" />
                    <button class="btn-add" onclick="addStudent()">Add</button>
                </div>
            </div>

            <!-- Search -->
            <div class="form-card">
                <h2>🔍 Search Student</h2>
                <div class="form-row">
                    <input type="text" id="search" placeholder="Search by name or roll number..." />
                    <button class="btn-search" onclick="searchStudent()">Search</button>
                    <button class="btn-add" onclick="loadStudents()">Show All</button>
                </div>
            </div>

            <!-- Student Table -->
            <div class="form-card">
                <h2>📋 Student Records</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Roll No</th>
                            <th>Branch</th>
                            <th>CGPA</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="studentTable"></tbody>
                </table>
                <p class="total" id="total"></p>
            </div>

            <!-- Pipeline Flow -->
            <div class="pipeline">
                <div class="step">Push Code</div>
                <div class="arrow">→</div>
                <div class="step">GitHub Actions</div>
                <div class="arrow">→</div>
                <div class="step">Docker Build</div>
                <div class="arrow">→</div>
                <div class="step">Render Deploy</div>
                <div class="arrow">→</div>
                <div class="step">Live App ✅</div>
            </div>
        </div>

        <script>
            function loadStudents() {
                fetch('/students')
                    .then(r => r.json())
                    .then(data => renderTable(data));
            }

            function renderTable(data) {
                const tbody = document.getElementById('studentTable');
                const total = document.getElementById('total');
                if (data.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#a0a0a0;">No students found</td></tr>';
                    total.textContent = '';
                    return;
                }
                tbody.innerHTML = data.map(s => `
                    <tr>
                        <td>${s.id}</td>
                        <td>${s.name}</td>
                        <td>${s.roll}</td>
                        <td>${s.branch}</td>
                        <td>${s.cgpa}</td>
                        <td><button class="btn-delete" onclick="deleteStudent(${s.id})">Delete</button></td>
                    </tr>
                `).join('');
                total.textContent = `Total Students: ${data.length}`;
            }

            function addStudent() {
                const name = document.getElementById('name').value;
                const roll = document.getElementById('roll').value;
                const branch = document.getElementById('branch').value;
                const cgpa = document.getElementById('cgpa').value;
                if (!name || !roll || !branch || !cgpa) {
                    alert('Please fill all fields!');
                    return;
                }
                fetch('/students', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({name, roll, branch, cgpa})
                }).then(() => {
                    document.getElementById('name').value = '';
                    document.getElementById('roll').value = '';
                    document.getElementById('branch').value = '';
                    document.getElementById('cgpa').value = '';
                    loadStudents();
                });
            }

            function deleteStudent(id) {
                fetch('/students/' + id, {method: 'DELETE'})
                    .then(() => loadStudents());
            }

            function searchStudent() {
                const query = document.getElementById('search').value;
                fetch('/students/search?q=' + query)
                    .then(r => r.json())
                    .then(data => renderTable(data));
            }

            // Load on start
            loadStudents();
        </script>
    </body>
    </html>
    """

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    new_id = max([s["id"] for s in students], default=0) + 1
    student = {
        "id": new_id,
        "name": data["name"],
        "roll": data["roll"],
        "branch": data["branch"],
        "cgpa": data["cgpa"]
    }
    students.append(student)
    return jsonify(student), 201

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Deleted"}), 200

@app.route("/students/search", methods=["GET"])
def search_students():
    query = request.args.get("q", "").lower()
    results = [s for s in students if query in s["name"].lower() or query in s["roll"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)