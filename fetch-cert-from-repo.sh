#! /bin/sh

# NAMES_FILE=test-names.dat
# TARGET_DIR=test-certs

NAMES_FILE=names.dat
TARGET_DIR=certs

if [ ! -d $TARGET_DIR ] ; then  
    mkdir $TARGET_DIR
fi  

cat $NAMES_FILE | xargs ./ndns-shot -d ${TARGET_DIR}/
