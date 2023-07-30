from time_details import get_hour, get_date
from output_module import output
from database import update_prev_date, get_prev_date


def wishme():
    # fetch prev date
    prev_date = get_prev_date()

    # fetch today's date
    today_date = get_date()
    update_prev_date(today_date)
    hour = int(get_hour())

    if prev_date == today_date:
        output("Glad to Help you again sir tell me how can i help you..")
    else:
        if hour >= 1 and hour <= 12:
            output("Good Morning sir how can i help you")
        elif hour >= 12 and hour <= 16:
            output("Good afternoon sir how can i help you")
        else:
            output("Good evening sir how can i help you")
