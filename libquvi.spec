#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A cross-platform library for parsing flash media stream
Name:		libquvi
Version:	0.4.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	acc5a5da25a7f89c6ff5338d00eaaf58
Patch0:		%{name}-automake-1.12.patch
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.18.2
BuildRequires:	libquvi-scripts >= 0.4.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libquvi-scripts >= 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libquvi is a cross-platform library for parsing flash media stream.

%package devel
Summary:	Header files for libquvi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libquvi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lua51-devel
Provides:	quvi-devel = %{version}-%{release}
Obsoletes:	quvi-devel < 0.2.16.2-2

%description devel
Header files for libquvi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libquvi.

%package static
Summary:	Static libquvi library
Summary(pl.UTF-8):	Statyczna biblioteka libquvi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	quvi-static = %{version}-%{release}
Obsoletes:	quvi-static < 0.2.16.2-2

%description static
Static libquvi library.

%description static -l pl.UTF-8
Statyczna biblioteka libquvi.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libquvi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libquvi.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquvi.so
%{_mandir}/man3/libquvi.3*
%{_includedir}/quvi
%{_pkgconfigdir}/libquvi.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libquvi.a
%endif
