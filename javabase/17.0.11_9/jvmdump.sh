set -x
filename=$(hostname)-$(date +"%Y%m%d%H%M%S").bin
jmap -dump:live,format=b,file=$filename $1
tar zcf $filename.tgz $filename