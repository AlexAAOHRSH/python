import requests

token = "1387500601:AAG1aLzoOY1lv4sstK5yOcvN9aChnaXTMyM"

res = requests.get("https://api.telegram.org/bot1387500601:AAG1aLzoOY1lv4sstK5yOcvN9aChnaXTMyM/getUpdate")

print(res.__dict__)





