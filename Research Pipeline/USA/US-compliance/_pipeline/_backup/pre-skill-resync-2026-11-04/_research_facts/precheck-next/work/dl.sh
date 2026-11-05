cd "$1/00-official-sources/precheck-copies"
while IFS=$'\t' read -r id url; do
  ( code=$(curl -sL -m 60 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36" -o "$id.raw" -w "%{http_code} %{content_type}" "$url"); echo "$id $code $(stat -c %s $id.raw 2>/dev/null) $url" ) &
  while [ $(jobs -r | wc -l) -ge 8 ]; do sleep 0.5; done
done < "$1/_research/precheck-next/work/dl.tsv"
wait
