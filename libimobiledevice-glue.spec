%define major 0
%define api 1.0
%define libname %mklibname imobiledevice-glue %{api} %{major}
%define devname %mklibname -d imobiledevice-glue
%define _disable_ld_no_undefined 1
%define	git 20211124

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice-glue
Version:	0.0.0
Release:	1.%{git}.0
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

#BuildRequires:	swig
BuildRequires:	pkgconfig(glib-2.0)
#BuildRequires:	pkgconfig(libplist-2.0) >= 2.2.0
#BuildRequires:	pkgconfig(libplist++-2.0) >= 2.2.0
#BuildRequires:	pkgconfig(libtasn1)
#BuildRequires:	pkgconfig(libusbmuxd-2.0) >= 2.0.2
BuildRequires:	pkgconfig(openssl)

%description
Library with common code used around the libimobiledevice project 

%package -n %{libname}
Group:		System/Libraries
Summary:	library with common code used around the libimobiledevice project 

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
%setup -q
%autopatch -p1

%build
./autogen.sh
%configure --enable-static=no

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
