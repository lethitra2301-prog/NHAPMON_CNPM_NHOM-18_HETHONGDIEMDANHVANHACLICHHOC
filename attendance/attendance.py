from .attendance_session import attendance_sessions

# Luu danh sach diem danh
attendance_records = {}


# Ghi nhan diem danh sinh vien
def record_attendance(session_id, student_id, student_name, status):

    if session_id not in attendance_sessions:
        print("Buoi diem danh khong ton tai!")
        return False

    if status not in ["Co mat", "Vang mat"]:
        print("Trang thai khong hop le!")
        return False

    # Tao danh sach cho buoi diem danh
    if session_id not in attendance_records:
        attendance_records[session_id] = {}

    # Kiem tra sinh vien da duoc diem danh chua
    if student_id in attendance_records[session_id]:
        print("Sinh vien da duoc diem danh!")
        return False

    attendance_records[session_id][student_id] = {
        "student_id": student_id,
        "student_name": student_name,
        "status": status
    }

    print("Ghi nhan diem danh thanh cong!")
    return True


# Cap nhat trang thai diem danh
def update_attendance(session_id, student_id, new_status):

    if session_id not in attendance_records:
        print("Khong tim thay buoi diem danh!")
        return False

    if student_id not in attendance_records[session_id]:
        print("Khong tim thay sinh vien!")
        return False

    if new_status not in ["Co mat", "Vang mat"]:
        print("Trang thai khong hop le!")
        return False

    attendance_records[session_id][student_id]["status"] = new_status

    print("Cap nhat trang thai thanh cong!")
    return True


# Xem lich su diem danh
def get_attendance_history(student_id):

    history = []

    for session_id, students in attendance_records.items():

        if student_id in students:

            session = attendance_sessions[session_id]

            record = {
                "student_id": student_id,
                "student_name": students[student_id]["student_name"],
                "subject": session["subject"],
                "class_name": session["class_name"],
                "date": session["date"],
                "status": students[student_id]["status"]
            }

            history.append(record)

    return history


# Xem danh sach diem danh cua mot buoi
def get_session_attendance(session_id):

    if session_id not in attendance_records:
        return []

    return list(attendance_records[session_id].values())