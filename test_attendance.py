import unittest
from attendance_service import AttendanceService

class TestAttendanceService(unittest.TestCase):
    
    def setUp(self):
        self.service = AttendanceService()

    def test_record_attendance_success(self):
        """Test điểm danh thành công"""
        success = self.service.record_attendance("S01", "SV001", "PRESENT")
        self.assertTrue(success)
        
        records = self.service.get_attendance_by_session("S01")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["student_id"], "SV001")
        self.assertEqual(records[0]["status"], "PRESENT")

    def test_duplicate_attendance_fail(self):
        """Test chống trùng lặp điểm danh trong cùng một buổi (Nhiệm vụ 7)"""
        self.service.record_attendance("S01", "SV001", "PRESENT")
        
        with self.assertRaises(ValueError) as context:
            self.service.record_attendance("S01", "SV001", "LATE")
            
        self.assertEqual(str(context.exception), "Sinh viên này đã được điểm danh trong buổi học này rồi!")

    def test_invalid_status_fail(self):
        """Test trạng thái điểm danh không hợp lệ"""
        with self.assertRaises(ValueError) as context:
            self.service.record_attendance("S01", "SV002", "INVALID")
            
        self.assertEqual(str(context.exception), "Trạng thái điểm danh không hợp lệ! Chỉ chấp nhận: PRESENT, LATE, ABSENT.")

if __name__ == "__main__":
    unittest.main()