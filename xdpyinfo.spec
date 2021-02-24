#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : xdpyinfo
Version  : 1.3.2
Release  : 5
URL      : https://www.x.org/releases/individual/app/xdpyinfo-1.3.2.tar.gz
Source0  : https://www.x.org/releases/individual/app/xdpyinfo-1.3.2.tar.gz
Source1  : https://www.x.org/releases/individual/app/xdpyinfo-1.3.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT-Opengroup
Requires: xdpyinfo-bin = %{version}-%{release}
Requires: xdpyinfo-license = %{version}-%{release}
Requires: xdpyinfo-man = %{version}-%{release}
BuildRequires : pkgconfig(dmx)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xtst)
BuildRequires : pkgconfig(xxf86dga)
BuildRequires : pkgconfig(xxf86vm)

%description
xdpyinfo is a utility for displaying information about an X server.
It is used to examine the capabilities of a server, the predefined
values for various parameters used in communicating between clients
and the server, and the different types of screens, visuals, and X11
protocol extensions that are available.

%package bin
Summary: bin components for the xdpyinfo package.
Group: Binaries
Requires: xdpyinfo-license = %{version}-%{release}

%description bin
bin components for the xdpyinfo package.


%package license
Summary: license components for the xdpyinfo package.
Group: Default

%description license
license components for the xdpyinfo package.


%package man
Summary: man components for the xdpyinfo package.
Group: Default

%description man
man components for the xdpyinfo package.


%prep
%setup -q -n xdpyinfo-1.3.2
cd %{_builddir}/xdpyinfo-1.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614192334
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1614192334
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdpyinfo
cp %{_builddir}/xdpyinfo-1.3.2/COPYING %{buildroot}/usr/share/package-licenses/xdpyinfo/a7c968e282631e3b29c66bcf4a438fc72b68be27
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xdpyinfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdpyinfo/a7c968e282631e3b29c66bcf4a438fc72b68be27

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xdpyinfo.1
