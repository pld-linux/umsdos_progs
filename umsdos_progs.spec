Summary:	Utilities for the Linux UMSDOS filesystem
Summary(pl):	Narzêdzia do linuksowego systemu plików UMSDOS
Name:		umsdos_progs
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.voyager.hr/umsdos/files/%{name}-%{version}.tgz
# Source0-md5:	46f41fd9dbc23204f95f59619d30eee7
Patch0:		%{name}-mangle.patch
Patch1:		%{name}-glibc.patch
URL:		http://linux.voyager.hr/umsdos/progs.html
# for tests
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_sbindir	/sbin

%description
umsdos_progs contains utilities for using UMSDOS filesystem, such as
umssync, udosctl and umssetup. umssync and other utilities are
required to promote directories to UNIX semantics, and to check/fix
any out-of-sync files you may create when not using Linux.

%description -l pl
Pakiet umsdos_progs zwiera narzêdzia do systemu plików UMSDOS, takie
jak umssync, udosctl i umssetup. umssync i inne narzêdzia s± potrzebne
do promocji katalogów do semantyki uniksowej oraz sprawdzania lub
poprawiania plików, które siê rozsynchronizowa³y podczas nie u¿ywania
Linuksa.

%package uvfat
Summary:	Utilities for the UVFAT filesystem
Summary(pl):	Narzêdzia do systemu plików UVFAT
Group:		Applications/System

%description uvfat
umsdos_progs-uvfat contains utilities for using UVFAT filesystem, such
as uvfatsync, uvfatctl and uvfatsetup. uvfatsync and other utilities
are required to promote directories to UNIX semantics, and to
check/fix any out-of-sync files you may create when not using Linux.

%description uvfat -l pl
Pakiet umsdos_progs-uvfat zwiera narzêdzia do systemu plików UVFAT,
takie jak uvfatsync, uvfatctl i uvfatsetup. uvfatsync i inne narzêdzia
s± potrzebne do promocji katalogów do semantyki uniksowej oraz
sprawdzania lub poprawiania plików, które siê rozsynchronizowa³y
podczas nie u¿ywania Linuksa.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

sed -e '/^#define BE_UVFAT/d' include/ums_config.h > h.tmp
mv -f h.tmp include/ums_config.h

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I../include -DBE_UVFAT=1"
mv -f util/umssync uvfatsync
rm -f util/*.o
%{__make} \
	CFLAGS="%{rpmcflags} -I../include -DBE_UVFAT=0"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install util/umssync $RPM_BUILD_ROOT%{_sbindir}
ln -sf umssync $RPM_BUILD_ROOT%{_sbindir}/udosctl
ln -sf umssync $RPM_BUILD_ROOT%{_sbindir}/umssetup
install util/umssync.8 $RPM_BUILD_ROOT%{_mandir}/man8

install uvfatsync $RPM_BUILD_ROOT%{_sbindir}
ln -sf uvfatsync $RPM_BUILD_ROOT%{_sbindir}/uvfatctl
ln -sf uvfatsync $RPM_BUILD_ROOT%{_sbindir}/uvfatsetup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README util/TODO
%attr(755,root,root) %{_sbindir}/u[dm]*
%{_mandir}/man*/*

%files uvfat
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/uvfat*
