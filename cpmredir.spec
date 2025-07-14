Summary:	CPMREDIR - filesystem functions of an emulated CP/M computer
Summary(pl.UTF-8):	CPMREDIR - funkcje obsługi systemu plików emulowanego komputera CP/M
Name:		cpmredir
Version:	1.1.1
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.seasip.info/Unix/Zxcc/%{name}-%{version}.tar.gz
# Source0-md5:	2e7c91fd169e4e9efb926ef44bd610a7
Patch0:		%{name}-shared.patch
URL:		http://www.seasip.info/Unix/Zxcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPMREDIR is a library intended to support the filesystem functions of
an emulated CP/M computer, in a Unix or Windows (mingw32) environment.

%description -l pl.UTF-8
CPMREDIR to biblioteka mająca obsługiwać funkcje systemu plików
emulowanego komputera CP/M w środowisku uniksowym lub pod Windows
(mingw32).

%package devel
Summary:	Header files for cpmredir library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cpmredir
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cpmredir library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cpmredir.

%package static
Summary:	Static cpmredir library
Summary(pl.UTF-8):	Statyczna biblioteka cpmredir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cpmredir library.

%description static -l pl.UTF-8
Statyczna biblioteka cpmredir.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/libcpmredir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcpmredir.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcpmredir.so
%{_libdir}/libcpmredir.la
%{_includedir}/cpmredir.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcpmredir.a
