#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pygobject
Version  : 3.34.0
Release  : 43
URL      : https://download.gnome.org/sources/pygobject/3.34/pygobject-3.34.0.tar.xz
Source0  : https://download.gnome.org/sources/pygobject/3.34/pygobject-3.34.0.tar.xz
Summary  : Python bindings for GObject Introspection
Group    : Development/Tools
License  : CC-BY-SA-3.0 LGPL-2.1
Requires: pygobject-license = %{version}-%{release}
Requires: pygobject-python = %{version}-%{release}
Requires: pygobject-python3 = %{version}-%{release}
Requires: pycairo
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pycairo

%description
.. image:: https://pygobject.readthedocs.io/en/latest/_images/pygobject.svg
:align: center
:width: 400px
:height: 98px

%package dev
Summary: dev components for the pygobject package.
Group: Development
Provides: pygobject-devel = %{version}-%{release}
Requires: pygobject = %{version}-%{release}

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
Requires: pygobject-python3 = %{version}-%{release}

%description python
python components for the pygobject package.


%package python3
Summary: python3 components for the pygobject package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pygobject package.


%prep
%setup -q -n pygobject-3.34.0
cd %{_builddir}/pygobject-3.34.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573763897
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/pygobject
cp %{_builddir}/pygobject-3.34.0/COPYING %{buildroot}/usr/share/package-licenses/pygobject/597bf5f9c0904bd6c48ac3a3527685818d11246d
cp %{_builddir}/pygobject-3.34.0/docs/images/LICENSE %{buildroot}/usr/share/package-licenses/pygobject/37e8ad1b8f297bce2b0974196aa6998cc7f8e418
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pygobject/37e8ad1b8f297bce2b0974196aa6998cc7f8e418
/usr/share/package-licenses/pygobject/597bf5f9c0904bd6c48ac3a3527685818d11246d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
