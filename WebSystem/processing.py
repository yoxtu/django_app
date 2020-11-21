def CalcPay(Hourly_wage,hour,minute,magnification = 1):
    result = int(hour) + int(minute) / 60
    return int(Hourly_wage) * result * magnification