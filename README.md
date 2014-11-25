This subproject is used to transfer existing certificate in Repo-ng to NDNS. The parent project is NDNS: https://github.com/named-data/ndns

 - names.dat: list all the names of certificate that to be transfer
 - name-shot: send Interest to fetch certficates from repo-ng. Source File: https://github.com/shockjiang/ndns/blob/deploy/tools/ndns-shot.cpp
 - fetch-cert-from-repo.sh: a shell script wrapper which gets input from names.dat and call name-shot to fetch all the certificates and save them on filesystem
 - ndns-add-rr-from-file: add a RR to ndns from a local file . Source File: https://github.com/shockjiang/ndns/blob/deploy/tools/ndns-add-rr-from-file.cpp
 - add-cert-to-ndns.sh: a shell script wrapper which add certificates on filesystem to ndns. ndns-add-rr-from-file is called. sudo may be needed


Author:
    [Xiaoke Jiang](http:://netarchlab.tsinghua.edu.cn/~shock/)
