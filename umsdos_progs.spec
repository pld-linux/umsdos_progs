Summary:	Utilities for the Linux UMSDOS filesystem
Summary(pl):	Narzêdzia do linuksowego systemu plików UMSDOS
Name:		umsdos_progs
Version:	1.14
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.voyager.hr/umsdos/files/%{name}-%{version}.tgz
Patch0:		%{name}-mangle.patch
URL:		http://linux.voyager.hr/umsdos/progs.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
umsdos_progs contains utilities for using UMSDOS filesystem, such as
umssync, udosctl and umssetup. umssync and other utilities are
required to promote directories to UNIX semantics, and to check/fix
any out-of-sync files you may create when not using Linux.

%description -l pl
Pakiet umsdos_progs zwiera narzêdzia do systemu plików UMSDOS, takie
jak umssync, udosctl i umssetup. umssync i inne narzêdzia s± potrzebne
do promocji katalogów do semantyki uniksowej orz sprawdzania lub
poprawiania plików, które siê rozsynchoronizowa³y podczas nie u¿ywania
Linuksa.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags} -I../include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install util/umssync $RPM_BUILD_ROOT%{_sbindir}
ln -sf umssync $RPM_BUILD_ROOT%{_sbindir}/udosctl
ln -sf umssync $RPM_BUILD_ROOT%{_sbindir}/umssetup
install util/umssync.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
