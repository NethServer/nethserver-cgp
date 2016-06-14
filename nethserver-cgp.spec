Summary: NethServer web interface to collectd
Name: nethserver-cgp
Version: 2.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: https://github.com/pommi/CGP/archive/master.tar.gz
Source2: config.local.php
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: nethserver-collectd, nethserver-httpd
Requires: perl-CGI, perl-RRD-Simple
Requires: nethserver-lib

%description
NethServer web interface to collectd
See: http://pommi.nethuis.nl/category/cgp/

%prep
%setup
mkdir -p root/usr/share/cgp
tar xzvf %{SOURCE1} --strip-components=1 -C root/usr/share/cgp
cp %{SOURCE2} root/usr/share/cgp/conf/config.local.php

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) /usr/share/cgp/conf/config.local.php
%doc COPYING

%changelog
* Tue Jun 14 2016 Davide Principi <davide.principi@nethesis.it> - 2.0.0-1
- CGP: update for Collectd 5 - Enhancement #3404 [NethServer]
- Syntax error in cgp and collectd-web httpd conf - Bug #3402 [NethServer]

* Thu Jun 09 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Syntax error in cgp and collectd-web httpd conf - Bug #3402 [NethServer]

* Thu May 26 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Access to graphs and reports from trusted network - Bug #3370 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- First release. Refs #2507

* Mon Dec 23 2013 Filippo Carletti <filippo.carletti@gmail.com> 1.0.0-1
- First release

