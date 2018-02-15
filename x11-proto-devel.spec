%bcond_with bootstrap

%define oldxorgnamedevel %mklibname xorg-x11

Name:		x11-proto-devel
Summary:	Xorg X11 protocol specification headers
Version:	2018.2
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xorgproto-%{version}.tar.bz2
Source10:	http://xf4vnc.sf.net/vncproto-1.0.0.tar.bz2
Source11:	http://xcb.freedesktop.org/dist/xcb-proto-1.12.tar.bz2
Source100:	x11-proto-devel.rpmlintrc
# (tpg) https://bugs.freedesktop.org/show_bug.cgi?id=95490
Patch1:		xcb-proto-1.12-Make-whitespace-use-consistent.patch
Patch2:		xcb-proto-1.12-print-is-a-function-and-needs-parentheses.patch
BuildRequires:	x11-util-macros >= 1.0.1

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
Conflicts:	%{oldxorgnamedevel}-devel < 7.0
Conflicts:	libxext6-devel <= 1.0.99.3-1mdv2010.0

%description
X.Org X11 Protocol headers.

#-----------------------------------------------------------

%package -n x11-proto-doc
Summary:	Documentation for the X11 protocol and extensions
Group:		Development/X11
# Old proto-devel versions had some docs:
Conflicts:	x11-proto-devel <= 7.6-0.3mdv2011.0

%description -n x11-proto-doc
Documentation for the X11 protocol and extensions.

#-----------------------------------------------------------

%prep
%setup -qn xorgproto-%{version} -a10 -a11

pushd xcb-proto-*
%patch1 -p1
%patch2 -p1
popd

# vncproto is from cvs
pushd vncproto-*
aclocal
automake -a -c
autoconf
popd

%build
%configure
%make

for dir in xcb-proto-* vncproto-*; do
	pushd $dir
	%configure
	%make
	popd
done

%install
%makeinstall_std
for dir in xcb-proto-* vnc-proto-*; do
    if [ -d $dir ]; then
	pushd $dir
	%makeinstall_std
	popd
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


%files -n x11-proto-doc
%{_datadir}/doc/xorgproto
