#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : modemmanager-qt
Version  : 5.106.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.106/modemmanager-qt-5.106.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.106/modemmanager-qt-5.106.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.106/modemmanager-qt-5.106.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: modemmanager-qt-data = %{version}-%{release}
Requires: modemmanager-qt-lib = %{version}-%{release}
Requires: modemmanager-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(ModemManager)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Modem Manager (MM) specification: https://developer.gnome.org/ModemManager/unstable/ref-dbus.html

%package data
Summary: data components for the modemmanager-qt package.
Group: Data

%description data
data components for the modemmanager-qt package.


%package dev
Summary: dev components for the modemmanager-qt package.
Group: Development
Requires: modemmanager-qt-lib = %{version}-%{release}
Requires: modemmanager-qt-data = %{version}-%{release}
Provides: modemmanager-qt-devel = %{version}-%{release}
Requires: modemmanager-qt = %{version}-%{release}

%description dev
dev components for the modemmanager-qt package.


%package lib
Summary: lib components for the modemmanager-qt package.
Group: Libraries
Requires: modemmanager-qt-data = %{version}-%{release}
Requires: modemmanager-qt-license = %{version}-%{release}

%description lib
lib components for the modemmanager-qt package.


%package license
Summary: license components for the modemmanager-qt package.
Group: Default

%description license
license components for the modemmanager-qt package.


%prep
%setup -q -n modemmanager-qt-5.106.0
cd %{_builddir}/modemmanager-qt-5.106.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684809142
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684809142
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/modemmanager-qt
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/modemmanager-qt-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/modemmanager-qt/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/modemmanagerqt.categories
/usr/share/qlogging-categories5/modemmanagerqt.renamecategories

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5ModemManagerQt.so
/usr/include/KF5/ModemManagerQt/Bearer
/usr/include/KF5/ModemManagerQt/Call
/usr/include/KF5/ModemManagerQt/GenericTypes
/usr/include/KF5/ModemManagerQt/Interface
/usr/include/KF5/ModemManagerQt/Manager
/usr/include/KF5/ModemManagerQt/Modem
/usr/include/KF5/ModemManagerQt/Modem3Gpp
/usr/include/KF5/ModemManagerQt/Modem3GppUssd
/usr/include/KF5/ModemManagerQt/ModemCdma
/usr/include/KF5/ModemManagerQt/ModemDevice
/usr/include/KF5/ModemManagerQt/ModemFirmware
/usr/include/KF5/ModemManagerQt/ModemLocation
/usr/include/KF5/ModemManagerQt/ModemMessaging
/usr/include/KF5/ModemManagerQt/ModemOma
/usr/include/KF5/ModemManagerQt/ModemSignal
/usr/include/KF5/ModemManagerQt/ModemSimple
/usr/include/KF5/ModemManagerQt/ModemTime
/usr/include/KF5/ModemManagerQt/ModemVoice
/usr/include/KF5/ModemManagerQt/Sim
/usr/include/KF5/ModemManagerQt/Sms
/usr/include/KF5/ModemManagerQt/bearer.h
/usr/include/KF5/ModemManagerQt/call.h
/usr/include/KF5/ModemManagerQt/generictypes.h
/usr/include/KF5/ModemManagerQt/interface.h
/usr/include/KF5/ModemManagerQt/manager.h
/usr/include/KF5/ModemManagerQt/modem.h
/usr/include/KF5/ModemManagerQt/modem3gpp.h
/usr/include/KF5/ModemManagerQt/modem3gppussd.h
/usr/include/KF5/ModemManagerQt/modemcdma.h
/usr/include/KF5/ModemManagerQt/modemdevice.h
/usr/include/KF5/ModemManagerQt/modemfirmware.h
/usr/include/KF5/ModemManagerQt/modemlocation.h
/usr/include/KF5/ModemManagerQt/modemmanagerqt_export.h
/usr/include/KF5/ModemManagerQt/modemmanagerqt_version.h
/usr/include/KF5/ModemManagerQt/modemmessaging.h
/usr/include/KF5/ModemManagerQt/modemoma.h
/usr/include/KF5/ModemManagerQt/modemsignal.h
/usr/include/KF5/ModemManagerQt/modemsimple.h
/usr/include/KF5/ModemManagerQt/modemtime.h
/usr/include/KF5/ModemManagerQt/modemvoice.h
/usr/include/KF5/ModemManagerQt/sim.h
/usr/include/KF5/ModemManagerQt/sms.h
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtConfig.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtConfigVersion.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtTargets.cmake
/usr/lib64/libKF5ModemManagerQt.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5ModemManagerQt.so.5.106.0
/V3/usr/lib64/libKF5ModemManagerQt.so.6
/usr/lib64/libKF5ModemManagerQt.so.5.106.0
/usr/lib64/libKF5ModemManagerQt.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/modemmanager-qt/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/modemmanager-qt/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/modemmanager-qt/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/modemmanager-qt/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/modemmanager-qt/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/modemmanager-qt/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/modemmanager-qt/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/modemmanager-qt/e458941548e0864907e654fa2e192844ae90fc32
