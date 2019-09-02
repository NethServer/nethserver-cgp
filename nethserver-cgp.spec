Summary: NethServer web interface to collectd
Name: nethserver-cgp
Version: 2.1.4
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
patch -p0 <  %{PATCH0}

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%config(noreplace) /usr/share/cgp/conf/config.local.php
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Jul 09 2019 Davide Principi <davide.principi@nethesis.it> - 2.1.4-1
- Cockpit legacy apps implementation - NethServer/dev#5782

* Thu Jul 27 2017 Filippo Carletti <filippo.carletti@gmail.com> - 2.1.3-1
- Upstream update to CGP 1.0

* Wed Jan 11 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.1.2-1
- httpd-admin: use KillMode=process - NethServer/dev#5190

* Fri Jul 08 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.1.1-1
- Dashboard: remove link from Applications page

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 2.1.0-1
- First NS7 release

* Tue Dec 29 2015 Filippo Carletti <filippo.carletti@gmail.com> - 1.2.0-1
- Update to latest cgp from github.

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- First release. Refs #2507

* Mon Dec 23 2013 Filippo Carletti <filippo.carletti@gmail.com> 1.0.0-1
- First release

