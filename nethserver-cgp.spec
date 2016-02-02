Summary: NethServer web interface to collectd
Name: nethserver-cgp
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
Source1: https://github.com/pommi/CGP/archive/master.tar.gz
Source2: config.local.php
Patch0:  header-color.patch
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: nethserver-collectd, nethserver-httpd
Requires: nethserver-lib

%description
NethServer web interface to collectd
See: http://pommi.nethuis.nl/category/cgp/

%prep
%setup
mkdir -p root/usr/share/cgp
tar xzvf %{SOURCE1} --strip-components=1 -C root/usr/share/cgp
cp %{SOURCE2} root/usr/share/cgp/conf/config.local.php
find
patch -p0 <  %{PATCH0}

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
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Dec 29 2015 Filippo Carletti <filippo.carletti@gmail.com> - 1.2.0-1
- Update to latest cgp from github.

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- First release. Refs #2507

* Mon Dec 23 2013 Filippo Carletti <filippo.carletti@gmail.com> 1.0.0-1
- First release

