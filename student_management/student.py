def them_sinh_vien(ds_sinh_vien):
    ma_sv = input("Nhập mã sinh viên: ").strip()

    if any(sv["ma_sv"] == ma_sv for sv in ds_sinh_vien):
        print("Mã sinh viên đã tồn tại!")
        return

    ho_ten = input("Nhập họ tên: ").strip()
    lop = input("Nhập lớp: ").strip()
    ngay_sinh = input("Nhập ngày sinh: ").strip()

    if not ma_sv or not ho_ten or not lop or not ngay_sinh:
        print("Không được để trống thông tin!")
        return

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "lop": lop,
        "ngay_sinh": ngay_sinh
    }

    ds_sinh_vien.append(sinh_vien)
    print("Thêm sinh viên thành công!")


def sua_sinh_vien(ds_sinh_vien):
    ma_sv = input("Nhập mã sinh viên cần sửa: ").strip()

    for sv in ds_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            print("Để trống nếu muốn giữ nguyên thông tin.")

            ho_ten = input("Họ tên mới: ").strip()
            lop = input("Lớp mới: ").strip()
            ngay_sinh = input("Ngày sinh mới: ").strip()

            if ho_ten:
                sv["ho_ten"] = ho_ten
            if lop:
                sv["lop"] = lop
            if ngay_sinh:
                sv["ngay_sinh"] = ngay_sinh

            print("Cập nhật thông tin thành công!")
            return

    print("Không tìm thấy sinh viên!")


def xoa_sinh_vien(ds_sinh_vien):
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip()

    for sv in ds_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            xac_nhan = input("Bạn có chắc chắn muốn xóa? (y/n): ")

            if xac_nhan.lower() == "y":
                ds_sinh_vien.remove(sv)
                print("Xóa sinh viên thành công!")
            else:
                print("Đã hủy thao tác.")
            return

    print("Không tìm thấy sinh viên!")


def tim_kiem_sinh_vien(ds_sinh_vien):
    tu_khoa = input("Nhập mã hoặc tên sinh viên cần tìm: ").strip().lower()

    ket_qua = [
        sv for sv in ds_sinh_vien
        if tu_khoa in sv["ma_sv"].lower()
        or tu_khoa in sv["ho_ten"].lower()
    ]

    if ket_qua:
        hien_thi_danh_sach(ket_qua)
    else:
        print("Không tìm thấy sinh viên phù hợp!")


def hien_thi_danh_sach(ds_sinh_vien):
    if not ds_sinh_vien:
        print("Danh sách sinh viên đang trống!")
        return

    print("\n========== DANH SÁCH SINH VIÊN ==========")
    print("{:<15} {:<25} {:<15} {:<15}".format(
        "Mã SV", "Họ tên", "Lớp", "Ngày sinh"
    ))

    for sv in ds_sinh_vien:
        print("{:<15} {:<25} {:<15} {:<15}".format(
            sv["ma_sv"],
            sv["ho_ten"],
            sv["lop"],
            sv["ngay_sinh"]
        ))