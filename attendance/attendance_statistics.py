from .attendance import attendance_records


# Thong ke diem danh cua sinh vien
def get_student_statistics(student_id):

    present = 0
    absent = 0
    total = 0

    for students in attendance_records.values():

        if student_id in students:

            status = students[student_id]["status"]

            total += 1

            if status == "Co mat":
                present += 1

            elif status == "Vang mat":
                absent += 1

    # Tinh ty le co mat
    if total > 0:
        attendance_rate = present / total * 100
    else:
        attendance_rate = 0

    statistics = {
        "student_id": student_id,
        "total_sessions": total,
        "present": present,
        "absent": absent,
        "attendance_rate": round(attendance_rate, 2)
    }

    return statistics