#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pygobject
Version  : 3.24.1
Release  : 2
URL      : https://download.gnome.org/sources/pygobject/3.24/pygobject-3.24.1.tar.xz
Source0  : https://download.gnome.org/sources/pygobject/3.24/pygobject-3.24.1.tar.xz
Summary  : Python bindings for GObject
Group    : Development/Tools
License  : LGPL-2.1
Requires: pygobject-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libffi)
BuildRequires : py2cairo
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
PyGObject
=====
Original authors:   James Henstridge <james@daa.com.au>
Johan Dahlin <johan@gnome.org>

%package dev
Summary: dev components for the pygobject package.
Group: Development
Provides: pygobject-devel

%description dev
dev components for the pygobject package.


%package python
Summary: python components for the pygobject package.
Group: Default

%description python
python components for the pygobject package.


%prep
%setup -q -n pygobject-3.24.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491837908
%configure --disable-static --disable-cairo
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1491837908
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
