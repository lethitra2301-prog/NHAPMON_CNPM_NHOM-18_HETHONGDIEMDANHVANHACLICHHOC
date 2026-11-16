# Lưu danh sách các buổi điểm danh
attendance_sessions = {}


# Tạo buổi điểm danh mới
def create_attendance_session(session_id, subject, class_name, date, start_time):
    if session_id in attendance_sessions:
        print("Ma buoi diem danh da ton tai!")
        return False

    session = {
        "session_id": session_id,
        "subject": subject,
        "class_name": class_name,
        "date": date,
        "start_time": start_time
    }

    attendance_sessions[session_id] = session

    print("Tao buoi diem danh thanh cong!")
    return True


# Xem thong tin mot buoi diem danh
def get_session(session_id):
    if session_id in attendance_sessions:
        return attendance_sessions[session_id]

    print("Khong tim thay buoi diem danh!")
    return None


# Xem tat ca cac buoi diem danh
def get_all_sessions():
    return list(attendance_sessions.values())