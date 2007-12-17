%define applewm_version 1.0.3
%define bigreqs_version 1.0.2
%define composite_version 0.4.0
%define damage_version 1.1.0
%define dmx_version 2.2.2
%define evieext_version 1.0.2
%define fixes_version 4.0
%define fontcache_version 0.1.2
%define fonts_version 2.0.2
%define gl_version 1.4.9
%define input_version 1.4.2.1
%define kb_version 1.0.3
%define print_version 1.0.3
%define randr_version 1.2.1
%define record_version 1.13.2
%define render_version 0.9.3
%define resource_version 1.0.2
%define scrnsaver_version 1.1.0
%define trap_version 3.4.3
%define video_version 2.2.2
%define vnc_version 1.0.0
%define windowswm_version 1.0.3
%define xcmisc_version 1.1.2
%define xext_version 7.0.2
%define xf86bigfont_version 1.1.2
%define xf86dga_version 2.0.3
%define xf86dri_version 2.0.3
%define xf86misc_version 0.9.2
%define xf86rush_version 1.1.2
%define xf86vidmode_version 2.2.2
%define xinerama_version 1.1.2
%define xproto_version 7.0.11
%define xproxymanagement_version 1.0.2
%define xcb_version 1.1

Name: x11-proto-devel
Summary: Xorg X11 protocol specification headers
Version: 7.3
Release: %mkrel 2
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
Source27: http://xorg.freedesktop.org/releases/individual/proto/xf86rushproto-%{xf86rush_version}.tar.bz2
Source28: http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-%{xf86vidmode_version}.tar.bz2
Source29: http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{xinerama_version}.tar.bz2
Source30: http://xorg.freedesktop.org/releases/individual/proto/xproto-%{xproto_version}.tar.bz2
Source31: http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-%{xproxymanagement_version}.tar.bz2
Source32: http://xf4vnc.sf.net/vncproto-%{vnc_version}.tar.bz2
Source33: http://xcb.freedesktop.org/dist/xcb-proto-%{xcb_version}.tar.bz2
BuildRequires: x11-util-macros >= 1.0.1
#gw for the pkgconfig files
#gw FIXME: this creates a circular dep on x11-proto-devel
BuildRequires: libxt-devel
BuildRequires: libxau-devel
#gw this is just for bootstrapping:
#Provides: pkgconfig(xproto) pkgconfig(kbproto) pkgconfig(renderproto)
%define oldxorgnamedevel  %mklibname xorg-x11
Conflicts: %{oldxorgnamedevel}-devel < 7.0

%description
X.Org X11 Protocol headers

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
./configure 	--prefix=%{_prefix} \
        	--exec-prefix=%{_prefix} \
        	--bindir=%{_bindir} \
        	--sbindir=%{_sbindir} \
        	--sysconfdir=%{_sysconfdir} \
        	--datadir=%{_datadir} \
        	--includedir=%{_includedir} \
        	--libdir=%{_libdir} \
        	--libexecdir=%{_libexecdir} \
        	--mandir=%{_mandir} \
        	--infodir=%{_infodir} 

%make
popd
done

%install
rm -rf %{buildroot}
for dir in *; do
pushd $dir
%makeinstall_std
popd
done

%clean
rm -rf %{buildroot}

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%defattr(-,root,root)
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
# these are doc, but it is not worth creating a doc package to put them in
%{_datadir}/doc/compositeproto/compositeproto.txt
%{_datadir}/doc/damageproto/damageproto.txt
%{_datadir}/doc/randrproto/randrproto.txt
%{_datadir}/doc/renderproto/renderproto.txt
