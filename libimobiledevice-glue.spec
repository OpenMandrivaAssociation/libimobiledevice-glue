%define major 0
%define api 1.0
%define oldlibname %mklibname imobiledevice-glue %{api} %{major}
%define libname %mklibname imobiledevice-glue
%define devname %mklibname -d imobiledevice-glue
#define _disable_ld_no_undefined 1
#define	git 20211124

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice-glue
Version:	1.3.0
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/%{version}/libimobiledevice-glue-%{version}.tar.bz2

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libplist-2.0) >= 2.2.0
BuildRequires:	pkgconfig(openssl)

%description
Library with common code used around the libimobiledevice project 

%package -n %{libname}
Group:		System/Libraries
Summary:	library with common code used around the libimobiledevice project 
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
Library with common code used around the libimobiledevice project 

%package -n %{devname}
Summary:	Development package for libimobiledevice-glue
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Files for development with libimobiledevice-glue.

%prep
%autosetup -p1

aclocal -I m4
autoheader
automake -a
autoconf

%configure

%build
%make_build

%install
%make_install

%files
%doc README.md

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so
%{_includedir}/%{name}/
