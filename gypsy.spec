%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Name:		gypsy
Version:	0.8
Release:	5
Summary:	A GPS multiplexing daemon
Group:		System/Libraries
# See LICENSE file for details
License:	LGPLv2 and GPLv2
URL:		http://gypsy.freedesktop.org/
Source0:	http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.gz
Patch0:		gypsy-0.8-no-werror-patch
Patch1:		gypsy-0.8-automake-1.13.patch

BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gtk-doc
BuildRequires:	xsltproc
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

%build
autoreconf -fi
%configure	\
	--disable-static \
	--enable-shared
%make V=2

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%config %{_sysconfdir}/dbus-1/system.d/Gypsy.conf
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



%changelog
* Sun Dec 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.8-4
+ Revision: 740193
- rebuild
- removed .la files
- spec clean up
- use apply_patches

* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8-3
+ Revision: 673125
- fix some rpmlint errors
- fix group
- add a canonical -devel provides
- fix build issues
- imported package gypsy


* Mon May 9 2011 Per Øyvind Karlsen peroyvind@mandriva.org> 0.8-3
- imported and heavily adapted from fedora

* Tue Sep 7 2010 Peter Robinson <pbrobinson@gmail.com> 0.8-2
- Update to new source URL

* Wed Jun 9 2010 Peter Robinson <pbrobinson@gmail.com> 0.8-1
- New upstream 0.8 release

* Thu Aug 06 2009 Bastien Nocera <bnocera@redhat.com> 0.7-1
- Update to 0.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Bastien Nocera <bnocera@redhat.com> 0.6-9
- Gypsy is supposed to run as a system service, as root

* Wed Mar  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.6-8
- Move docs to noarch, some spec file updates

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-6
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-5
- Rebuild

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.6-4
- Rebuild

* Mon May 15 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-3
- Further spec file cleanups

* Mon Apr 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-2
- Some spec file cleanups

* Sat Apr 26 2008 Peter Robinson <pbrobinson@gmail.com> 0.6-1
- Initial package
