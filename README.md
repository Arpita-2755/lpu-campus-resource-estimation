# 🏫 Campus Resource & Parameter Estimation System

## 📌 Project Overview

This project is developed as part of the Smart AI-Enabled LPU Campus Management System.

The system manages campus infrastructure and faculty workload by analyzing:

- Classroom capacity utilization
- Faculty course distribution
- Average usage metrics
- Visual workload analytics

It provides a modern dashboard interface with real-time analytics and graphical visualization.

---

## 🎯 Objectives

- Store and manage classroom data
- Calculate capacity utilization percentage
- Monitor faculty workload
- Provide data-driven insights
- Display analytics through interactive charts

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite
- Bootstrap 5
- Chart.js
- HTML & CSS

---

## 🧠 System Architecture

Frontend:
- Bootstrap-based modern dashboard
- Animated navigation bar
- Analytics cards
- Chart.js visualizations

Backend:
- Flask routing
- SQLite database integration
- Dynamic template rendering using Jinja

Database Tables:

### Classrooms Table
| Field | Type |
|-------|------|
| id | Integer (Primary Key) |
| name | Text |
| capacity | Integer |
| enrolled | Integer |

### Faculty Table
| Field | Type |
|-------|------|
| id | Integer (Primary Key) |
| name | Text |
| courses | Integer |

---

## ⚙️ System Workflow

1. Admin adds classroom details:
   - Room name
   - Total capacity
   - Number of enrolled students

2. System calculates:
   Utilization (%) = (Enrolled / Capacity) × 100

3. Admin adds faculty details:
   - Faculty name
   - Number of assigned courses

4. Dashboard displays:
   - Total classrooms
   - Average utilization
   - Classroom utilization bar chart
   - Faculty workload bar chart

---

## 📊 Features Implemented

- Classroom resource tracking
- Faculty workload monitoring
- Average capacity calculation
- Data visualization dashboard
- Responsive modern UI
- Animated navbar

---

## 🚀 How to Run

### 1. Clone Repository

git clone <your_repo_link>
cd lpu-campus-resource-estimation


### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run Application

python app.py


### 5. Open Browser

http://127.0.0.1:5000


---

## 🔮 Future Enhancements

- AI-based resource optimization
- Automated classroom allocation
- Predictive faculty workload balancing
- Advanced analytics dashboard
- Export reports to PDF

---

## 📚 Academic Context

Developed under:
Smart AI-Enabled LPU Campus Management System (Project II)

---

## 👩‍💻 Author

Arpita Mishra  
B.Tech CSE | Python & Full Stack