Summary: NethServer web interface to collectd
Name: nethserver-cgp
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
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

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) /var/www/html/cgp/conf/config.local.php
%doc COPYING

%changelog
* Thu May 26 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Access to graphs and reports from trusted network - Bug #3370 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- First release. Refs #2507

* Mon Dec 23 2013 Filippo Carletti <filippo.carletti@gmail.com> 1.0.0-1
- First release

