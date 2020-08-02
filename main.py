import time
import schedule
import requests
import shutil
import telebot

# total, used, free = shutil.disk_usage("d:/")
# report_disk_total="Total: %d GB" % (total // (2**30))
# report_disk_used="Used: %d GB" % (used // (2**30))
# report_disk_free="Free: %d GB" % (free // (2**30))
bot = telebot.TeleBot('1107438786:AAED_PIcm4FYHNX_zCLJBGDktDVpAvf7g5Q')

def telegram_bot_sendtext(bot_message):
    bot_token = '1107438786:AAED_PIcm4FYHNX_zCLJBGDktDVpAvf7g5Q'
    bot_chatID = '342923927'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def report():
    report_movie="*Report for Hydra Server:* \n\n ~~_MEDIA:_~~\n -New Added Movie:\n     *American Sniper (2020)*\n"
    #report_tv="-New Added Movie:\n     *Arrow S08E01*\n\n"
    #report_spacing="~~_DISK USAGE_~~\n -Total: \n      *{}*\n -Use: \n      *{}* \n-Free: \n      *{}\n*".format(report_disk_total, report_disk_used,report_disk_free)
    #report_title=report_movie+report_tv + report_spacing
    telegram_bot_sendtext(report_movie)

schedule.every().day.at("12:04").do(report)
while True:
    schedule.run_pending()
time.sleep(1)