import sys
import os

import requests


try:
	url = str(sys.argv[2])
	method = str(sys.argv[1])
except:
	os.system('clear')
	print "Exemple"
	print 'Use: python '+str(sys.argv[0])+" --GET https://www.sitevuln.com/?index=\nor\npython "+str(sys.argv[0])+" --POST https://www.sitevuln.com/ -p username\n\n--GET    for GET attack\n--POST   for POST attack\n\n-p       define Parameter"
	exit(0)

def get(url):
	payloads = open('xss.txt', 'r')
	p_xss = payloads.readlines()

	for xss in p_xss:
		try:
			r = requests.get(url+xss)
			if xss in r.text:
				sys.stdout.write("Payload found: "+str(xss))
			else:
				None
		except:
			None
	print 'Done.'


def post(url):
	None

if method == '--GET':
	os.system('clear')
	print "    )  (    (         (                      )  \n ( /(  )\ ) )\ )      )\ )   (     (      ( /(   \n )\())(()/((()/(     (()/(   )\    )\     )\()) \n((_)\  /(_))/(_))     /(_))(((_)((((_)(  ((_)\  \n__((_)(_)) (_))      (_))  )\___ )\ _ )\  _((_) \n\ \/ // __|/ __|     / __|((/ __|(_)_\(_)| \| | \n >  < \__ \\\__ \     \__ \ | (__  / _ \  | .` | \n/_/\_\|___/|___/_____|___/  \___|/_/ \_\ |_|\_| \n               |_____|" 
	print "\n[!] Method GET enabled"
	print "[!] URL: "+url
	get(url)

if method == '--POST':
	os.system('clear')
	print "    )  (    (         (                      )  \n ( /(  )\ ) )\ )      )\ )   (     (      ( /(   \n )\())(()/((()/(     (()/(   )\    )\     )\()) \n((_)\  /(_))/(_))     /(_))(((_)((((_)(  ((_)\  \n__((_)(_)) (_))      (_))  )\___ )\ _ )\  _((_) \n\ \/ // __|/ __|     / __|((/ __|(_)_\(_)| \| | \n >  < \__ \\\__ \     \__ \ | (__  / _ \  | .` | \n/_/\_\|___/|___/_____|___/  \___|/_/ \_\ |_|\_| \n               |_____|" 
        print "\n[!] Method POST is not avaliable"
	exit(0)
