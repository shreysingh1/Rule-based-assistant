from database import *
from time_details import get_time, get_date
from internet import internet_conn, check_on_internet
from webtask import *
from news import get_news
import assistant_details
from weather import get_weather
from system_task import *


def process(query):
    ans = get_ans(query)
    if ans == 'get time details':
        return "Time is" + get_time()
    elif ans == "check internet connection":
        if internet_conn():
            return "Internet is connected"
        else:
            return "Internet is not connected"
    elif ans == "tell date":
        return "Date is " + get_date()

    elif ans == "on speak":
        return speak_on()
    elif ans == "off speak":
        return speak_off()

    elif ans == "speech on":
        return speech_on()
    elif ans == "speech off":
        return speech_off()

    elif ans == "open facebook":
        open_facebook()
        return "opening facebook"
    elif ans == "google":
        search_google()
        return "opening google"
    elif ans == 'youtube':
        search_youtube()
        return "Opening youtube"
    elif ans == "open google":
        open_google()
        return "Opening google"
    elif ans == "open youtube":
        open_youtube()
        return "Opening Youtube"
    elif ans == "get directions":
        return get_directions()
    elif ans == "open map":
        # maps()
        temp1 = maps()
        return "Opening map of " + temp1
    elif ans == "email":
        sendEmail()
        return "Email sent successfuly"

    elif ans == "alarm":
        return set_alarm()
    elif ans == "change wallpaper":
        return wallpaper()
    elif ans == "get news":
        return get_news()
    elif ans == "get weather":
        return get_weather()

    elif ans == "excel":
        return excel()
    elif ans == "powerpoint":
        return powerpoint()
    elif ans == "word":
        return word()
    elif ans == "shell":
        return shell()
    elif ans == "vs code":
        return vs_code()
    elif ans == "closing excel":
        return close_excel()
    elif ans == "closing powerpoint":
        return close_powerpoint()
    elif ans == "closing word":
        return close_word()
    elif ans == "closing shell":
        return close_shell()
    elif ans == "closing vs code":
        return close_vs_code()
    elif ans == 'close browser':
        return close_browser()
    elif ans == "sleep":
        output("Okay sir takecare till then")
        return exit(0)


    elif ans == "change name":
        output("Okay what do you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "I think you're happy with my old name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return f'hello sir iam {assistant_details.name} how can i help you'
    else:
        output("Dont know this one should i search over internet?")
        answer = take_input()
        if 'yes' in answer:
            ans = check_on_internet(query)
            if ans != "":
                return ans
        else:
            output("can you tell me what it means")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()
                value = get_ans(ans)
                if value == "":
                    return "Can't help with this one"
                else:
                    insert_qsn_ans(query, value)
                    return "Okay now i'll remember this for the next time"
            else:
                return "Can't help with this one"
