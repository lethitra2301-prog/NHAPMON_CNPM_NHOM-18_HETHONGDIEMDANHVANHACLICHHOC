class QuanLyLopHoc:
    def __init__(self):
        self.danh_sach_lop = {}      # Lưu thông tin lớp học
        self.danh_sach_mon_hoc = []  # Danh sách các môn học
        self.danh_sach_giang_vien = [] # Danh sách giảng viên

    # ================= 1. QUẢN LÝ MÔN HỌC =================
    def them_mon_hoc(self, ten_mon):
        if ten_mon not in self.danh_sach_mon_hoc:
            self.danh_sach_mon_hoc.append(ten_mon)
            print(f"✅ Đã thêm môn học thành công: {ten_mon}")
        else:
            print(f"⚠️ Môn học '{ten_mon}' đã tồn tại trong hệ thống!")

    def hien_thi_mon_hoc(self):
        print("\n--- DANH SÁCH MÔN HỌC ---")
        if not self.danh_sach_mon_hoc:
            print("Chưa có môn học nào.")
        for idx, mon in enumerate(self.danh_sach_mon_hoc, 1):
            print(f"{idx}. {mon}")

    # ================= 2. QUẢN LÝ GIẢNG VIÊN =================
    def them_giang_vien(self, ten_gv):
        if ten_gv not in self.danh_sach_giang_vien:
            self.danh_sach_giang_vien.append(ten_gv)
            print(f"✅ Đã thêm giảng viên thành công: {ten_gv}")
        else:
            print(f"⚠️ Giảng viên '{ten_gv}' đã tồn tại!")

    def hien_thi_giang_vien(self):
        print("\n--- DANH SÁCH GIẢNG VIÊN ---")
        if not self.danh_sach_giang_vien:
            print("Chưa có giảng viên nào.")
        for idx, gv in enumerate(self.danh_sach_giang_vien, 1):
            print(f"{idx}. {gv}")

    # ================= 3. THÊM, SỬA, XÓA LỚP HỌC =================
    def them_lop_hoc(self, ma_lop, ten_lop, mon_hoc, giang_vien):
        if ma_lop in self.danh_sach_lop:
            print(f"❌ Mã lớp '{ma_lop}' đã tồn tại! Vui lòng dùng mã khác.")
            return
        
        self.danh_sach_lop[ma_lop] = {
            "ten_lop": ten_lop,
            "mon_hoc": mon_hoc,
            "giang_vien": giang_vien,
            "sinh_vien": []  # Danh sách sinh viên trong lớp
        }
        print(f"✅ Đã tạo lớp học thành công: {ten_lop} (Mã: {ma_lop})")

    def sua_lop_hoc(self, ma_lop, ten_lop=None, mon_hoc=None, giang_vien=None):
        if ma_lop not in self.danh_sach_lop:
            print(f"❌ Không tìm thấy mã lớp '{ma_lop}' để sửa!")
            return
        
        if ten_lop:
            self.danh_sach_lop[ma_lop]["ten_lop"] = ten_lop
        if mon_hoc:
            self.danh_sach_lop[ma_lop]["mon_hoc"] = mon_hoc
        if giang_vien:
            self.danh_sach_lop[ma_lop]["giang_vien"] = giang_vien
        
        print(f"✅ Đã cập nhật thành công thông tin cho lớp {ma_lop}")

    def xoa_lop_hoc(self, ma_lop):
        if ma_lop in self.danh_sach_lop:
            del self.danh_sach_lop[ma_lop]
            print(f"🗑️ Đã xóa thành công lớp học có mã: {ma_lop}")
        else:
    print(f"❌ Không tìm thấy mã lớp '{ma_lop}' cần xóa!")

    # ================= 4. PHÂN SINH VIÊN VÀO LỚP =================
    def phan_sinh_vien_vao_lop(self, ma_lop, ten_sinh_vien):
        if ma_lop not in self.danh_sach_lop:
            print(f"❌ Không tìm thấy mã lớp '{ma_lop}'!")
            return
        
        if ten_sinh_vien not in self.danh_sach_lop[ma_lop]["sinh_vien"]:
            self.danh_sach_lop[ma_lop]["sinh_vien"].append(ten_sinh_vien)
            print(f"✅ Đã phân sinh viên '{ten_sinh_vien}' vào lớp {ma_lop}")
        else:
            print(f"⚠️ Sinh viên '{ten_sinh_vien}' đã có trong lớp này rồi!")

    # ================= 5. XEM THÔNG TIN LỚP HỌC =================
    def xem_thong_tin_lop(self, ma_lop):
        if ma_lop not in self.danh_sach_lop:
            print(f"❌ Không tìm thấy mã lớp '{ma_lop}'!")
            return
        
        lop = self.danh_sach_lop[ma_lop]
        print(f"\n========================================")
        print(f"📌 THÔNG TIN CHI TIẾT LỚP: {ma_lop}")
        print(f"• Tên lớp: {lop['ten_lop']}")
        print(f"• Môn học: {lop['mon_hoc']}")
        print(f"• Giảng viên phụ trách: {lop['giang_vien']}")
        print(f"• Sĩ số: {len(lop['sinh_vien'])} sinh viên")
        print(f"• Danh sách sinh viên:")
        if not lop['sinh_vien']:
            print("  (Chưa có sinh viên nào trong lớp)")
        else:
            for idx, sv in enumerate(lop['sinh_vien'], 1):
                print(f"  {idx}. {sv}")
        print(f"========================================")


# ================= CHẠY THỬ NGHIỆM (DEMO) =================
if __name__ == "__main__":
    quan_ly = QuanLyLopHoc()

    # 1. Thêm môn học & giảng viên
    quan_ly.them_mon_hoc("Nhập môn Công nghệ phần mềm")
    quan_ly.them_giang_vien("TS. Trần Văn Long")

    # 2. Thêm lớp học mới
    quan_ly.them_lop_hoc(
        ma_lop="CNPM01", 
        ten_lop="Thực hành CNPM - Nhóm 18", 
        mon_hoc="Nhập môn Công nghệ phần mềm", 
        giang_vien="TS. Trần Văn Long"
    )

    # 3. Phân sinh viên vào lớp
    quan_ly.phan_sinh_vien_vao_lop("CNPM01", "Nguyễn Văn A")
    quan_ly.phan_sinh_vien_vao_lop("CNPM01", "Trần Thị B")

    # 4. Xem thông tin lớp học
    quan_ly.xem_thong_tin_lop("CNPM01")

    # 5. Sửa thông tin lớp học
    quan_ly.sua_lop_hoc("CNPM01", ten_lop="Thực hành CNPM - Lớp Đặc Biệt")
    quan_ly.xem_thong_tin_lop("CNPM01")        