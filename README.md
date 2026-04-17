🎓 Student Risk Monitoring & Dropout Prediction Dashboard

A Power BI–based analytics dashboard designed to identify, monitor, and analyze student dropout risk using academic, attendance, and behavioral data.
This project helps institutions take data-driven early intervention decisions.

📌 Project Overview

Student dropout is a major challenge in educational institutions.
This dashboard provides a centralized risk monitoring system that:

Detects high-risk students early

Tracks academic & behavioral risk factors

Enables drill-down analysis at individual student level

Supports data-driven decision making

🧠 Key Features
✅ 1. Student Risk Monitoring Dashboard (Home Page)

Total Students

At-Risk Students

Safe Students

Dropout Percentage

Average Attendance %

Average CGPA

Overall Risk Score (Gauge)

📊 Visuals:

At-Risk Students by Year

At-Risk Students by Course

Academic Performance Distribution

Attendance vs CGPA vs Participation (Scatter)

📊 2. Risk Analysis Page

Risk Factor Comparison:

Attendance

Backlogs

Disciplinary Cases

Counseling Sessions

Dropout Risk Heatmap (Course × Year)

Gender-wise Dropout Risk Analysis

Dropout Risk Trend by Academic Year & Course

🎯 Purpose:

Understand why students are at risk, not just who is at risk.

🔍 3. Student Drilldown Page

Top 10 High-Risk Students

Detailed student performance metrics

Risk severity comparison

Risk Score % ranking

Interactive filtering & sorting

🔥 Highlights:

Top-N filtering

Risk severity visualization

Action-oriented insights

🧠 4. Individual Student Risk Breakdown

Student-wise risk profiling

Risk Level classification:

Low

Medium

High

Critical

Conditional formatting for quick identification

Dynamic slicers:

Year

Course

Risk Level

Student Name

⚙️ Risk Score Calculation Logic

Risk Score is calculated using academic and behavioral indicators:

Risk Score =
(Backlogs × 10)
+ (100 − Attendance %)
+ (Disciplinary / Counseling Cases × 5)
🎯 Risk Score Percentage

Normalized to 0–100 scale

Enables easy comparison and ranking

🧰 Tools & Technologies Used

Power BI

DAX (Data Analysis Expressions)

Data Modeling & Relationships

Interactive Visualizations

Conditional Formatting

Drillthrough & Filters

📂 Dataset Description

The dataset includes:

Student Demographics

Academic Performance (CGPA, Backlogs)

Attendance Records

Behavioral Data (Disciplinary / Counseling Sessions)

Dropout Risk Labels

⚠️ Data used is synthetic and created for educational/demo purposes.
