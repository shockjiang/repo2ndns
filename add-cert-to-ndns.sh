#! /bin/sh

# SRC_DIR=test-certs

SRC_DIR=certs

Zone=""

function getZone() {
  line=$1
  OLD_IFS="$IFS"
  IFS="."
  arr=($line)
  IFS="$OLD_IFS"

  Zone=""
  count=0
  while [ "x${arr[count]}" != "xKEY" ]
  do
      Zone="${Zone}/${arr[count]}"
      count=$(( $count + 1 ))
  done
}

for fpath in ${SRC_DIR}/* ; do
    fname=${fpath#*/}
    getZone "${fname}"
    echo "insert cert ${fname} to zone ${Zone}"
    ./ndns-add-rr-from-file ${Zone} -p ${fpath}
done
