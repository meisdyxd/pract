from datetime import datetime

date_format = "%d.%m.%Y %H:%M"
date1 = "01.01.1970 0:00"
date2 = "01.01.1970 0:00"

# Преобразование строковых значений в объекты datetime
date1_obj = datetime.strptime(date1, date_format)
date2_obj = datetime.strptime(date2, date_format)

# Получение разницы между датами
time_difference = date2_obj - date1_obj

# Получение разницы в часах
hours_difference = time_difference.total_seconds() // 3600

print("Разница между датами в часах:", hours_difference)