import json

class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def to_dict(self): 
        return {
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "loai": self.__class__.__name__, # Lưu lại tên Class để sau này biết đường phục hồi
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ho_ten"], 
            d["tuoi"],
            d["gioi_tinh"], 
            d["dia_chi"]
        )
    def __str__(self):
        return f"{self.__class__.__name__} - {self.ho_ten}, {self.tuoi} tuổi, Địa chỉ: {self.dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def to_dict(self):
        d = super().to_dict() 
        d["bac"] = self.bac  
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["bac"])


danh_sach = [
    CanBo("Nguyễn An", 30, "Nam", "Hà Nội"),
    CongNhan("Trần Bình", 25, "Nam", "TP.HCM", 5),
]
data = [cb.to_dict() for cb in danh_sach]
#save
with open("canbo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
#dl
with open("canbo.json", "r", encoding="utf-8") as f:
    raw = json.load(f)
#Khôi phục đúng loại theo "loại"
ds_load = [CanBo.from_dict(d) for d in raw]
for cb in ds_load:
    print(cb)