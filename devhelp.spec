#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : devhelp
Version  : 3.22.0
Release  : 2
URL      : https://download.gnome.org/sources/devhelp/3.22/devhelp-3.22.0.tar.xz
Source0  : https://download.gnome.org/sources/devhelp/3.22/devhelp-3.22.0.tar.xz
Summary  : devhelp
Group    : Development/Tools
License  : GPL-2.0
Requires: devhelp-bin
Requires: devhelp-lib
Requires: devhelp-data
Requires: devhelp-license
Requires: devhelp-locales
Requires: devhelp-man
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(webkit2gtk-4.0)

%description
Devhelp information
===================
The following packages are required to compile Devhelp:

%package bin
Summary: bin components for the devhelp package.
Group: Binaries
Requires: devhelp-data
Requires: devhelp-license
Requires: devhelp-man

%description bin
bin components for the devhelp package.


%package data
Summary: data components for the devhelp package.
Group: Data

%description data
data components for the devhelp package.


%package dev
Summary: dev components for the devhelp package.
Group: Development
Requires: devhelp-lib
Requires: devhelp-bin
Requires: devhelp-data
Provides: devhelp-devel

%description dev
dev components for the devhelp package.


%package lib
Summary: lib components for the devhelp package.
Group: Libraries
Requires: devhelp-data
Requires: devhelp-license

%description lib
lib components for the devhelp package.


%package license
Summary: license components for the devhelp package.
Group: Default

%description license
license components for the devhelp package.


%package locales
Summary: locales components for the devhelp package.
Group: Default

%description locales
locales components for the devhelp package.


%package man
Summary: man components for the devhelp package.
Group: Default

%description man
man components for the devhelp package.


%prep
%setup -q -n devhelp-3.22.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536449990
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536449990
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/devhelp
cp COPYING %{buildroot}/usr/share/doc/devhelp/COPYING
%make_install
%find_lang devhelp

%files
%defattr(-,root,root,-)
/usr/lib64/gedit/plugins/devhelp.plugin
/usr/lib64/gedit/plugins/devhelp.py

%files bin
%defattr(-,root,root,-)
/usr/bin/devhelp

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/devhelp.convert
/usr/share/appdata/org.gnome.Devhelp.appdata.xml
/usr/share/applications/org.gnome.Devhelp.desktop
/usr/share/dbus-1/services/org.gnome.Devhelp.service
/usr/share/devhelp/assistant/assistant.css
/usr/share/devhelp/assistant/assistant.js
/usr/share/devhelp/dtd/devhelp-1.dtd
/usr/share/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
/usr/share/icons/hicolor/16x16/apps/devhelp.png
/usr/share/icons/hicolor/22x22/apps/devhelp.png
/usr/share/icons/hicolor/24x24/apps/devhelp.png
/usr/share/icons/hicolor/256x256/apps/devhelp.png
/usr/share/icons/hicolor/32x32/apps/devhelp.png
/usr/share/icons/hicolor/48x48/apps/devhelp.png
/usr/share/icons/hicolor/symbolic/apps/devhelp-symbolic.svg

%files dev
%defattr(-,root,root,-)
/usr/include/devhelp-3.0/devhelp/devhelp.h
/usr/include/devhelp-3.0/devhelp/dh-app.h
/usr/include/devhelp-3.0/devhelp/dh-assistant-view.h
/usr/include/devhelp-3.0/devhelp/dh-assistant.h
/usr/include/devhelp-3.0/devhelp/dh-book-manager.h
/usr/include/devhelp-3.0/devhelp/dh-book-tree.h
/usr/include/devhelp-3.0/devhelp/dh-book.h
/usr/include/devhelp-3.0/devhelp/dh-error.h
/usr/include/devhelp-3.0/devhelp/dh-keyword-model.h
/usr/include/devhelp-3.0/devhelp/dh-language.h
/usr/include/devhelp-3.0/devhelp/dh-link.h
/usr/include/devhelp-3.0/devhelp/dh-sidebar.h
/usr/include/devhelp-3.0/devhelp/dh-window.h
/usr/lib64/libdevhelp-3.so
/usr/lib64/pkgconfig/libdevhelp-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdevhelp-3.so.2
/usr/lib64/libdevhelp-3.so.2.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/devhelp/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/devhelp.1

%files locales -f devhelp.lang
%defattr(-,root,root,-)

