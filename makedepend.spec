Summary:	Create dependencies in makefiles
Name:		makedepend
Version:	1.0.5
Release:	4
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0

%description
The makedepend program reads each source file in sequence and parses it like  a
C-preprocessor, processing all C #* directives so that it can correctly tell
which include directives would be used in a compilation.

%prep
%setup -q
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
autoreconf -fi

%build
%configure2_5x \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1*

