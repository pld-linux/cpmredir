Summary:	CPMREDIR - filesystem functions of an emulated CP/M computer
Summary(pl):	CPMREDIR - funkcje obs³ugi systemu plików emulowanego komputera CP/M
Name:		cpmredir
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/Zxcc/%{name}-%{version}.tar.gz
# Source0-md5:	2e7c91fd169e4e9efb926ef44bd610a7
Patch0:		%{name}-shared.patch
URL:		http://www.seasip.demon.co.uk/Unix/Zxcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPMREDIR is a library intended to support the filesystem functions of
an emulated CP/M computer, in a Unix or Windows (mingw32) environment.

%description -l pl
CPMREDIR to biblioteka maj±ca obs³ugiwaæ funkcje systemu plików
emulowanego komputera CP/M w ¶rodowisku uniksowym lub pod Windows
(mingw32).

%package devel
Summary:	Header files for cpmredir library
Summary(pl):	Pliki nag³ówkowe biblioteki cpmredir
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	readline-devel

%description devel
Header files for cpmredir library.

%description devel -l pl
Pliki nag³ówkowe biblioteki cpmredir.

%package static
Summary:	Static cpmredir library
Summary(pl):	Statyczna biblioteka cpmredir
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static cpmredir library.

%description static -l pl
Statyczna biblioteka cpmredir.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
