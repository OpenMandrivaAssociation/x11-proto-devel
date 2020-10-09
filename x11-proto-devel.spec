
%bcond_without bootstrap

%define oldxorgnamedevel %mklibname xorg-x11
%define debug_package %{nil}

Name:		x11-proto-devel
Summary:	Xorg X11 protocol specification headers
Version:	2020.1
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xorgproto-%{version}.tar.bz2
Source10:	https://github.com/bbidulock/vncproto/archive/vncproto-1.1.tar.gz
Source11:	https://xorg.freedesktop.org/archive/individual/proto/xcb-proto-1.14.1.tar.xz
Source100:	x11-proto-devel.rpmlintrc
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	meson
%if !%{with bootstrap}
# For docs:
BuildRequires:	asciidoc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-dtd45-xml
BuildRequires:	xmlto
BuildRequires:	x11-sgml-doctools
%endif

BuildRequires:	python
BuildRequires:	python2
Conflicts:	%{oldxorgnamedevel}-devel < 7.0
Conflicts:	libxext6-devel <= 1.0.99.3-1mdv2010.0
Obsoletes:	x11-proto-doc < 2018.3

%description
X.Org X11 Protocol headers.

%package -n python2-xcbgen
Summary:	Python 2.x version of the XCB generators
Group:		Development/X11

%description -n python2-xcbgen
Python 2.x version of the XCB generators

#-----------------------------------------------------------

%prep
%setup -qn xorgproto-%{version} -a10 -a11

# vncproto is from git
cd vncproto-*
aclocal
automake -a -c
autoconf
cd ..

%build
%meson -Dlegacy=true
%meson_build

# Chromium uses the python xcbgen bits in a
# python2 specific script :/
# Google needs to get a brain
cd xcb-proto-*
mkdir buildpy2
cd buildpy2
export PYTHON=%{_bindir}/python2
CONFIGURE_TOP=.. \
	%configure
%make_build
unset PYTHON
cd ../..

for dir in xcb-proto-* vncproto-*; do
	cd $dir
	mkdir build
	cd build
	CONFIGURE_TOP=.. %configure
	%make_build
	cd ../..
done

%install
%meson_install

cd xcb-proto-*/buildpy2
%make_install
cd ../..
for dir in xcb-proto-* vnc-proto-*; do
    if [ -d $dir ]; then
	cd $dir/build
	%make_install
	cd ../..
    fi
done

# kill Xprint manpage since it clearly doesn't belong to printproto:
rm -rf %{buildroot}%{_mandir}/man7/Xprint*

%files
%dir %{_datadir}/xcb
%{_includedir}/GL/glx*
%{_includedir}/GL/internal/*
%{_includedir}/X11/*.h
%{_includedir}/X11/dri/*
%{_includedir}/X11/extensions/*
%{_includedir}/X11/fonts/*
%{_includedir}/X11/PM/*
%{_datadir}/pkgconfig/*.pc
%{_libdir}/pkgconfig/*.pc
%{_datadir}/xcb/*
# xcbgen stuff
%{python_sitelib}/xcbgen/align.py
%{python_sitelib}/xcbgen/__init__.py
%{python_sitelib}/xcbgen/error.py
%{python_sitelib}/xcbgen/expr.py
%{python_sitelib}/xcbgen/matcher.py
%{python_sitelib}/xcbgen/state.py
%{python_sitelib}/xcbgen/xtypes.py
%{python_sitelib}/xcbgen/__pycache__/*

%files -n python2-xcbgen
%{_prefix}/lib/python2*/site-packages/xcbgen
