Summary:	Utilities for the Linux UMSDOS filesystem.
Summary(pl):	Narz/edzia do linuksowego systemu plik/ow UMSDOS
Name:		umsdos_progs
Version:	1.13
Release:	1
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
License:	GPL
Source0:	http://linux.voyager.hr/umsdos/files/%{name}-%{version}.tgz
URL:		http://linux.voyager.hr/umsdos/progs.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		prefix	/
%description
umsdos_progs contains utilities for using UMSDOS filesystem, such as
umssync, udosctl and umssetup. umssync and other utilities are
required to promote directories to UNIX semantics, and to check/fix
any out-of-sync files you may create when not using Linux.
umsdos_progs contains utilities for using UMSDOS filesystem, such as
umssync, udosctl and umssetup. umssync and other utilities are
required to promote directories to UNIX semantics, and to check/fix
any out-of-sync files you may create when not using Linux.

%description -l pl

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -I../include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_sbindir},%{_mandir}/man8}
install util/umssync $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_sbindir}/umssync $RPM_BUILD_ROOT%{_sbindir}/udosctl
ln -sf /sbin/umssync $RPM_BUILD_ROOT%{_sbindir}/umssetup
install util/umssync.8 $RPM_BUILD_ROOT%{_mandir}/man8
				
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
