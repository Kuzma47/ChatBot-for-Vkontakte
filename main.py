import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time
import requests
from vk_api import VkUpload


def send(MSG, ID):
    vk.messages.send(message=MSG, peer_id=ID, random_id=0)
def send_photo():
    attachments = []
    session = requests.Session()
    upload = VkUpload(vk_session)
    image_url = photos[random.randint(0,len(photos)-1)]
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
    vk.messages.send(peer_id=id, attachment=','.join(attachments), random_id=0)
vk_session = vk_api.VkApi(token='06f16e4dd85ac708936265462fdf23f523c230edafd50378fa0db2d21e0e1165cfa1acc11ae8871c574f2')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 153439683)
photos = []#different urls on images in the internet
memb = []
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.message['text']
            if event.from_chat == True:
                if 'everydayporn' in msg or 'порно от андрея (не гейское)' in msg:
                    id = event.message['peer_id']
                    if 'команд' in msg.lower():
                        send('@everydayporn привет - б(анальное) приветствие\n@everydayporn нибучинов - Нибучинов дня\n@everydayporn '
                             'номера - список номеров учатсников беседы\n@everydayporn ты сука? - ...\n@everydayporn порно - В процессе '
                             'создания..', id)
                    elif 'привет' in msg.lower():
                        vk.messages.send(peer_id=id, sticker_id='21', random_id=0)
                    elif 'нибуч' in msg.lower():
                        name = vk_session.method('messages.getConversationMembers', {'peer_id': id})
                        count = name["count"] -3
                        for i in range(count):
                            first_name = name["profiles"][i]["first_name"]
                            last_name = name["profiles"][i]["last_name"]
                            peer_id = name["profiles"][i]["id"]
                            message = "@id" + str(peer_id) + "(" + first_name + " " + last_name + ")"
                            memb.append(message)
                        send('Взламываю данные серверов ВКонтакте...', id)
                        time.sleep(2)
                        send('Обрабатываю полученную информацию...', id)
                        mes = random.choice(memb)
                        time.sleep(2)
                        send(mes+' - Нибучинов дня', id)
                    elif 'номер' in msg.lower():
                        send('+79827352462 - Андрей ', id)
                    elif 'порно' in msg.lower():
                        send_photo()
                    elif 'сука' in msg.lower():
                        send('Ублюдок, мать твою, а ну иди сюда говно собачье, решил ко мне лезть? Ты, засранец вонючий,'
                             ' мать твою, а? Ну иди сюда, попробуй меня трахнуть, я тебя сам трахну ублюдок, онанист чертов,'
                             ' будь ты проклят, иди идиот, трахать тебя и всю семью, говно собачье, жлоб вонючий, дерьмо,'
                             ' сука, падла, иди сюда, мерзавец, негодяй, гад, иди сюда ты - говно, ЖОПА!', id)
                    else:
                        send('Я не знаю такой команды\nВведите @everydayporn команды для полного списка функций', id)