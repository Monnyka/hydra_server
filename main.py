import time
import schedule
import shutil
import telebot

bot = telebot.TeleBot('1107438786:AAED_PIcm4FYHNX_zCLJBGDktDVpAvf7g5Q')

# def telegram_bot_sendtext(bot_message):
#     bot_token = '1107438786:AAED_PIcm4FYHNX_zCLJBGDktDVpAvf7g5Q'
#     bot_chatID = '342923927'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#     response = requests.get(send_text)
#     return response.json()

# def report():
#     report_movie="*Report for Hydra Server:* \n\n ~~_MEDIA:_~~\n -New Added Movie:\n     *American Sniper (2020)*\n"
#     #report_tv="-New Added Movie:\n     *Arrow S08E01*\n\n"
#     #report_spacing="~~_DISK USAGE_~~\n -Total: \n      *{}*\n -Use: \n      *{}* \n-Free: \n      *{}\n*".format(report_disk_total, report_disk_used,report_disk_free)
#     #report_title=report_movie+report_tv + report_spacing
#     telegram_bot_sendtext(report_movie)

def stop():
        import os
        os.system("sudo systemctl stop minecraftpeserver.service")
schedule.every().day.at("15:35").do(stop)

# schedule.every().day.at("15:08").do(report)
while True:
    schedule.run_pending()
time.sleep(1)