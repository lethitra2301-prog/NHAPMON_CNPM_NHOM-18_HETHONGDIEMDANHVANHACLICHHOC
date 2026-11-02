# auth.py - Chức năng Đăng nhập & Phân quyền hệ thống
import hashlib

# Cơ sở dữ liệu tài khoản giả lập
USERS_DB = {
    "admin@gmail.com": {
        "password_hash": hashlib.sha256("123456".encode()).hexdigest(),
        "role": "ADMIN",
        "name": "Quan tri vien"
    },
    "teacher@gmail.com": {
        "password_hash": hashlib.sha256("123456".encode()).hexdigest(),
        "role": "TEACHER",
        "name": "Giang vien"
    },
    "student@gmail.com": {
        "password_hash": hashlib.sha256("123456".encode()).hexdigest(),
        "role": "STUDENT",
        "name": "Sinh vien"
    }
}

def login(email, password):
    """Xử lý đăng nhập và xác thực vai trò"""
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user = USERS_DB.get(email)

    if user and user["password_hash"] == password_hash:
        print(f"Đăng nhập thành công! Chào mừng {user['name']} (Vai trò: {user['role']})")
        return user
    else:
        print("Email hoặc mật khẩu không chính xác!")
        return None

if _name_ == "_main_":
    # Kiểm thử chức năng đăng nhập
    print("--- KIỂM THỬ HỆ THỐNG QUẢN LÝ TÀI KHOẢN ---")
    login("admin@gmail.com", "123456")