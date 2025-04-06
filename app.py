from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Health Monitoring
@app.route("/health")
def health():
    data_path = os.path.join('static', 'css', 'data', 'health_monitoring.csv')
    data = pd.read_csv(data_path).tail(100)

    fig = px.line(data, x='Timestamp', y='Heart Rate', title='Heart Rate Over Time')
    fig.update_layout(
        xaxis=dict(tickangle=45),
        margin=dict(l=40, r=20, t=50, b=120),
        height=500
    )
    graph_html = fig.to_html(full_html=False)

    return render_template("health.html", graph=graph_html, data=data.to_dict(orient="records"))

# Routine Reminders
@app.route("/reminders")
def reminders():
    reminder_path = os.path.join('static', 'css', 'data', 'daily_reminder.csv')
    reminders = pd.read_csv(reminder_path).tail(900)

    if 'Type' in reminders.columns:
        fig = px.pie(reminders, names='Type', title='Reminder Types Distribution')
        graph_html = fig.to_html(full_html=False)
    else:
        graph_html = None

    return render_template("reminders.html", reminders=reminders.to_dict(orient="records"), graph=graph_html)

# Fall Detection
@app.route("/fall")
def fall():
    data_path = os.path.join('static', 'css', 'data', 'safety_monitoring.csv')
    data = pd.read_csv(data_path).tail(200)

    if 'Location' in data.columns:
        fig = px.bar(data, x='Location', title='Falls by Location')
        graph_html = fig.to_html(full_html=False)
    else:
        graph_html = None

    return render_template("fall.html", data=data.to_dict(orient="records"), graph=graph_html)

# Emergency Alerts
@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

# Diet Plan
@app.route("/diet")
def diet():
    return render_template("diet.html")

# Medications
@app.route("/medications")
def medications():
    return render_template("medications.html")

if __name__ == "__main__":
    app.run(debug=True)
