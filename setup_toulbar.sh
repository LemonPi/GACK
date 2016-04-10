#!/bin/sh
# Downloads and installs ToulBar 2 (a Max-CSP solver), which is required for multiple parts of this project.
# Internet access and about 15 MB of disk space is required.
wget "https://mulcyber.toulouse.inra.fr/frs/download.php/1447/toulbar2.0.9.8.0-Release-x86_64.tar.gz"
tar xf toulbar2.0.9.8.0-Release-x86_64.tar.gz
curl "https://mulcyber.toulouse.inra.fr/plugins/scmgit/cgi-bin/gitweb.cgi?p=toulbar2/toulbar2.git;a=blob_plain;f=toulbar2/misc/script/libcp.awk;hb=master" >libcp.awk
curl "https://mulcyber.toulouse.inra.fr/plugins/scmgit/cgi-bin/gitweb.cgi?p=toulbar2/toulbar2.git;a=blob_plain;f=toulbar2/misc/script/cp2wcsp.awk;hb=master" >cp2wcsp.awk
curl "https://mulcyber.toulouse.inra.fr/plugins/scmgit/cgi-bin/gitweb.cgi?p=toulbar2/toulbar2.git;a=blob_plain;f=toulbar2/misc/script/solution2cp.awk;hb=master" >solution2cp.awk
