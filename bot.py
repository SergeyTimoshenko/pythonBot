import pyowm
import telebot
bot = telebot.TeleBot("898543409:AAHw13XbqdPUApF14DEYgW2jO6DcfU77Wbg")
owm = pyowm.OWM('50230065b13a7102b3993469b286bd0e', language = "ru")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    try:
        observation = owm.weather_at_place(message.text)
    except:
        bot.send_message(message.chat.id, "Неизвестный город: " + message.text)
        return
    w = observation.get_weather()
    answer = "На улице сейчас " + w.get_detailed_status() + '\n'
    answer = answer + "Температура воздуха: " + str(w.get_temperature('celsius')['temp'])
    
    bot.send_message(message.chat.id, answer)
        
bot.polling()