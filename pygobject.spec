#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pygobject
Version  : 3.28.3
Release  : 23
URL      : https://download.gnome.org/sources/pygobject/3.28/pygobject-3.28.3.tar.xz
Source0  : https://download.gnome.org/sources/pygobject/3.28/pygobject-3.28.3.tar.xz
Summary  : Python bindings for GObject Introspection
Group    : Development/Tools
License  : CC-BY-SA-3.0 LGPL-2.1
Requires: pygobject-python3
Requires: pygobject-license
Requires: pygobject-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(pycairo)
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://pygobject.readthedocs.io/en/latest/_images/pygobject.svg
:align: center
:width: 400px
:height: 98px

%package dev
Summary: dev components for the pygobject package.
Group: Development
Provides: pygobject-devel

%description dev
dev components for the pygobject package.


%package license
Summary: license components for the pygobject package.
Group: Default

%description license
license components for the pygobject package.


%package python
Summary: python components for the pygobject package.
Group: Default
Requires: pygobject-python3

%description python
python components for the pygobject package.


%package python3
Summary: python3 components for the pygobject package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pygobject package.


%prep
%setup -q -n pygobject-3.28.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530382734
%configure --disable-static --enable-cairo
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1530382734
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pygobject
cp COPYING %{buildroot}/usr/share/doc/pygobject/COPYING
cp docs/images/LICENSE %{buildroot}/usr/share/doc/pygobject/docs_images_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc

%files license
%defattr(-,root,root,-)
/usr/share/doc/pygobject/COPYING
/usr/share/doc/pygobject/docs_images_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
