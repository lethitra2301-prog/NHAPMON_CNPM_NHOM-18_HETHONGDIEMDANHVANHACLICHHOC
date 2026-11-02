from attendance import (
    create_attendance_session,
    record_attendance,
    update_attendance,
    get_attendance_history,
    get_student_statistics
)

# 1. Tao buoi diem danh
print("===== TAO BUOI DIEM DANH =====")

create_attendance_session(
    "DD001",
    "Nhap mon lap trinh",
    "K46A",
    "02/11/2026",
    "07:00"
)

# 2. Ghi nhan diem danh
print("\n===== GHI NHAN DIEM DANH =====")

record_attendance("DD001", "SV001", "Nguyen Van A", "Co mat")
record_attendance("DD001", "SV002", "Tran Van B", "Vang mat")
record_attendance("DD001", "SV003", "Le Van C", "Co mat")

# 3. Cap nhat trang thai
print("\n===== CAP NHAT DIEM DANH =====")

update_attendance("DD001", "SV002", "Co mat")

# 4. Xem lich su
print("\n===== LICH SU DIEM DANH =====")

history = get_attendance_history("SV001")

for record in history:
    print(record)

# 5. Thong ke
print("\n===== THONG KE DIEM DANH =====")

statistics = get_student_statistics("SV001")

for key, value in statistics.items():
    print(key, ":", value)