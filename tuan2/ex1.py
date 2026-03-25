# Câu 1:
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print("Tổng số giây:", total_seconds)
# Câu 2: 
km = 10
miles = km / 1.61
print("Quãng đường tính bằng dặm:", miles)
# Câu 3: 
# 1. Tính Average Speed 
total_hours = total_seconds / 3600 
average_speed = miles / total_hours
print("Average speed:", average_speed, "miles per hour")
# 2. Tính Average Pace 
total_minutes = total_seconds / 60 
average_pace = total_minutes / miles
print("Average pace:", average_pace, "minutes per mile")