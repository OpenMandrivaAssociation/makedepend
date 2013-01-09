Name:		makedepend
Version:	1.0.4
Release:	1
Summary:	Create dependencies in makefiles
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

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
%makeinstall_std

%files
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1*



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 666359
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 590415
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 464636
- New version: 1.0.2

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-6mdv2010.0
+ Revision: 426065
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-5mdv2009.1
+ Revision: 351549
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 223144
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.1
+ Revision: 152894
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Apr 17 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 13740
- new upstream release (1.0.1):
   * Pointer "file" dereferenced before NULL check
   * Packaged using new util macros


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:09:03 (27479)
- fix description & summary

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

