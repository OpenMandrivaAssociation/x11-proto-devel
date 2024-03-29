%bcond_without bootstrap
# Presently still needed because some chromium derivates
# haven't moved on
%bcond_without python2

%define oldxorgnamedevel %mklibname xorg-x11
%define debug_package %{nil}

Name:		x11-proto-devel
Summary:	Xorg X11 protocol specification headers
Version:	2023.2
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xorgproto-%{version}.tar.xz
Source10:	https://github.com/bbidulock/vncproto/archive/vncproto-1.1.tar.bz2
Source11:	https://xorg.freedesktop.org/archive/individual/proto/xcb-proto-1.16.0.tar.xz
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
%if %{with python2}
BuildRequires:	python2
%endif
BuildArch:	noarch
Conflicts:	%{oldxorgnamedevel}-devel < 7.0
Conflicts:	libxext6-devel <= 1.0.99.3-1mdv2010.0
Obsoletes:	x11-proto-doc < 2018.3

%description
X.Org X11 Protocol headers.

%package -n python2-xcbgen
Summary:	Python 2.x version of the XCB generators
Group:		Development/X11

%description -n python2-xcbgen
Python 2.x version of the XCB generators.

#-----------------------------------------------------------

%prep
%setup -qn xorgproto-%{version} -a10 -a11

# vncproto is from git
cd vncproto-*
aclocal
automake -a -c
autoconf
cd ..

# Not using the %%meson macro because specifying the (correct)
# crosscompiler breaks the build -- xorg-proto assumes
# build == host (but the result is noarch, so this is fine)
meson setup build \
	--buildtype=plain \
	--prefix=%{_prefix} \
	-Dlegacy=true

%build
%meson_build

%if %{with python2}
# Chromium uses the python xcbgen bits in a
# python2 specific script :/
# Google needs to get a brain
cd xcb-proto-*
mkdir buildpy2
cd buildpy2
export PYTHON=%{_bindir}/python2
# (tpg) let's be noarch
# Not using the %%configure macro because specifying the (correct)
# crosscompiler breaks the build -- xorg-proto assumes
# build == host (but the result is noarch, so this is fine)
../configure --prefix=%{_prefix} --libdir=%{_datadir}
%make_build
unset PYTHON
cd ../..
%endif

for dir in xcb-proto-* vncproto-*; do
    cd $dir
    mkdir build
    cd build
# (tpg) let's be noarch
# Not using the %%configure macro because specifying the (correct)
# crosscompiler breaks the build -- xorg-proto assumes
# build == host (but the result is noarch, so this is fine)
    ../configure --prefix=%{_prefix} --libdir=%{_datadir}
    %make_build
    cd ../..
done

%install
%meson_install

%if %{with python2}
cd xcb-proto-*/buildpy2
%make_install
cd ../..
%endif
for dir in xcb-proto-* vnc-proto-*; do
    if [ -d $dir ]; then
	cd $dir/build
	%make_install
	cd ../..
    fi
done

# now in libx11 since release 1.6.9
rm -rf %{buildroot}%{_includedir}/X11/extensions/XKBgeom.h
# now in libXvMC since release 1.0.12
rm -rf %{buildroot}%{_includedir}/X11/extensions/vldXvMC.h

rm -rf %{buildroot}%{_datadir}/doc/xorgproto/*.txt
rm -rf %{buildroot}%{_datadir}/doc/xorgproto/PM_spec

# kill Xprint manpage since it clearly doesn't belong to printproto:
rm -rf %{buildroot}%{_mandir}/man7/Xprint*

%files
%doc %{_docdir}/xorgproto
%dir %{_datadir}/xcb
%{_includedir}/GL/glx*
%{_includedir}/GL/internal/*
%{_includedir}/X11/*.h
%{_includedir}/X11/dri/*
%{_includedir}/X11/extensions/*
%{_includedir}/X11/fonts/*
%{_includedir}/X11/PM/*
%{_datadir}/pkgconfig/*.pc
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

%if %{with python2}
%files -n python2-xcbgen
%{_prefix}/lib/python2*/site-packages/xcbgen
%endif
