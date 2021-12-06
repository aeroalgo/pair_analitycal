from datetime import datetime


def get_today_date():
    """ Returns current date in dd.mm.yyyy format """
    today_date = datetime.today()
    return today_date.strftime("%d.%m.%Y")
