def calcular_tempo(total_minutes):
    days = total_minutes // (24 * 60)
    hours = (total_minutes // 60) % 24
    minutes = total_minutes % 60
    return days, hours, minutes