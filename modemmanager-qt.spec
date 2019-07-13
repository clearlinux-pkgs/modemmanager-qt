#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : modemmanager-qt
Version  : 5.60.0
Release  : 19
URL      : https://download.kde.org/stable/frameworks/5.60/modemmanager-qt-5.60.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.60/modemmanager-qt-5.60.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.60/modemmanager-qt-5.60.0.tar.xz.sig
Summary  : Qt wrapper for ModemManager DBus API
Group    : Development/Tools
License  : LGPL-2.1
Requires: modemmanager-qt-data = %{version}-%{release}
Requires: modemmanager-qt-lib = %{version}-%{release}
Requires: modemmanager-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(ModemManager)
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n modemmanager-qt-5.60.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563048114
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1563048114
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/modemmanager-qt
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/modemmanager-qt/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/modemmanager-qt.categories

%files dev
%defattr(-,root,root,-)
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
/usr/include/KF5/ModemManagerQt/modemmessaging.h
/usr/include/KF5/ModemManagerQt/modemoma.h
/usr/include/KF5/ModemManagerQt/modemsignal.h
/usr/include/KF5/ModemManagerQt/modemsimple.h
/usr/include/KF5/ModemManagerQt/modemtime.h
/usr/include/KF5/ModemManagerQt/modemvoice.h
/usr/include/KF5/ModemManagerQt/sim.h
/usr/include/KF5/ModemManagerQt/sms.h
/usr/include/KF5/modemmanagerqt_version.h
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtConfig.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtConfigVersion.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ModemManagerQt/KF5ModemManagerQtTargets.cmake
/usr/lib64/libKF5ModemManagerQt.so
/usr/lib64/qt5/mkspecs/modules/qt_ModemManagerQt.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ModemManagerQt.so.5.60.0
/usr/lib64/libKF5ModemManagerQt.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/modemmanager-qt/COPYING.LIB
