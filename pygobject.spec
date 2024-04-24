#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be97e829
#
Name     : pygobject
Version  : 3.48.2
Release  : 89
URL      : https://download.gnome.org/sources/pygobject/3.48/pygobject-3.48.2.tar.xz
Source0  : https://download.gnome.org/sources/pygobject/3.48/pygobject-3.48.2.tar.xz
Summary  : Python bindings for GObject
Group    : Development/Tools
License  : CC-BY-SA-3.0 LGPL-2.1
Requires: pygobject-license = %{version}-%{release}
Requires: pygobject-python = %{version}-%{release}
Requires: pygobject-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(py3cairo)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://gitlab.gnome.org/GNOME/pygobject/-/raw/master/docs/images/pygobject.svg?ref_type=heads
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


%package extras
Summary: extras components for the pygobject package.
Group: Default

%description extras
extras components for the pygobject package.


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
Provides: pypi(PyGObject)
Provides: pypi(pygobject)

%description python3
python3 components for the pygobject package.


%prep
%setup -q -n pygobject-3.48.2
cd %{_builddir}/pygobject-3.48.2
pushd ..
cp -a pygobject-3.48.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713917015
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtests=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtests=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/pygobject
cp %{_builddir}/pygobject-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pygobject/597bf5f9c0904bd6c48ac3a3527685818d11246d || :
cp %{_builddir}/pygobject-%{version}/docs/images/LICENSE %{buildroot}/usr/share/package-licenses/pygobject/37e8ad1b8f297bce2b0974196aa6998cc7f8e418 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc

%files extras
%defattr(-,root,root,-)
/V3/usr/lib/python3.12/site-packages/gi/_gi_cairo.cpython-312-x86_64-linux-gnu.so
/usr/lib/python3.12/site-packages/gi/_gi_cairo.cpython-312-x86_64-linux-gnu.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pygobject/37e8ad1b8f297bce2b0974196aa6998cc7f8e418
/usr/share/package-licenses/pygobject/597bf5f9c0904bd6c48ac3a3527685818d11246d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3.12/site-packages/gi/_gi.cpython-312-x86_64-linux-gnu.so
/usr/lib/python3.12/site-packages/PyGObject-3.48.2.egg-info
/usr/lib/python3.12/site-packages/gi/__init__.py
/usr/lib/python3.12/site-packages/gi/__pycache__/__init__.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_constants.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_error.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_gtktemplate.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_option.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_ossighelper.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_propertyhelper.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/_signalhelper.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/docstring.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/importer.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/module.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/pygtkcompat.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/__pycache__/types.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/_constants.py
/usr/lib/python3.12/site-packages/gi/_error.py
/usr/lib/python3.12/site-packages/gi/_gi.cpython-312-x86_64-linux-gnu.so
/usr/lib/python3.12/site-packages/gi/_gtktemplate.py
/usr/lib/python3.12/site-packages/gi/_option.py
/usr/lib/python3.12/site-packages/gi/_ossighelper.py
/usr/lib/python3.12/site-packages/gi/_propertyhelper.py
/usr/lib/python3.12/site-packages/gi/_signalhelper.py
/usr/lib/python3.12/site-packages/gi/docstring.py
/usr/lib/python3.12/site-packages/gi/importer.py
/usr/lib/python3.12/site-packages/gi/module.py
/usr/lib/python3.12/site-packages/gi/overrides/GIMarshallingTests.py
/usr/lib/python3.12/site-packages/gi/overrides/GLib.py
/usr/lib/python3.12/site-packages/gi/overrides/GObject.py
/usr/lib/python3.12/site-packages/gi/overrides/Gdk.py
/usr/lib/python3.12/site-packages/gi/overrides/GdkPixbuf.py
/usr/lib/python3.12/site-packages/gi/overrides/Gio.py
/usr/lib/python3.12/site-packages/gi/overrides/Gtk.py
/usr/lib/python3.12/site-packages/gi/overrides/Pango.py
/usr/lib/python3.12/site-packages/gi/overrides/__init__.py
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/GIMarshallingTests.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/GLib.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/GObject.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/Gdk.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/GdkPixbuf.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/Gio.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/Gtk.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/Pango.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/__init__.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/__pycache__/keysyms.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/overrides/keysyms.py
/usr/lib/python3.12/site-packages/gi/pygtkcompat.py
/usr/lib/python3.12/site-packages/gi/repository/__init__.py
/usr/lib/python3.12/site-packages/gi/repository/__pycache__/__init__.cpython-312.pyc
/usr/lib/python3.12/site-packages/gi/types.py
/usr/lib/python3.12/site-packages/pygtkcompat/__init__.py
/usr/lib/python3.12/site-packages/pygtkcompat/__pycache__/__init__.cpython-312.pyc
/usr/lib/python3.12/site-packages/pygtkcompat/__pycache__/generictreemodel.cpython-312.pyc
/usr/lib/python3.12/site-packages/pygtkcompat/__pycache__/pygtkcompat.cpython-312.pyc
/usr/lib/python3.12/site-packages/pygtkcompat/generictreemodel.py
/usr/lib/python3.12/site-packages/pygtkcompat/pygtkcompat.py
