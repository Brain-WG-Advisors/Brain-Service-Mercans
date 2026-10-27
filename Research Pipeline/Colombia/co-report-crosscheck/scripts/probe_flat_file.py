"""Probe a flat text file WITHOUT printing its content: encoding, byte size, line terminator, line count,
line-length distribution and the first two characters of each line (record type), plus their distribution.
Usage: python3 scripts/probe_flat_file.py <file name inside 02-client-reports-raw>"""
import os,sys,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,'02-client-reports-raw',sys.argv[1])
raw=open(p,'rb').read()
try: txt=raw.decode('utf-8'); enc='utf-8'
except UnicodeDecodeError: txt=raw.decode('latin-1'); enc='latin-1'
crlf=raw.count(b'\r\n'); lf=raw.count(b'\n')
lines=txt.split('\r\n') if crlf else txt.split('\n')
if lines and lines[-1]=='': lines=lines[:-1]
print('file:',sys.argv[1],'| encoding:',enc,'| bytes:',len(raw),'| terminator:','CRLF' if crlf else ('LF' if lf else 'none'),'| lines:',len(lines))
print('line-length distribution (chars):',dict(sorted(collections.Counter(len(l) for l in lines).items())))
pref=[l[:2] for l in lines]
print('first-2-chars distribution:',dict(collections.Counter(pref)))
print('first-2-chars sequence:',','.join(pref))
