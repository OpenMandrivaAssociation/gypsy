%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Summary:	A GPS multiplexing daemon
Name:		gypsy
Version:	0.9
Release:	3
Group:		System/Libraries
# See LICENSE file for details
License:	LGPLv2 and GPLv2
Url:		http://gypsy.freedesktop.org/
Source0:	http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.gz
Patch0:		gypsy-0.8-no-werror-patch

BuildRequires:	xsltproc
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
Requires:	dbus

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to 
access GPS data from multiple GPS sources concurrently. 

%package -n	%{libname}
Summary:	Libraries for gypsys
Group:		System/Libraries

%description -n %{libname}
Gypsy is a GPS multiplexing daemon which allows multiple clients to 
access GPS data from multiple GPS sources concurrently. 

%package -n	%{devname}
Summary:	Development package for gypsy
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
Header files for development with gypsy.

%package	docs
Summary:	Documentation files for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{version}
Requires:	gtk-doc
BuildArch:	noarch

%description	docs
This package contains developer documentation for %{name}.

%prep
%setup -q
%apply_patches
find -name Makefile|xargs rm -f
autoreconf -fi

%build
%configure \
	--disable-static \
	--enable-shared
%make V=2

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%config %{_sysconfdir}/dbus-1/system.d/Gypsy.conf
%config %{_sysconfdir}/gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service
%{_libexecdir}/gypsy-daemon

%files -n %{libname}
%{_libdir}/libgypsy.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/gypsy.pc
%dir %{_includedir}/gypsy
%{_includedir}/gypsy/*.h
%{_libdir}/libgypsy.so

%files docs
%{_datadir}/gtk-doc/html/gypsy

