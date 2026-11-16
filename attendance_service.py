from datetime import datetime

class AttendanceService:
    def __init__(self):
        # Giả lập cơ sở dữ liệu lưu dưới dạng Dictionary
        self.attendance_db = {}

    def record_attendance(self, session_id: str, student_id: str, status: str) -> bool:
        """
        Ghi nhận điểm danh cho sinh viên trong một buổi học.
        Đáp ứng yêu cầu: Trạng thái (PRESENT, LATE, ABSENT) và chống trùng lặp.
        """
        key = f"{session_id}_{student_id}"
        
        # 1. Hạn chế việc điểm danh trùng lặp trong cùng một buổi học (Nhiệm vụ 7)
        if key in self.attendance_db:
            raise ValueError("Sinh viên này đã được điểm danh trong buổi học này rồi!")

        # 2. Kiểm tra trạng thái hợp lệ (Nhiệm vụ 2 & 6)
        valid_statuses = ["PRESENT", "LATE", "ABSENT"]
        if status not in valid_statuses:
            raise ValueError("Trạng thái điểm danh không hợp lệ! Chỉ chấp nhận: PRESENT, LATE, ABSENT.")

        # 3. Lưu thông tin điểm danh (Nhiệm vụ 3)
        self.attendance_db[key] = {
            "session_id": session_id,
            "student_id": student_id,
            "status": status,
            "check_in_time": datetime.now()
        }
        return True

    def get_attendance_by_session(self, session_id: str) -> list:
        """
        Tra cứu / hiển thị danh sách điểm danh theo buổi học (Nhiệm vụ 4 & 5)
        """
        result = []
        for record in self.attendance_db.values():
            if record["session_id"] == session_id:
                result.append(record)
        return result