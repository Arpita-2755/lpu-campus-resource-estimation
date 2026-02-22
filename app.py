from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Classrooms Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS classrooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            capacity INTEGER,
            enrolled INTEGER
        )
    """)

    # Faculty Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            courses INTEGER
        )
    """)

    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    if request.method == "POST":

        if "classroom_name" in request.form:
            name = request.form["classroom_name"]
            capacity = int(request.form["capacity"])
            enrolled = int(request.form["enrolled"])

            c.execute("INSERT INTO classrooms (name, capacity, enrolled) VALUES (?, ?, ?)",
                      (name, capacity, enrolled))

        if "faculty_name" in request.form:
            name = request.form["faculty_name"]
            courses = int(request.form["courses"])

            c.execute("INSERT INTO faculty (name, courses) VALUES (?, ?)",
                      (name, courses))

        conn.commit()

    c.execute("SELECT * FROM classrooms")
    classrooms = c.fetchall()

    c.execute("SELECT * FROM faculty")
    faculty = c.fetchall()

    total_rooms = len(classrooms)

    total_util = 0
    room_names = []
    utilization_values = []

    for room in classrooms:
        if room[2] != 0:
            util = (room[3] / room[2]) * 100
            total_util += util
            room_names.append(room[1])
            utilization_values.append(round(util, 2))

    avg_util = round(total_util / total_rooms, 2) if total_rooms > 0 else 0

    faculty_names = [f[1] for f in faculty]
    faculty_courses = [f[2] for f in faculty]

    conn.close()

    return render_template("index.html",
                           classrooms=classrooms,
                           faculty=faculty,
                           total_rooms=total_rooms,
                           avg_util=avg_util,
                           room_names=room_names,
                           utilization_values=utilization_values,
                           faculty_names=faculty_names,
                           faculty_courses=faculty_courses)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)