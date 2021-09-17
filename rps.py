from utlis.rank import setrank,isrank,remrank,remsudos,setsudo, GPranks,IDrank
from utlis.send import send_msg, BYusers, GetLink,Name,Glang
from utlis.locks import st,getOR
from utlis.tg import Bot
from config import *

from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random, re, json
import importlib

from uuid import uuid4

from pyrogram import (
     InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
)

ANSWERS = ['ROCK', 'PAPER', 'SCISSORS']
def get_winner(first, second):
    first_index = ANSWERS.index(first.upper())
    second_index = ANSWERS.index(second.upper())
    diff = first_index - second_index
    mod = diff % 5
    if mod in [1, 3]:
        return 0
    elif mod in [2, 4]:
        return 1
    return "tie"


def emj(ch1):
  if ch1 == "ROCK":
    return "ًں§±"
  if ch1 == "PAPER":
    return "ًں“ƒ"
  if ch1 == "SCISSORS":
    return "âœ‚ï¸ڈ"
def updateMsgs(client, message,redis):
  pass


def updateCb(client, callback_query,redis):
  if callback_query.inline_message_id:
    return False
  date = callback_query.data
  userID = callback_query.from_user.id
  userFN = callback_query.from_user.first_name
  username = callback_query.from_user.username
  chatID = callback_query.message.chat.id
  message_id = callback_query.message.message_id
  if re.search("^rps.pyplay$",date):
    start = """âœ‚ï¸ڈê’گ ط­ط¬ط±ظ‡ ظˆط±ظ‚ظ‡ ظ…ظ‚طµ
ًں‘¤ê’گ ط§ط¶ط؛ط· ظ„ظ„ط¹ط¨ ظ…ط¹ ({})""".format(userFN)
    kb = InlineKeyboardMarkup([[InlineKeyboardButton("ط§ظ„ط¹ط¨", callback_data="rps="+str(userID))]])
    Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":start,"disable_web_page_preview":True,"reply_markup":kb})

  if re.search("rer=",date):
    tx = callback_query.message.text
    p1 = date.split("=")[1]
    if userID == int(p1):
      start = """âœ‚ï¸ڈê’گ ط­ط¬ط±ظ‡ ظˆط±ظ‚ظ‡ ظ…ظ‚طµ
ًں‘¤ê’گ ط§ط¶ط؛ط· ظ„ظ„ط¹ط¨ ظ…ط¹ ({})""".format(userFN)
      kb = InlineKeyboardMarkup([[InlineKeyboardButton("ط§ظ„ط¹ط¨", callback_data="rps="+str(userID))]])
      Bot("sendMessage",{"chat_id":chatID,"text":start,"disable_web_page_preview":True,"reply_markup":kb})
      Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":tx,"disable_web_page_preview":True})
    else:
      Bot("answerCallbackQuery",{"callback_query_id":callback_query.id,"text":"ط¹ط°ط±ط§ظ‹ ط§ظ„ظ„ط¹ط¨ظ‡ ظ„ظٹط³طھ ظ„ظƒ","show_alert":True})


  go = """{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط§ظˆظ„ :- ({})
{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط«ط§ظ†ظٹ :- ({})
ًں”½ê’گ ط§ط®طھط± ظ…ط§ طھط±ظٹط¯ ({})"""
  go2 = """{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط§ظˆظ„ :- ({})
{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط«ط§ظ†ظٹ :- ({})
ًںژٹê’گ ط§ظ„ظپط§ط¦ط² ({})"""

  go3 = """{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط§ظˆظ„ :- ({})
{}ê’گ ط§ظ„ظ„ط§ط¹ط¨ ط§ظ„ط«ط§ظ†ظٹ :- ({})
ًں”´ê’گ طھط¹ط§ط¯ظ„"""

  if re.search("st1=",date):
    ex = date.split("=")
    user1 = ex[1]
    user2 = ex[2]
    chs = ex[3]
    try:
      getUser = client.get_users(int(user2))
      userId = getUser.id
      userFn = getUser.first_name
    except Exception as e:
      userFn = user2
    if userID != int(user1):
      Bot("answerCallbackQuery",{"callback_query_id":callback_query.id,"text":"ط§ظ†طھط¸ط± ط¯ظˆط±ظƒ","show_alert":True})
      return False
    ch = ANSWERS[int(chs)]
    kb = InlineKeyboardMarkup([
      [InlineKeyboardButton("ًں§±",callback_data="st2={}={}=0={}".format(user1,user2,chs)),
      InlineKeyboardButton("ًں“ƒ",callback_data="st2={}={}=1={}".format(user1,user2,chs)),
      InlineKeyboardButton("âœ‚ï¸ڈ",callback_data="st2={}={}=2={}".format(user1,user2,chs)),],

      [InlineKeyboardButton("ًں“£",url="t.me/calmaacc")]
      ])
    Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":go.format("âœ…",userFN,"âڈ؛",userFn, userFn),"disable_web_page_preview":True,"reply_markup":kb})

  if re.search("st2=",date):
    ex = date.split("=")
    user1 = ex[1]
    user2 = ex[2]
    chs2 = ex[3]
    chs1 = ex[4]
    try:
      getUser = client.get_users(int(user1))
      userFn = getUser.first_name
    except Exception as e:
      userFn = user1
    if userID != int(user2):
      Bot("answerCallbackQuery",{"callback_query_id":callback_query.id,"text":"ط§ظ†طھط¸ط± ط¯ظˆط±ظƒ","show_alert":True})
      return False
    ch1 = ANSWERS[int(chs1)]
    ch2 = ANSWERS[int(chs2)]
    pe = [user1,user2]
    winer = get_winner(ch1, ch2)
    if winer != "tie":
      if int(pe[winer]) == int(user2):
        us = userFN
        usin = user2
      elif int(pe[winer]) == int(user1):
        us = userFn
        usin = user1
      redis.hincrby("{}Nbot:{}:points".format(BOT_ID,chatID),usin,5)
      kb = InlineKeyboardMarkup([[InlineKeyboardButton("ط§ظ„ظ„ط¹ط¨ ظ…ط¬ط¯ط¯ط§ظ‹",callback_data="rer={}".format(user1))]])
      Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":go2.format(emj(ch1),userFn,emj(ch2),userFN, us),"disable_web_page_preview":True,"reply_markup":kb})

    elif winer == "tie":
      redis.hincrby("{}Nbot:{}:points".format(BOT_ID,chatID),user1,2)
      redis.hincrby("{}Nbot:{}:points".format(BOT_ID,chatID),user2,2)
      kb = InlineKeyboardMarkup([[InlineKeyboardButton("ط§ظ„ظ„ط¹ط¨ ظ…ط¬ط¯ط¯ط§ظ‹",callback_data="rer={}".format(user1))]])
      Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":go3.format(emj(ch1),userFn,emj(ch2),userFN),"disable_web_page_preview":True,"reply_markup":kb})



  if re.search("rps=",date):
    userid = date.split("=")[1]
    if userID == int(userid):
      Bot("answerCallbackQuery",{"callback_query_id":callback_query.id,"text":"ط§ظ†طھ ظ…ظ† ط¨ط¯ط£طھ ط§ظ„ظ„ط¹ط¨ظ‡ ط§ظ†طھط¸ط± ط§ط­ط¯ ط§طµط¯ظ‚ط§ط¦ظƒ","show_alert":True})
      return False
    try:
      getUser = client.get_users(userid)
      userId = getUser.id
      userFn = getUser.first_name
    except Exception as e:
      userFn = userid
    kb = InlineKeyboardMarkup([
      [InlineKeyboardButton("ًں§±",callback_data="st1={}={}=0".format(userid,userID)),
      InlineKeyboardButton("ًں“ƒ",callback_data="st1={}={}=1".format(userid,userID)),
      InlineKeyboardButton("âœ‚ï¸ڈ",callback_data="st1={}={}=2".format(userid,userID)),],

      [InlineKeyboardButton("ًں“£",url="t.me/calmaacc")]
      ])

    Bot("editMessageText",{"chat_id":chatID,"message_id":message_id,"text":go.format("âڈ؛",userFn,"âڈ؛",userFN, userFn),"disable_web_page_preview":True,"reply_markup":kb})


  
