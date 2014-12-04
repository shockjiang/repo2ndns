This subproject is used to transfer existing certificate in Repo-ng to NDNS. The parent project is NDNS: https://github.com/named-data/ndns

 - names.dat: list all the names of certificate that to be transfer
 - add-cert-to-ndns.py: script to fetch certificates from repo and import them to ndns using ndns-add-rr-from-file. Note that existing records
   will be removed and the latest version of the record from names.dat will be inserted

Author:
  -  [Xiaoke Jiang](http:://netarchlab.tsinghua.edu.cn/~shock/)

  - [Alexander Afanasyev](http://lasr.cs.ucla.edu/afanasyev/index.html)
