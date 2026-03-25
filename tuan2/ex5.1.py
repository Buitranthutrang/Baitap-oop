import time
# Lấy tổng số giây từ epoch
total_secs = int(time.time())
# Tính số ngày (1 ngày = 24 * 60 * 60 = 86400 giây)
days = total_secs // 86400
# Tính số giây lẻ của ngày hôm nay
secs_today = total_secs % 86400
hours = secs_today // 3600
minutes = (secs_today % 3600) // 60
seconds = secs_today % 60
print(f"Số ngày kể từ Epoch: {days} ngày")
print(f"Giờ hiện tại (GMT): {hours:02d}:{minutes:02d}:{seconds:02d}")