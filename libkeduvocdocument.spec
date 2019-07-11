#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkeduvocdocument
Version  : 19.04.3
Release  : 9
URL      : https://download.kde.org/stable/applications/19.04.3/src/libkeduvocdocument-19.04.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.3/src/libkeduvocdocument-19.04.3.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.3/src/libkeduvocdocument-19.04.3.tar.xz.sig
Summary  : Common libraries for KDE Edu applications
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: libkeduvocdocument-lib = %{version}-%{release}
Requires: libkeduvocdocument-license = %{version}-%{release}
Requires: libkeduvocdocument-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
Contents of libkeduvocdocument as of July 2014, and brief description of each module:

%package dev
Summary: dev components for the libkeduvocdocument package.
Group: Development
Requires: libkeduvocdocument-lib = %{version}-%{release}
Provides: libkeduvocdocument-devel = %{version}-%{release}
Requires: libkeduvocdocument = %{version}-%{release}
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
%setup -q -n libkeduvocdocument-19.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562886451
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
export SOURCE_DATE_EPOCH=1562886451
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkeduvocdocument
cp COPYING %{buildroot}/usr/share/package-licenses/libkeduvocdocument/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkeduvocdocument/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libkeduvocdocument/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkeduvocdocument

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
/usr/lib64/libKEduVocDocument.so.5
/usr/lib64/libKEduVocDocument.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkeduvocdocument/COPYING
/usr/share/package-licenses/libkeduvocdocument/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libkeduvocdocument/COPYING.LIB

%files locales -f libkeduvocdocument.lang
%defattr(-,root,root,-)

