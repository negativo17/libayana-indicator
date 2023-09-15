Name:           libayatana-indicator
Version:        0.9.3
Release:        1%{?dist}
Summary:        Ayatana Indicators shared library
License:        GPLv3
URL:            https://github.com/AyatanaIndicators/%{name}

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-build.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Ayatana Indicators shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Ayatana Indicators shared library.

This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
    -DENABLE_IDO=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc ChangeLog NEWS README.md
%{_libdir}/%{name}3.so.7
%{_libdir}/%{name}3.so.7.0.0

%files devel
%{_includedir}/%{name}3-0.4/*
%{_libdir}/%{name}3.so
%{_libdir}/pkgconfig/ayatana-indicator3-0.4.pc

%changelog
* Fri Sep 15 2023 Simone Caronni <negativo17@gmail.com> - 0.9.3-1
- First build.
