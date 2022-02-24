import telebot
import requests
API_KEY='5211168652:AAHgO41Z4FNIEF08R7z1XSaMvn9plZlxXH8'
log_in_url="http://103.112.27.37:8282/CampusPortalSOA/login"
result="http://103.112.27.37:8282/CampusPortalSOA/stdrst"
HEADERS = {"Content-Type": "application/json"}
class student:
    payload={
    'username': "",
    'password': "",
    'MemberType': "S"
    }
    cookies=""
    def __init__(self,regno,password):
        self.payload['username']=str(regno)
        self.payload['password']=str(password)
        self.regno=regno
        self.password=password
        r=requests.post(log_in_url,data=str(self.payload),headers=HEADERS)
        self.data=r.json()
        if(self.data['status']=="success"):
            self.cookies=r.cookies
            print(self.data['message'])
        else:
            print(self.data['message'])
    def getname(self):
        return (self.data['name'])
    def get_result(self):
        payload = "{}"
        response = requests.post(
            result,
            data=str({}),
            headers=HEADERS,
            cookies=self.cookies)
        data=response.json()
        dic=[]
        lis=[]
        for i in data['data']:
            st='sem_number='+str(i['stynumber'])+' sgpa='+str(i['sgpaR'])
            lis.append(st)
            st=""
        return lis
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['result'])
def greet(message):
  text=message.text.split()
  regno=text[1]
  pas=text[-1]
  s=student(regno,pas)
  lis=s.get_result()
  bot.send_message(message.chat.id,s.getname())
  for i in lis:
    bot.send_message(message.chat.id,i)
bot.polling()
