# ==========================================
# EDUVISION AI PRO
# Intelligent Student Success & Career Predictor
# ==========================================

print("=" * 70)
print("🎓 EDUVISION AI PRO")
print("Student Success, Risk Analysis & Career Prediction System")
print("=" * 70)

students = []
results = []

# Number of students
num_students = int(input("\nEnter Number of Students: "))

# Input Section
for i in range(num_students):
    print(f"\n{'-' * 50}")
    print(f"Enter Details for Student {i+1}")
    print(f"{'-' * 50}")

    name = input("Student Name: ")
    study_hours = float(input("Study Hours Per Day: "))
    attendance = float(input("Attendance (%): "))
    assignment_score = float(input("Assignment Score (0-100): "))
    test_score = float(input("Test Score (0-100): "))

    # AI Score Formula
    score = (
        study_hours * 5
        + attendance * 0.3
        + assignment_score * 0.3
        + test_score * 0.4
    )

    # Classification
    if score >= 90:
        performance = "High Performer"
    elif score >= 70:
        performance = "Average Performer"
    else:
        performance = "Needs Improvement"

    # Grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Scholarship Eligibility
    if score >= 90:
        scholarship = "Eligible"
    else:
        scholarship = "Not Eligible"

    # Career Recommendation
    if score >= 90:
        career = "AI Engineer / Data Scientist"
    elif score >= 80:
        career = "Software Developer"
    elif score >= 70:
        career = "Business Analyst"
    elif score >= 60:
        career = "Technical Support Specialist"
    else:
        career = "Skill Development Recommended"

    # AI Confidence
    confidence = min(100, int(score))

    # Future Prediction
    if score >= 90:
        future = "Excellent Growth Potential"
    elif score >= 75:
        future = "Good Growth Potential"
    else:
        future = "Needs Guidance and Improvement"

    students.append({
        "name": name,
        "study_hours": study_hours,
        "attendance": attendance,
        "assignment_score": assignment_score,
        "test_score": test_score,
        "score": round(score, 2),
        "performance": performance,
        "grade": grade,
        "scholarship": scholarship,
        "career": career,
        "future": future,
        "confidence": confidence
    })

    results.append(performance)

# ==========================================
# INDIVIDUAL REPORTS
# ==========================================

print("\n\n" + "=" * 70)
print("📊 STUDENT ANALYSIS REPORT")
print("=" * 70)

for student in students:

    print("\n" + "-" * 50)
    print(f"👤 Student Name: {student['name']}")
    print("-" * 50)

    print(f"📚 Study Hours       : {student['study_hours']}")
    print(f"📅 Attendance        : {student['attendance']}%")
    print(f"📝 Assignment Score  : {student['assignment_score']}")
    print(f"📖 Test Score        : {student['test_score']}")
    print(f"🎯 AI Score          : {student['score']}")
    print(f"🏆 Performance       : {student['performance']}")
    print(f"🏅 Grade             : {student['grade']}")
    print(f"🤖 AI Confidence     : {student['confidence']}%")
    print(f"🎓 Scholarship       : {student['scholarship']}")
    print(f"💼 Career Suggestion : {student['career']}")
    print(f"🔮 Future Prediction : {student['future']}")

    # Risk Detection
    risks = []

    if student['attendance'] < 60:
        risks.append("Low Attendance")

    if student['study_hours'] < 3:
        risks.append("Low Study Hours")

    if student['test_score'] < 50:
        risks.append("Low Test Performance")

    if risks:
        print("⚠ Risk Factors:")
        for risk in risks:
            print("   -", risk)

    # Recommendations
    recommendations = []

    if student['attendance'] < 75:
        recommendations.append("Improve attendance")

    if student['study_hours'] < 5:
        recommendations.append("Increase study hours")

    if student['test_score'] < 70:
        recommendations.append("Practice more mock tests")

    if recommendations:
        print("💡 Recommendations:")
        for rec in recommendations:
            print("   -", rec)

    # Motivation
    if student['score'] >= 90:
        print("🌟 Outstanding work! Keep aiming higher.")
    elif student['score'] >= 75:
        print("👍 Good performance. Stay consistent.")
    else:
        print("💪 Improvement is possible. Keep learning.")

# ==========================================
# CLASS ANALYTICS
# ==========================================

print("\n\n" + "=" * 70)
print("📈 CLASS ANALYTICS DASHBOARD")
print("=" * 70)

total_students = len(students)

high = results.count("High Performer")
average = results.count("Average Performer")
low = results.count("Needs Improvement")

avg_score = sum(s["score"] for s in students) / total_students

print(f"👥 Total Students          : {total_students}")
print(f"🌟 High Performers         : {high}")
print(f"📘 Average Performers      : {average}")
print(f"⚠ Needs Improvement       : {low}")
print(f"📊 Average Class Score     : {avg_score:.2f}")

# ==========================================
# LEADERBOARD
# ==========================================

students.sort(key=lambda x: x["score"], reverse=True)

print("\n" + "=" * 70)
print("🏆 STUDENT LEADERBOARD")
print("=" * 70)

for rank, student in enumerate(students, start=1):
    print(
        f"{rank}. {student['name']} | "
        f"Score: {student['score']} | "
        f"Grade: {student['grade']}"
    )

# ==========================================
# TOP PERFORMER
# ==========================================

top_student = students[0]

print("\n🥇 TOP PERFORMER OF THE CLASS")
print("-" * 50)
print(f"Name  : {top_student['name']}")
print(f"Score : {top_student['score']}")
print(f"Grade : {top_student['grade']}")

# ==========================================
# REPORT GENERATION
# ==========================================

with open("student_report.txt", "w", encoding="utf-8") as file:

    file.write("EDUVISION AI PRO REPORT\n")
    file.write("=" * 50 + "\n\n")

    for student in students:
        file.write(f"Name: {student['name']}\n")
        file.write(f"Score: {student['score']}\n")
        file.write(f"Performance: {student['performance']}\n")
        file.write(f"Grade: {student['grade']}\n")
        file.write(f"Career: {student['career']}\n")
        file.write("-" * 40 + "\n")

    file.write("\nTOP PERFORMER\n")
    file.write(f"{top_student['name']} - {top_student['score']}\n")

print("\n💾 Report saved successfully as 'student_report.txt'")

print("\n✅ Project Execution Completed Successfully")
print("🚀 Thank You For Using EduVision AI Pro")