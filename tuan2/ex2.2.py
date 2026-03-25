#Câu 1:
import math
r = 5
the_tich = (4/3) * math.pi * (r**3)
print("Thể tích hình cầu là:", the_tich)
#Câu 2:
gia_bia = 24.95
chiet_khau = 0.4
so_luong = 60
tien_sach = gia_bia * (1 - chiet_khau) * so_luong
tien_ship = 3 + 0.75 * (so_luong - 1)
tong_chi_phi = tien_sach + tien_ship
print(f"Câu 2 - Tổng chi phí cho {so_luong} cuốn là: ${tong_chi_phi:.2f}")
#Câu 3:
# đổi tgian bdau ra giây
bat_dau_giay = (6 * 3600) + (52 * 60)
# đổi v pace ra giây
pace_easy = (8 * 60) + 15 
pace_tempo = (7 * 60) + 12
# Tổng thời gian chạy tính bằng giây
tong_chay_giay = (2 * pace_easy) + (3 * pace_tempo)
ve_nha_giay = bat_dau_giay + tong_chay_giay
# Quy đổi ngược lại thành Giờ, Phút, Giây
gio = ve_nha_giay // 3600
phut = (ve_nha_giay % 3600) // 60
giay = ve_nha_giay % 60
print(f"Thời gian về nhà là: {gio:02d}:{phut:02d}:{giay:02d} AM")
