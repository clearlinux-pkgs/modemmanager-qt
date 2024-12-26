#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : modemmanager-qt
Version  : 6.9.0
Release  : 89
URL      : https://download.kde.org/stable/frameworks/6.9/modemmanager-qt-6.9.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.9/modemmanager-qt-6.9.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.9/modemmanager-qt-6.9.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: modemmanager-qt-data = %{version}-%{release}
Requires: modemmanager-qt-lib = %{version}-%{release}
Requires: modemmanager-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : pkg-config
BuildRequires : pkgconfig(ModemManager)
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n modemmanager-qt-6.9.0
cd %{_builddir}/modemmanager-qt-6.9.0
pushd ..
cp -a modemmanager-qt-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735238656
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1735238656
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
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/modemmanagerqt.categories
/usr/share/qlogging-categories6/modemmanagerqt.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Bearer
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Call
/usr/include/KF6/ModemManagerQt/ModemManagerQt/GenericTypes
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Interface
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Manager
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Modem
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Modem3Gpp
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Modem3GppUssd
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemCdma
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemDevice
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemFirmware
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemLocation
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemMessaging
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemOma
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemSignal
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemSimple
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemTime
/usr/include/KF6/ModemManagerQt/ModemManagerQt/ModemVoice
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Sim
/usr/include/KF6/ModemManagerQt/ModemManagerQt/Sms
/usr/include/KF6/ModemManagerQt/modemmanagerqt/bearer.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/call.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/generictypes.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/interface.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/manager.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modem.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modem3gpp.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modem3gppussd.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemcdma.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemdevice.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemfirmware.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemlocation.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemmessaging.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemoma.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemsignal.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemsimple.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemtime.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/modemvoice.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/sim.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt/sms.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt_export.h
/usr/include/KF6/ModemManagerQt/modemmanagerqt_version.h
/usr/lib64/cmake/KF6ModemManagerQt/KF6ModemManagerQtConfig.cmake
/usr/lib64/cmake/KF6ModemManagerQt/KF6ModemManagerQtConfigVersion.cmake
/usr/lib64/cmake/KF6ModemManagerQt/KF6ModemManagerQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6ModemManagerQt/KF6ModemManagerQtTargets.cmake
/usr/lib64/libKF6ModemManagerQt.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6ModemManagerQt.so.6.9.0
/usr/lib64/libKF6ModemManagerQt.so.6
/usr/lib64/libKF6ModemManagerQt.so.6.9.0

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
