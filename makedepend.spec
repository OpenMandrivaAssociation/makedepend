Summary:	Create dependencies in makefiles
Name:		makedepend
Version:	1.0.8
Release:	2
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0

%description
The makedepend program reads each source file in sequence and parses it like  a
C-preprocessor, processing all C #* directives so that it can correctly tell
which include directives would be used in a compilation.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/makedepend
%doc %{_mandir}/man1/makedepend.1*
