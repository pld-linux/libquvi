#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A cross-platform library for parsing flash media stream
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do analizy flashowych strumieni multimedialnych
Name:		libquvi
Version:	0.9.4
Release:	1
License:	AGPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	8e3f2134a6b3376934bd884b07dcdac5
URL:		http://quvi.sourceforge.net/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	curl-devel >= 7.21
BuildRequires:	doxygen
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	libgcrypt-devel >= 1.4.5
BuildRequires:	libproxy-devel >= 0.3.1
BuildRequires:	libquvi-scripts >= 0.9
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	curl-libs >= 7.21
Requires:	glib2 >= 1:2.24
Requires:	libgcrypt >= 1.4.5
Requires:	libproxy >= 0.3.1
Requires:	libquvi-scripts >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libquvi is a cross-platform library for parsing flash media stream.

%description -l pl.UTF-8
libquvi to wieloplatformowa biblioteka do analizy flashowych strumieni
multimedialnych.

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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static} \
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
%attr(755,root,root) %{_libdir}/libquvi-0.9-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquvi-0.9.so
%{_includedir}/quvi-0.9
%{_pkgconfigdir}/libquvi-0.9.pc
%{_mandir}/man3/libquvi.3*
%{_mandir}/man7/quvi-object.7*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libquvi-0.9.a
%endif
