#yeucau1
class CanBo :  
    def __init__ (self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    
    def loai_cb(self):
        return "Cán Bộ"
    
    def hien_thi_cb(self):
        print(f"[{self.loai_cb()}] | Họ  và tên: {self.ho_ten}")
        print(f" Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} |Địa chỉ {self.dia_chi}")
    
class CongNhan (CanBo):
    def __init__ (self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.__bac = bac
    def loai_cb(self):
        return "Công Nhân"     #method overriding  
    def hien_thi_cb(self):
        super().hien_thi_cb()
        print(f"Bậc: {self.__bac}")

class KySu(CanBo):
    def __init__ (self, ho_ten, tuoi, gioi_tinh, dia_chi, bac, nganh):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.__nganh = nganh
    def loai_cb(self):
        return "Kỹ sư"     #method overriding  
    def hien_thi_cb(self):
        super().hien_thi_cb()
        print(f"Ngành đào tạo: {self.__nganh}")

class NhanVien(CanBo) :
    def __init__ (self, ho_ten, tuoi, gioi_tinh, dia_chi, congviec):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.__congviec = congviec
    def loai_cb(self):
        return "Nhân viên"     #method overriding  
    def hien_thi_cb(self):
        super().hien_thi_cb()
        print(f"Công việc: {self.__congviec}")

cb1 =CanBo ("Trang",19,"Nữ","Gia Lâm")
cb2= CongNhan ("Trâm béo",19,"Nữ","Tây Hồ")
cb3 =KySu ("Trang",19,"Nữ","Gia Lâm",5)
cb4= NhanVien ("Trâm béo",19,"Nữ","Tây Hồ","văn phòng")
cb1.hien_thi_cb()
#yeucau2
class QLCB:
    def __init__(self):
        self.danhsach = []
    def themmoi (self):
        print("Nhập vào 1.Công Nhân/2.Kỹ Sư/3.Nhân Viên")
        loai = input("")
        hoten = input("Nhập vào Họ và Tên:")
        tuoi = input("Nhập vào tuổi:")
        gioitinh = input("Nhập vào giới tính:")
        diachi = input("Nhập vào địa chỉ:")
        
        if loai == "1":
            bac = input("Nhập vào bậc Công Nhân")
            cb = CongNhan(hoten, tuoi, gioitinh, diachi, bac)
        elif loai == "2":
            nganh = input("Nhập vào ngành đào tạo")
            cb = KySu(hoten, tuoi, gioitinh, diachi, nganh)
        elif loai == "3":
            congviec = input ("Nhập vào Công việc")
            cb = NhanVien(hoten, tuoi, gioitinh, diachi, congviec)
        
        self.danhsach.append(cb)

    def timkiem (self):
        ten = input("Nhập vào tên:")
        for item in self.danhsach:
            if item._hoten == ten:
                item.hien_thi()
    def hienthids (self):
        for item in self.danhsach:
            item.hien_thi()
    def chay (self):
        while True:
            print("----- Nhập loại yêu cầu ------")
            print("1.Thêm mới cán bộ")
            print("2.Tìm kiếm cán bộ")
            print("3. Hiện thị danh sách cán bộ")
            print("4.Thoát khỏi chương trình")
            loai = input ("")
            if loai == "1":
                self.themoi()
            elif loai == "2":
                self.timkiem()
            elif loai == "3":
                self.hienthids()
            else:
                loai == "4"
                break
if __name__ == "__main__":
    ql = QLCB()
    ql.chay()