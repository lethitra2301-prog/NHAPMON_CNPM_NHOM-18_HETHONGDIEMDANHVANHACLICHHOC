
from datetime import datetime, timedelta
import time

# ==============================
# DU LIEU BUOI HOC
# ==============================

schedule = [
    {
        "id": 1,
        "subject": "Nhap mon Cong nghe phan mem",
        "date": "2026-11-05 07:00",
        "room": "Phong A101",
        "reminder": 30
    },
    {
        "id": 2,
        "subject": "Lap trinh Python",
        "date": "2026-11-06 13:30",
        "room": "Phong B202",
        "reminder": 15
    },
    {
        "id": 3,
        "subject": "Co so du lieu",
        "date": "2026-11-08 07:00",
        "room": "Phong C103",
        "reminder": 30
    }
]

# ==============================
# DU LIEU DIEM DANH
# ==============================

attendance = [
    {"subject": "Python", "status": "Co mat"},
    {"subject": "Python", "status": "Co mat"},
    {"subject": "Python", "status": "Vang mat"},
    {"subject": "Co so du lieu", "status": "Co mat"},
    {"subject": "Co so du lieu", "status": "Vang mat"},
    {"subject": "Co so du lieu", "status": "Co mat"}
]

# Luu lich su thong bao
notifications = []

# Luu cac buoi hoc da gui nhac
sent_reminders = set()


# ==============================
# CHUC NANG 1:
# HIEN THI CAC BUOI HOC SAP DIEN RA
# ==============================

def show_upcoming_classes():
    print("\n===== CAC BUOI HOC SAP DIEN RA =====")

    now = datetime.now()

    upcoming = []

    for lesson in schedule:
        lesson_time = datetime.strptime(
            lesson["date"], "%Y-%m-%d %H:%M"
        )

        if lesson_time >= now:
            upcoming.append((lesson, lesson_time))

    upcoming.sort(key=lambda x: x[1])

    if not upcoming:
        print("Khong co buoi hoc nao sap dien ra.")
        return

    for lesson, lesson_time in upcoming:
        print("\nMa buoi hoc:", lesson["id"])
        print("Mon hoc:", lesson["subject"])
        print("Thoi gian:", lesson_time.strftime("%d/%m/%Y %H:%M"))
        print("Phong hoc:", lesson["room"])
        print("Nhac truoc:", lesson["reminder"], "phut")


# ==============================
# CHUC NANG 2:
# THIET LAP THOI GIAN NHAC LICH
# ==============================

def set_reminder():
    show_all_classes()

    try:
        lesson_id = int(input("\nNhap ma buoi hoc: "))
        minutes = int(input("Nhap so phut muon nhac truoc: "))

        if minutes < 0:
            print("Thoi gian nhac khong hop le!")
            return

        for lesson in schedule:
            if lesson["id"] == lesson_id:
                lesson["reminder"] = minutes
                sent_reminders.discard(lesson_id)

                print("Cap nhat thoi gian nhac lich thanh cong!")
                return

        print("Khong tim thay buoi hoc!")

    except ValueError:
        print("Vui long nhap so nguyen hop le!")


def show_all_classes():
    print("\n===== DANH SACH BUOI HOC =====")

    for lesson in schedule:
        print(
            f'Ma: {lesson["id"]} | '
            f'Mon: {lesson["subject"]} | '
            f'Thoi gian: {lesson["date"]}'
        )


# ==============================
# CHUC NANG 3:
# GUI THONG BAO NHAC LICH HOC
# ==============================

def send_reminders():
    now = datetime.now()
    found = False

    for lesson in schedule:
        lesson_time = datetime.strptime(
            lesson["date"], "%Y-%m-%d %H:%M"
        )

        reminder_time = lesson_time - timedelta(
            minutes=lesson["reminder"]
        )

        if (
            reminder_time <= now <= lesson_time
            and lesson["id"] not in sent_reminders
        ):
            message = (
                f"Nhac lich hoc: {lesson['subject']} "
                f"luc {lesson_time.strftime('%H:%M %d/%m/%Y')}, "
                f"tai {lesson['room']}."
            )

            print("\n!!! THONG BAO !!!")
            print(message)

            notifications.append({
                "time": now.strftime("%d/%m/%Y %H:%M:%S"),
                "message": message
            })

            sent_reminders.add(lesson["id"])
            found = True

    if not found:
        print("\nHien tai khong co thong bao nhac lich moi.")


# ==============================
# CHUC NANG 4:
# HIEN THI THONG BAO CHO SINH VIEN
# ==============================

def show_notifications():
    print("\n===== THONG BAO CUA SINH VIEN =====")

    if not notifications:
        print("Chua co thong bao nao.")
        return

    for i, notification in enumerate(notifications, 1):
        print(f"\nThong bao {i}")
        print("Thoi gian:", notification["time"])
        print("Noi dung:", notification["message"])


# ==============================
# CHUC NANG 5:
# THONG KE TINH HINH CHUYEN CAN
# ==============================

def attendance_statistics():
    print("\n===== THONG KE CHUYEN CAN =====")

    if not attendance:
        print("Chua co du lieu diem danh.")
        return

    subjects = {}

    for record in attendance:
        subject = record["subject"]
        status = record["status"]

        if subject not in subjects:
            subjects[subject] = {
                "Co mat": 0,
                "Vang mat": 0
            }

        if status in subjects[subject]:
            subjects[subject][status] += 1

    total_present = 0
    total_absent = 0

    for subject, data in subjects.items():
        present = data["Co mat"]
        absent = data["Vang mat"]
        total = present + absent

        percentage = present / total * 100 if total > 0 else 0

        print("\nMon hoc:", subject)
        print("So buoi co mat:", present)
        print("So buoi vang mat:", absent)
        print("Tong so buoi:", total)
        print(f"Ty le chuyen can: {percentage:.2f}%")

        total_present += present
        total_absent += absent

    total = total_present + total_absent

    percentage = (
        total_present / total * 100
        if total > 0 else 0
    )

    print("\n===== TONG KET =====")
    print("Tong so buoi co mat:", total_present)
    print("Tong so buoi vang mat:", total_absent)
    print("Tong so buoi hoc:", total)
    print(f"Ty le chuyen can chung: {percentage:.2f}%")


# ==============================
# CHUONG TRINH CHINH
# ==============================

def main():
    while True:
        print("\n================================")
        print("    QUAN LY NHAC LICH VA THONG KE")
        print("================================")
        print("1. Hien thi buoi hoc sap dien ra")
        print("2. Thiet lap thoi gian nhac lich")
        print("3. Kiem tra va gui thong bao nhac lich")
        print("4. Hien thi thong bao")
        print("5. Thong ke tinh hinh chuyen can")
        print("0. Thoat chuong trinh")

        choice = input("\nNhap lua chon: ")

        if choice == "1":
            show_upcoming_classes()

        elif choice == "2":
            set_reminder()

        elif choice == "3":
            send_reminders()

        elif choice == "4":
            show_notifications()

        elif choice == "5":
            attendance_statistics()

        elif choice == "0":
            print("Ket thuc chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
