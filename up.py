# -*- coding: utf8 -*-
import requests as r
import json,os,sys,time
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
def main():
 try:
  os.system("clear")
  print """%s
   ____           ___  ___  %sAuthor by abilseno11%s
  /  _/_ _  ___ _/ _ )/ _ ) %sGithub github.com/AbilSeno%s
 _/ //  ' \/ _ `/ _  / _  | %sTeam anoncybfakeplayer%s
/___/_/_/_/\_, /____/____/  %sImgBB Image Uploader
          /___/               """%(qu,pu,qu,pu,qu,pu,qu,qu)
  file = raw_input("%s[%s?%s] %sFile : "%(pu,me,pu,pu))
  with open("%s"%file, "rb") as f:
      data = f.read()
      t = data.encode("base64")
  h = json.loads(r.post("https://api.imgbb.com/1/upload?expiration=600&key=3cf5868d3e9fb6d9596d51b9660ecf99",data={'image':t}).text)["data"]["url"]
  print "%s[%s!%s] %sOk, success upload to %s%s"%(pu,me,pu,pu,ku,h)
  ulg = raw_input("%s[%s?%s] %sRepeat %s[%sy%s/%sn%s] ? "%(pu,me,pu,pu,pu,hi,pu,me,pu))
  if (ulg == "y") or (ulg == "Y"):
   main()
  else:
   exit("%s[%s!%s] %sYahh, masa udahan sih "%(pu,me,pu,pu))
 except r.exceptions.ConnectionError:
   print "%s[%s!%s] %sKoneksi error!!!"%(pu,me,pu,pu)
 except KeyboardInterrupt:
   print "%s[%s!%s] %sBye, selamat tinggall"%(pu,me,pu,pu)
 except IOError:
   print "%s[%s!%s] %sFile %s%s %sdo not exist!!!"%(pu,me,pu,me,ku,file,pu)
   time.sleep(2)
   main()
main()
