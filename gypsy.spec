Name:		gypsy
Version:	0.8
Release:	3
Summary:	A GPS multiplexing daemon

Group:		System/Libraries
# See LICENSE file for details
License:	LGPLv2 and GPLv2
URL:		http://gypsy.freedesktop.org/
Source0:	http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	bluez-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	xsltproc
Requires:	dbus

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to 
access GPS data from multiple GPS sources concurrently. 

%define	major	0
%define	libname	%mklibname %{name} %{major}
%package -n	%{libname}
Summary:	Libraries for gypsys
Group:		System/Libraries

%description -n %{libname}
Gypsy is a GPS multiplexing daemon which allows multiple clients to 
access GPS data from multiple GPS sources concurrently. 

%define	devname	%mklibname -d %{name}
%package -n	%{devname}
Summary:	Development package for gypsy
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Header files for development with gypsy.

%package	docs
Summary:	Documentation files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc
BuildArch:	noarch

%description	docs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Wno-error" \
%configure	--disable-static \
		--enable-shared \
		--enable-n810 \
%make

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%{_sysconfdir}/dbus-1/system.d/Gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service
%{_libexecdir}/gypsy-daemon

%files -n %{libname}
%{_libdir}/libgypsy.so.%{major}
%{_libdir}/libgypsy.so.%{major}.0.0

%files -n %{devname}
%{_libdir}/pkgconfig/gypsy.pc
%dir %{_includedir}/gypsy
%{_includedir}/gypsy/*.h
%{_libdir}/libgypsy.so

%files docs
%{_datadir}/gtk-doc/html/gypsy

