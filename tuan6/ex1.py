from abc import ABC, abstractmethod
from typing import override

# 1. Tự định nghĩa lỗi (Custom Exception)
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        super().__init__(f"Lỗi: Giá '{gia}' không hợp lệ (phải >= 0)")

# 2. Bộ quản lý bối cảnh (Context Manager) để dùng với 'with'
class KiemTraNghiepVu:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is GiaKhongHopLe:
            print(f"--- [HỆ THỐNG BÁO LỖI]: {exc_val} ---")
            return True # Ngăn chương trình bị sập
        return False

# 3. Lớp cha trừu tượng HangHoa
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.gia = gia # Gọi qua setter để validate

    # Sử dụng @property để thay thế getter/setter kiểu cũ
    @property
    def ma_hang(self): return self.__ma_hang

    @property
    def gia(self): return self.__gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value

    # Phương thức trừu tượng: bắt buộc lớp con phải có
    @abstractmethod
    def loai_hang(self):
        pass

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.__ma_hang} | {self.__ten_hang} | Giá: {self.__gia:,.0f}đ"

    # --- Magic Methods ---
    def __str__(self): # Dùng khi print(object)
        return self.inTTin()

    def __repr__(self): # Dùng cho developer debug
        return f"{self.__class__.__name__}(ma='{self.__ma_hang}', gia={self.__gia})"

    def __eq__(self, other): # So sánh bằng (==) qua mã hàng
        if not isinstance(other, HangHoa): return False
        return self.__ma_hang == other.__ma_hang

    def __lt__(self, other): # So sánh nhỏ hơn (<) qua giá
        return self.__gia < other.__gia

    def __hash__(self): # Để dùng được trong set hoặc dict key
        return hash(self.__ma_hang)

# 4. Lớp con: Hàng Điện Máy
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__bao_hanh = bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    @override
    def loai_hang(self):
        return "Điện máy"

    @override
    def inTTin(self):
        return f"{super().inTTin()} | BH: {self.__bao_hanh}th | {self.__dien_ap}V"

# 5. Lớp con: Hàng Sành Sứ
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__nguyen_lieu = nguyen_lieu

    @override
    def loai_hang(self):
        return "Sành sứ"

    @override
    def inTTin(self):
        return f"{super().inTTin()} | NL: {self.__nguyen_lieu}"

# 6. Lớp con: Hàng Thực Phẩm
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, han_su_dung):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__han_su_dung = han_su_dung

    @override
    def loai_hang(self):
        return "Thực phẩm"

    @override
    def inTTin(self):
        return f"{super().inTTin()} | HSD: {self.__han_su_dung}"

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    # Test Context Manager và Custom Exception
    with KiemTraNghiepVu():
        tivi = HangDienMay("DM001", "Tivi Sony", "Sony", 12500000, 24, 220, 150)
        # Thử tạo lỗi giá âm
        sua_loi = HangThucPham("TP002", "Sữa hỏng", "Vinamilk", -100, "2024", "2025")

    am_chen = HangSanhSu("SS001", "Bộ ấm chén", "Bát Tràng", 850000, "Gốm sứ")

    # Test Magic Methods
    print(tivi) # Chạy __str__
    print(f"Tivi có rẻ hơn ấm chén không? {tivi < am_chen}") # Chạy __lt__