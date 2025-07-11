#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkeduvocdocument
Version  : 25.04.2
Release  : 82
URL      : https://download.kde.org/stable/release-service/25.04.2/src/libkeduvocdocument-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/libkeduvocdocument-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/libkeduvocdocument-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-1-Clause BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: libkeduvocdocument-lib = %{version}-%{release}
Requires: libkeduvocdocument-license = %{version}-%{release}
Requires: libkeduvocdocument-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Contents of libkeduvocdocument as of July 2014, and brief description of each module:

%package dev
Summary: dev components for the libkeduvocdocument package.
Group: Development
Requires: libkeduvocdocument-lib = %{version}-%{release}
Provides: libkeduvocdocument-devel = %{version}-%{release}
Requires: libkeduvocdocument = %{version}-%{release}

%description dev
dev components for the libkeduvocdocument package.


%package lib
Summary: lib components for the libkeduvocdocument package.
Group: Libraries
Requires: libkeduvocdocument-license = %{version}-%{release}

%description lib
lib components for the libkeduvocdocument package.


%package license
Summary: license components for the libkeduvocdocument package.
Group: Default

%description license
license components for the libkeduvocdocument package.


%package locales
Summary: locales components for the libkeduvocdocument package.
Group: Default

%description locales
locales components for the libkeduvocdocument package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkeduvocdocument-25.04.2
cd %{_builddir}/libkeduvocdocument-25.04.2
pushd ..
cp -a libkeduvocdocument-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749487565
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1749487565
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkeduvocdocument
cp %{_builddir}/libkeduvocdocument-%{version}/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkeduvocdocument/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/libkeduvocdocument-%{version}/LICENSES/BSD-1-Clause.txt %{buildroot}/usr/share/package-licenses/libkeduvocdocument/6620eeea6ee5696c0b887850201ba4c607380356 || :
cp %{_builddir}/libkeduvocdocument-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/libkeduvocdocument/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/libkeduvocdocument-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkeduvocdocument/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
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
%find_lang libkeduvocdocument
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libkeduvocdocument/KEduVocArticle
/usr/include/libkeduvocdocument/KEduVocConjugation
/usr/include/libkeduvocdocument/KEduVocContainer
/usr/include/libkeduvocdocument/KEduVocDeclension
/usr/include/libkeduvocdocument/KEduVocDocument
/usr/include/libkeduvocdocument/KEduVocExpression
/usr/include/libkeduvocdocument/KEduVocIdentifier
/usr/include/libkeduvocdocument/KEduVocKVTML2Writer
/usr/include/libkeduvocdocument/KEduVocLeitnerBox
/usr/include/libkeduvocdocument/KEduVocLesson
/usr/include/libkeduvocdocument/KEduVocMultipleChoice
/usr/include/libkeduvocdocument/KEduVocPersonalPronoun
/usr/include/libkeduvocdocument/KEduVocText
/usr/include/libkeduvocdocument/KEduVocTranslation
/usr/include/libkeduvocdocument/KEduVocWordFlags
/usr/include/libkeduvocdocument/KEduVocWordtype
/usr/include/libkeduvocdocument/SharedKVTMLFiles
/usr/include/libkeduvocdocument/keduvocarticle.h
/usr/include/libkeduvocdocument/keduvocconjugation.h
/usr/include/libkeduvocdocument/keduvoccontainer.h
/usr/include/libkeduvocdocument/keduvocdeclension.h
/usr/include/libkeduvocdocument/keduvocdocument.h
/usr/include/libkeduvocdocument/keduvocdocument_export.h
/usr/include/libkeduvocdocument/keduvocdocument_version.h
/usr/include/libkeduvocdocument/keduvocexpression.h
/usr/include/libkeduvocdocument/keduvocidentifier.h
/usr/include/libkeduvocdocument/keduvockvtml2writer.h
/usr/include/libkeduvocdocument/keduvocleitnerbox.h
/usr/include/libkeduvocdocument/keduvoclesson.h
/usr/include/libkeduvocdocument/keduvocmultiplechoice.h
/usr/include/libkeduvocdocument/keduvocpersonalpronoun.h
/usr/include/libkeduvocdocument/keduvoctext.h
/usr/include/libkeduvocdocument/keduvoctranslation.h
/usr/include/libkeduvocdocument/keduvocwordflags.h
/usr/include/libkeduvocdocument/keduvocwordtype.h
/usr/include/libkeduvocdocument/sharedkvtmlfiles.h
/usr/lib64/cmake/libkeduvocdocument/LibKEduVocDocumentConfig.cmake
/usr/lib64/cmake/libkeduvocdocument/LibKEduVocDocumentTargets-relwithdebinfo.cmake
/usr/lib64/cmake/libkeduvocdocument/LibKEduVocDocumentTargets.cmake
/usr/lib64/libKEduVocDocument.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKEduVocDocument.so.5.1.0
/usr/lib64/libKEduVocDocument.so.5
/usr/lib64/libKEduVocDocument.so.5.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkeduvocdocument/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkeduvocdocument/6620eeea6ee5696c0b887850201ba4c607380356
/usr/share/package-licenses/libkeduvocdocument/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc
/usr/share/package-licenses/libkeduvocdocument/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f libkeduvocdocument.lang
%defattr(-,root,root,-)

