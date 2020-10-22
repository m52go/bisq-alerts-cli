lfp=`jq .bisqLogFilePath settings.json` && lfpn=${lfp:1:-1}
kbh=`jq .keybaseHandle settings.json` 

tail -fn0 $lfpn | \
while read line ; do
    python3 read.py "$line" $kbh
done
