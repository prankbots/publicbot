# -*- coding: utf-8 -*-
from PRANKBOTS import *
from datetime import datetime
from time import sleep
# EDITOR | ACIL
# VERSION | PYTHON 3
# VORKED | PRANKBOT INDONESIA
#======HARGAI HAK CIPTA| JIKA MERUBAH NAMA BOT SILAHKAN CANTUMKAN NAMA BOT ASALNYA
#=== CONTOH || CREATOR BY. SAPRI || BOT GARANG || SUPORT BY.PRANKBOTS

#TAMBAHAN INSTALL
# tinggal di pastekan aja sob
# apt install python3-pip
# pip3 install bs4 gtts
from bs4 import BeautifulSoup
from gtts import gTTS
import time, random, sys, json, codecs,  threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast
botStart = time.time()
prank = LineClient()
prank.log("Auth Token : " + str(prank.authToken))
channel = LineChannel(prank)
prank.log("Channel Access Token : " + str(channel.channelAccessToken))
prankProfile = prank.getProfile()
prankSettings = prank.getSettings()
prankPoll = LinePoll(prank)
prankMID = prank.profile.mid
contact = prank.getProfile()
backup = prank.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
cl = prank
#=[REVIEW DAFTAR BOT DAN HARGA]

#DAFTAR:_______|_______PERPANJANG:
#=======[SELFBOT ONLY]
#selfbot only                              ~ 50k ||50k

#=======[SELFBOT PROTECT]
#1 selfbot + 2 asist                  ~ 100k || 80k
#1 selfbot + 2 asist + 1 kicker ~ 100k ||100k 
#1 selfbot + 3asist + 2 kicker ~ 150k || 150k
#1 selfbot + 4 asist + 2 kicker ~ 200k || 150k
#1 selfbot + 5 asist + 2 kicker ~ 200k || 200k
#1 selfbot + 6 asist + 2 kicker ~ 250k|| 200k
#1 selfbot + 7 asist + 2 kicker ~ 250k|| 250k
#1 selfbot + 8 asist + 2 kicker ~ 300k || 250k

#=======[SELFBOT PREMIUM]
#2 selfbot + 10 asist + 4 kicker ~ 500k || 450k
#2 selfbot + 12 asist + 4 kicker ~ 500k || 500k
#=================


#=======[PROTECT GRUP]
#👉 BOT PROTECT PER GRUP
#MAXIMAL 2 ADMIN 👉 5 bot~ 50k  per bulan
#MAXIMAL 3 ADMIN 👉 8 bot ~100k per bulan
#MAXIMAL 4 ADMIN 👉 11 bot ~ 150k per bulan

#[[SEMUA SELFBOT SUDAH TERMASUK OWNER BOT PROTECT]]
#== GABUNGAN SELFBOT DENGAN BOT PROTECT ==

#MINAT PM ID  👉     http://line.me/ti/p/~adiputra.95
settings = {
    "autoAdd":False,
    "autoJoin":False,
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = prankProfile.displayName
myProfile["statusMessage"] = prankProfile.statusMessage
myProfile["pictureStatus"] = prankProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = prank.getProfile().mid
    if myid in nm:    
        nm.remove(myid)
    for mm in nm:
        akh = akh + 6
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 7
        akh = akh + 1
        bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
    try:
        prank.sendMessage(msg.to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)
#===============SB ONLY====================
#===================================#
def help():
    helpMessage = "╭━━╦℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́╦в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╦━━╮\n┣╦━━━╩PUBLIC BOTS╩━━━━" + "\n" + \
                  "┣╦Nama Bot╦ " + prankProfile.displayName + "\n" + \
                  "┣╦Help" + "\n" + \
                  "┣╦Set" + "\n" + \
                  "┣╦Me" + "\n" + \
                  "┣╦Add" + "\n" + \
                  "┣╦Creator" + "\n" + \
                  "┣╦Restart" + "\n" + \
                  "┣╦Speed" + "\n" + \
                  "┣╦Runtime" + "\n" + \
                  "┣╦Mymid" + "\n" + \
                  "┣╦Myname" + "\n" + \
                  "┣╦Mybio" + "\n" + \
                  "┣╦Mypicture" + "\n" + \
                  "┣╦Myvideo" + "\n" + \
                  "┣╦Mycover" + "\n" + \
                  "┣╦Getmid @" + "\n" + \
                  "┣╦Getbio @" + "\n" + \
                  "┣╦Getname @" + "\n" + \
                  "┣╦Getpicture @" + "\n" + \
                  "┣╦Getvideo @" + "\n" + \
                  "┣╦Getcontact @" + "\n" + \
                  "┣╦Getcover @" + "\n" + \
                  "┣╦Getprofile @" + "\n" + \
                  "┣━━━━━━━━━━━━" + "\n" + \
                  "┣╦Cloneprofile @" + "\n" + \
                  "┣╦Restoreprofile" + "\n" + \
                  "┣╦Cekmid *mid" + "\n" + \
                  "┣╦Friendlist" + "\n" + \
                  "┣╦Blocklist" + "\n" + \
                  "┣╦Mention" + "\n" + \
                  "┣╦Lurk:on" + "\n" + \
                  "┣╦Lurk:off" + "\n" + \
                  "┣╦Lurk:rest" + "\n" + \
                  "┣╦Lurkers" + "\n" + \
                  "┣━━━━━╩━━━╩━━━━━\n┣━╦🇮🇩CREATOR INDONESIA🇮🇩╦━╣\n╰━━╩℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к╩̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╩━━╯"
    return helpMessage
while True:
    try:
        ops=prankPoll.singleTrace(count=50)
        
        for op in ops:
            if op.type == 5:
                prank.findAndAddContactsByMid(op.param1)
                xname = prank.getContact(op.param1).displayName
                prank.sendMessage(op.param1, "Hay " + xname + "\nBOT PUBLIC VORKED : PRANKBOTS\n\nOWNER BOTS\nhttp://line.me/ti/p/~adiputra.95")
            if op.type == 13:
                print ("[NOTIFIED_INVITE_INTO_GROUP]")
                if prankMID in op.param3:
                    G = prank.getGroup(op.param1)
                    prank.acceptGroupInvitation(op.param1)
            if op.type == 26: ## JIKA INI DI GANTI KE 25 JADI SELFBOT ONLY ^_^ [VORKED PRANKBOTS]
                print ("[ 26 ] READ MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            prank.sendChatChecked(receiver, msg_id)
                            contact = prank.getContact(sender)
                            if text.lower() == "help":
                               helpMessage = help()
                               prank.sendMessage(msg.to, str(helpMessage))
                               prank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            if text.lower() == 'speed':
                                start = time.time()
                                prank.sendMessage(receiver, "waitting..")
                                elapsed_time = time.time() - start
                                prank.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif text.lower() == 'restart':
                                prank.sendMessage(msg.to, "Bot Program has been restarted")
                                restartBot()
                            elif text.lower() == 'runtime':
                            	eltime = time.time() - botStart
                            	timerun = "Bot has been active "+waktu(eltime)
                            	prank.sendMessage(msg.to,timerun)
#==============================================================================#
                            elif text.lower() == 'me':
                                prank.sendContact(msg.to, prankMID)
                                prank.sendMessage(msg.to,"Ini kontak saya")
                                prank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                prank.sendMessage(msg.to,"Ini kontak kamu")
                            elif text.lower() == 'add':		
                                prank.sendMessage(msg.to,"❂•••••••••✧••••••••••❂")
                                prank.sendMessage(receiver, None, contentMetadata={'mid': 'u5818cb4404411c2e2e6e6937d172cca8'}, contentType=13)
                                prank.sendMessage(receiver, None, contentMetadata={'mid': 'udfaf52176415b46cb445ae2757ec85f3'}, contentType=13)
                                prank.sendMessage(receiver, None, contentMetadata={'mid': 'u17a086ccff618e754588a1108335867f'}, contentType=13)
                                prank.sendMessage(msg.to,"❂•••••••••✧••••••••••❂")
                            elif text.lower() == 'creator':		
                                prank.sendMessage(msg.to,"❂•••••••••✧••••••••••❂")
                                prank.sendMessage(receiver, None, contentMetadata={'mid': 'u961be7189409ffd9138c7206e35003b0'}, contentType=13)
                                prank.sendMessage(msg.to,"❂•••••••••✧••••••••••❂")
                            elif text.lower() == 'mymid':
                                prank.sendMessage(msg.to, sender)
                                prank.sendMessage(msg.to,"Ini mid kamu")
                            elif text.lower() == 'myname':
                                me = prank.getContact(prankMID)
                                me1 = prank.getContact(sender)
                                prank.sendMessage(msg.to,"nama ku\n" + me.displayName + "\nnama kamu\n" + me1.displayName)
                            elif text.lower() == 'mybio':
                                me = prank.getContact(sender)
                                prank.sendMessage(msg.to,"[Status kamu]\n" + me.statusMessage)
                            elif text.lower() == 'mypicture':
                                h = prank.getContact(prankMID)
                                path = "http://dl.profile.line.naver.jp/" + h.pictureStatus
                                prank.sendImageWithURL(msg.to, str(path))
                                prank.sendMessage(msg.to,"Ini foto profile saya")
                                me1 = prank.getContact(sender)
                                path = "http://dl.profile.line-cdn.net/" + me1.pictureStatus
                                prank.sendImageWithURL(msg.to, str(path))
                                prank.sendMessage(msg.to,"Ini foto profile kamu")
                            elif text.lower() == 'myvideo':
                                me = prank.getContact(sender)
                                prank.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = prank.getContact(prankMID)
                                cover = channel.getProfileCoverURL(prankMID)    
                                prank.sendImageWithURL(msg.to, cover)
                                prank.sendMessage(msg.to,"Ini foto branda saya")
                                me1 = prank.getContact(sender)
                                cover1 = channel.getProfileCoverURL(sender)    
                                prank.sendImageWithURL(msg.to, cover1)
                                prank.sendMessage(msg.to,"Ini foto branda kamu")
                            elif 'getmid' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}" + ls
                                    prank.sendMessage(msg.to, str(ret_))
                            elif 'getpicture' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line.naver.jp/" + prank.getContact(ls).pictureStatus
                                        prank.sendImageWithURL(msg.to, str(path))
                            elif 'getcover' in text.lower():
                                if channel != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = channel.getProfileCoverURL(ls)
                                            prank.sendImageWithURL(msg.to, str(path))
                            elif 'getname' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = prank.getContact(ls)
                                        prank.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            elif 'getbio' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = prank.getContact(ls)
                                        prank.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            elif 'getprofile' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = prank.getContact(ls)
                                        cu = channel.getProfileCoverURL(ls)
                                        path = str(cu)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        prank.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                        prank.sendImageWithURL(msg.to,image)
                                        prank.sendImageWithURL(msg.to,path)
                            elif 'getcontact' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = prank.getContact(ls)
                                        mi_d = contact.mid
                                        prank.sendContact(msg.to, mi_d)
                            elif 'cloneprofile' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        prank.cloneContactProfile(contact)
                                        prank.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        prank.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    prank.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    prank.updateProfile(clientProfile)
                                    prank.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    prank.sendMessage(msg.to, "Gagal restore profile")
                            elif 'cekmid' in text.lower():
                                separate = text.split(" ")
                                saya = text.replace(separate[0] + " ","")
                                prank.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)
                                
                            elif text.lower() == 'friendlist':
                                contactlist = prank.getAllContactIds()
                                kontak = prank.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                prank.sendMessage(msg.to, msgs)
                                
                            elif text.lower() == 'blocklist':
                                blockedlist = prank.getBlockedContactIds()
                                kontak = prank.getContacts(blockedlist)
                                num=1
                                msgs="═════════List Blocked═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                                prank.sendMessage(msg.to, msgs)
                            elif text.lower() == 'mention':
                                group = prank.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    mention(msg.to, nm5)             
                                prank.sendMessage(receiver, "Members :"+str(jml))
                            elif text.lower() == 'lurk:on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            prank.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        prank.sendMessage(msg.to, "Set reading point:\n" + readTime)
                                        
                            elif text.lower() == 'lurk:off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    prank.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    prank.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                
                            elif text.lower() == 'lurk:rest':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    prank.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    prank.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif text.lower() == 'lurkers':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        prank.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = prank.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        prank.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    prank.sendMessage(receiver,"Lurking has not been set.")
                except Exception as e:
                    prank.log("[SEND_MESSAGE] ERROR : " + str(e))
                    
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass
            prankPoll.setRevision(op.revision)
            
    except Exception as e:
        prank.log("[SINGLE_TRACE] ERROR : " + str(e))
