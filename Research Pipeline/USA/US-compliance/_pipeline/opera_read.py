# Read a page's visible text through the running Opera (CDP on 9333). Usage: opera_read.py URL [wait_s]
import sys,json,time,urllib.request,websocket
url=sys.argv[1]; wait=float(sys.argv[2]) if len(sys.argv)>2 else 8
req=urllib.request.Request('http://127.0.0.1:9333/json/new?'+url,method='PUT')
tab=json.load(urllib.request.urlopen(req))
time.sleep(wait)
ws=websocket.create_connection(tab['webSocketDebuggerUrl'],timeout=30,suppress_origin=True)
ws.send(json.dumps({'id':1,'method':'Runtime.evaluate','params':{'expression':'[document.title,location.href,document.body.innerText].join(String.fromCharCode(10))','returnByValue':True}}))
while True:
    r=json.loads(ws.recv())
    if r.get('id')==1: break
ws.close()
urllib.request.urlopen('http://127.0.0.1:9333/json/close/'+tab['id'])
sys.stdout.reconfigure(encoding='utf-8')
print(r.get('result',{}).get('result',{}).get('value',r))
