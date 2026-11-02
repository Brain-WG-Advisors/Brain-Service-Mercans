#!/bin/sh
# usage: pg.sh file page [grep]
awk -v p="--- p.$2 ---" -v q="--- p.$(($2+1)) ---" '$0==p{f=1} $0==q{f=0} f' "$1" | grep -v '^\s*$' | ( [ -n "$3" ] && grep -i -B3 -A6 "$3" || cat )
