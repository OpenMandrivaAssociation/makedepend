Name: makedepend
Version: 1.0.4
Release: 1
Summary: Create dependencies in makefiles
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The makedepend program reads each source file in sequence and parses it like  a
C-preprocessor, processing all C #* directives so that it can correctly tell
which include directives would be used in a compilation.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1*

