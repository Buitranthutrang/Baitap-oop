# Lớp cha: Hàng Hóa
class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx

    def getMaHang(self):
        return self.__ma_hang
        
    def getTenHang(self):
        return self.__ten_hang
        
    def getNhaSX(self):
        return self.__nha_sx

    def hien_thi(self):
        print(f"Mã hàng: {self.__ma_hang}")
        print(f"Tên hàng: {self.__ten_hang}")
        print(f"Nhà sản xuất: {self.__nha_sx}")
# Lớp con 1: Hàng Điện Máy
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia = gia
        self.__bao_hanh = bao_hanh   
        self.__dien_ap = dien_ap       
        self.__cong_suat = cong_suat     

    def hien_thi(self):
        print("--- THÔNG TIN HÀNG ĐIỆN MÁY ---")
        super().hien_thi()
        print(f"Giá bán: {self.__gia:,.0f} VNĐ")
        print(f"Bảo hành: {self.__bao_hanh} tháng")
        print(f"Điện áp: {self.__dien_ap}V")
        print(f"Công suất: {self.__cong_suat}W")
# Lớp con 2: Hàng Sành Sứ
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia = gia
        self.__nguyen_lieu = nguyen_lieu

    def hien_thi(self):
        print("--- THÔNG TIN HÀNG SÀNH SỨ ---")
        super().hien_thi()
        print(f"Giá bán: {self.__gia:,.0f} VNĐ")
        print(f"Chất liệu: {self.__nguyen_lieu}")
# Lớp con 3: Hàng Thực Phẩm
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, han_su_dung):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.__gia = gia
        self.__ngay_sx = ngay_sx
        self.__han_su_dung = han_su_dung

    def hien_thi(self):
        print("--- THÔNG TIN HÀNG THỰC PHẨM ---")
        super().hien_thi()
        print(f"Giá bán: {self.__gia:,.0f} VNĐ")
        print(f"Ngày sản xuất: {self.__ngay_sx}")
        print(f"Hạn sử dụng: {self.__han_su_dung}")
# Test
tivi = HangDienMay("DM001", "Tivi Sony 55 inch", "Sony", 12500000, 24, 220, 150)
am_chen = HangSanhSu("SS001", "Bộ ấm chén", "Bát Tràng", 850000, "Gốm sứ")
sua = HangThucPham("TP001", "Sữa tươi TH", "TH Group", 45000, "15/04/2026", "15/10/2026")

tivi.hien_thi()
am_chen.hien_thi()
sua.hien_thi()