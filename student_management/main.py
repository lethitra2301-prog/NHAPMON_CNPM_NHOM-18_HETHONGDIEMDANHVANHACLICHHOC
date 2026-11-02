from student import (
    them_sinh_vien,
    sua_sinh_vien,
    xoa_sinh_vien,
    tim_kiem_sinh_vien,
    hien_thi_danh_sach
)

ds_sinh_vien = []

while True:
    print("\n====== QUẢN LÝ SINH VIÊN ======")
    print("1. Thêm sinh viên")
    print("2. Sửa thông tin sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm sinh viên")
    print("5. Xem danh sách sinh viên")
    print("0. Thoát chương trình")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == "1":
        them_sinh_vien(ds_sinh_vien)
    elif lua_chon == "2":
        sua_sinh_vien(ds_sinh_vien)
    elif lua_chon == "3":
        xoa_sinh_vien(ds_sinh_vien)
    elif lua_chon == "4":
        tim_kiem_sinh_vien(ds_sinh_vien)
    elif lua_chon == "5":
        hien_thi_danh_sach(ds_sinh_vien)
    elif lua_chon == "0":
        print("Đã thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")