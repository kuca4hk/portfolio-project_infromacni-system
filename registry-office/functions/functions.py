def time_format(time):
    if time == "" or time is None:
        return ""
    else:
        t = time.strftime("%d.%m.%Y")
        return t


def date_convert(date):
    month = date.month
    if month <= 8:
        return date.strftime("%Yaa")
    else:
        return date.strftime("%Ybb")
