%define builddocs 1
#define bootstrap 0
#{?_without_bootstrap: %global bootstrap 0}
#{?_with_bootstrap: %global bootstrap 1}

%define applewm_version 1.4.2
%define bigreqs_version 1.1.2
%define composite_version 0.4.2
%define damage_version 1.2.1
%define dmx_version 2.3.1
%define dri2_version 2.6
%define evieext_version 1.1.1
%define fixes_version 5.0
%define fontcache_version 0.1.3
%define fonts_version 2.1.2
%define gl_version 1.4.15
%define input_version 2.2
%define kb_version 1.0.6
%define print_version 1.0.5
%define randr_version 1.3.2
%define record_version 1.14.2
%define render_version 0.11.1
%define resource_version 1.2.0
%define scrnsaver_version 1.2.2
%define trap_version 3.4.3
%define video_version 2.3.1
%define vnc_version 1.0.0
%define windowswm_version 1.0.4
%define xcmisc_version 1.2.2
%define xext_version 7.2.1
%define xf86bigfont_version 1.2.0
%define xf86dga_version 2.1
%define xf86dri_version 2.1.1
%define xf86misc_version 0.9.3
%define xf86vidmode_version 2.3.1
%define xinerama_version 1.2.1
%define xproto_version 7.0.22
%define xproxymanagement_version 1.0.3
%define xcb_version 1.7.1

Name: x11-proto-devel
Summary: Xorg X11 protocol specification headers
Version: 7.6
Release: 7
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/proto/applewmproto-%{applewm_version}.tar.bz2
Source1: http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{bigreqs_version}.tar.bz2
Source2: http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{composite_version}.tar.bz2
Source3: http://xorg.freedesktop.org/releases/individual/proto/damageproto-%{damage_version}.tar.bz2
Source4: http://xorg.freedesktop.org/releases/individual/proto/dmxproto-%{dmx_version}.tar.bz2
Source5: http://xorg.freedesktop.org/releases/individual/proto/evieext-%{evieext_version}.tar.bz2
Source6: http://xorg.freedesktop.org/releases/individual/proto/fixesproto-%{fixes_version}.tar.bz2
Source7: http://xorg.freedesktop.org/releases/individual/proto/fontcacheproto-%{fontcache_version}.tar.bz2
Source8: http://xorg.freedesktop.org/releases/individual/proto/fontsproto-%{fonts_version}.tar.bz2
Source9: http://xorg.freedesktop.org/releases/individual/proto/glproto-%{gl_version}.tar.bz2
Source10: http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{input_version}.tar.bz2
Source11: http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{kb_version}.tar.bz2
Source12: http://xorg.freedesktop.org/releases/individual/proto/printproto-%{print_version}.tar.bz2
Source13: http://xorg.freedesktop.org/releases/individual/proto/randrproto-%{randr_version}.tar.bz2
Source14: http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{record_version}.tar.bz2
Source15: http://xorg.freedesktop.org/releases/individual/proto/renderproto-%{render_version}.tar.bz2
Source16: http://xorg.freedesktop.org/releases/individual/proto/resourceproto-%{resource_version}.tar.bz2
Source17: http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-%{scrnsaver_version}.tar.bz2
Source18: http://xorg.freedesktop.org/releases/individual/proto/trapproto-%{trap_version}.tar.bz2
Source19: http://xorg.freedesktop.org/releases/individual/proto/videoproto-%{video_version}.tar.bz2
Source20: http://xorg.freedesktop.org/releases/individual/proto/windowswmproto-%{windowswm_version}.tar.bz2
Source21: http://xorg.freedesktop.org/releases/individual/proto/xcmiscproto-%{xcmisc_version}.tar.bz2
Source22: http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{xext_version}.tar.bz2
Source23: http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-%{xf86bigfont_version}.tar.bz2
Source24: http://xorg.freedesktop.org/releases/individual/proto/xf86dgaproto-%{xf86dga_version}.tar.bz2
Source25: http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-%{xf86dri_version}.tar.bz2
Source26: http://xorg.freedesktop.org/releases/individual/proto/xf86miscproto-%{xf86misc_version}.tar.bz2
Source27: http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{xf86vidmode_version}.tar.bz2
Source28: http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{xinerama_version}.tar.bz2
Source29: http://xorg.freedesktop.org/releases/individual/proto/xproto-%{xproto_version}.tar.bz2
Source30: http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-%{xproxymanagement_version}.tar.bz2
Source31: http://xf4vnc.sf.net/vncproto-%{vnc_version}.tar.bz2
Source32: http://xcb.freedesktop.org/dist/xcb-proto-%{xcb_version}.tar.bz2
Source33: http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{dri2_version}.tar.bz2
Source100: x11-proto-devel.rpmlintrc

BuildRequires: x11-util-macros >= 1.0.1

%if %builddocs
# For docs:
BuildRequires: docbook-dtd412-xml
BuildRequires: docbook-dtd45-xml
#BuildRequires: fop
BuildRequires: xmlto
BuildRequires: x11-sgml-doctools
%endif

# (cg) As previously noted by gw, requiring libxt-devel and libxau-devel
# creates a circular dependancy. This can cause problems when building e.g.
# libx11 as it requires itself. When libxcb changed and droped a provided library
# libx11 could not be rebuilt due to this problem.
#
# In order to build libx11 without the circular problem, it is necessary
# to submit a bootstrapping version of this package that contains the minimal
# (manual) pkgconfig() provides as commented below, and disable the 
# BuildRequires on libxt-devel and libxau-devel.
# After libx11 is built and available, this package should be reverted.
#if %bootstrap
#Provides: pkgconfig(xproto) pkgconfig(kbproto) pkgconfig(renderproto)
#else
#BuildRequires: libxt-devel
#BuildRequires: libxau-devel
#endif
BuildRequires: python
%define oldxorgnamedevel  %mklibname xorg-x11
Conflicts: %{oldxorgnamedevel}-devel < 7.0
Conflicts: libxext6-devel <= 1.0.99.3-1mdv2010.0

%description
X.Org X11 Protocol headers

#-----------------------------------------------------------

%package -n x11-proto-doc
Summary: Documentation for the X11 protocol and extensions
Group:   Development/X11
# Old proto-devel versions had some docs:
Conflicts: x11-proto-devel <= 7.6-0.3mdv2011.0

%description -n x11-proto-doc
Documentation for the X11 protocol and extensions.

#-----------------------------------------------------------

%prep
%setup -q -c x11-proto-devel -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9 -b10 -b11 -b12 -b13 -b14 -b15 -b16 -b17 -b18 -b19 -b20 -b21 -b22 -b23 -b24 -b25 -b26 -b27 -b28 -b29 -b30 -b31 -b32 -b33

%build
# vncproto is from cvs
pushd vncproto-*
aclocal
automake -a -c
autoconf
popd

for dir in *; do
pushd $dir
%configure2_5x
%make
popd
done

%install
rm -rf %{buildroot}
for dir in *; do
    if [ -d $dir ]; then
	pushd $dir
	%makeinstall_std
	popd
    fi
done

# kill Xprint manpage since it clearly doesn't belong to printproto:
rm -rf %{buildroot}%{_mandir}/man7/Xprint*

%pre
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%dir %{_datadir}/xcb
%{_includedir}/GL/glx*
%{_includedir}/GL/internal/*
%{_includedir}/X11/*.h
%{_includedir}/X11/dri/*
%{_includedir}/X11/extensions/*
%{_includedir}/X11/fonts/*
%{_includedir}/X11/PM/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/xcb/*
# xcbgen stuff
%{python_sitelib}/xcbgen/__init__.py
%{python_sitelib}/xcbgen/__init__.pyc
%{python_sitelib}/xcbgen/__init__.pyo
%{python_sitelib}/xcbgen/error.py
%{python_sitelib}/xcbgen/error.pyc
%{python_sitelib}/xcbgen/error.pyo
%{python_sitelib}/xcbgen/expr.py
%{python_sitelib}/xcbgen/expr.pyc
%{python_sitelib}/xcbgen/expr.pyo
%{python_sitelib}/xcbgen/matcher.py
%{python_sitelib}/xcbgen/matcher.pyc
%{python_sitelib}/xcbgen/matcher.pyo
%{python_sitelib}/xcbgen/state.py
%{python_sitelib}/xcbgen/state.pyc
%{python_sitelib}/xcbgen/state.pyo
%{python_sitelib}/xcbgen/xtypes.py
%{python_sitelib}/xcbgen/xtypes.pyc
%{python_sitelib}/xcbgen/xtypes.pyo

%files -n x11-proto-doc
%{_datadir}/doc/bigreqsproto
%{_datadir}/doc/compositeproto
%{_datadir}/doc/damageproto
%{_datadir}/doc/dri2proto
%{_datadir}/doc/fixesproto
%{_datadir}/doc/fontsproto
%{_datadir}/doc/inputproto
%{_datadir}/doc/randrproto
%{_datadir}/doc/recordproto
%{_datadir}/doc/renderproto
%{_datadir}/doc/resourceproto
%{_datadir}/doc/scrnsaverproto
%{_datadir}/doc/videoproto
%{_datadir}/doc/xcmiscproto
%{_datadir}/doc/xextproto
%{_datadir}/doc/xproxymanagementprotocol
%{_datadir}/doc/xproto
%{_datadir}/doc/kbproto
