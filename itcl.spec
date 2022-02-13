%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Summary:        Object oriented extensions to Tcl and Tk
Name:           itcl
Version:        4.1.1
Release:        1
License:        TCL
URL:            http://incrtcl.sourceforge.net/itcl/
Source0:        https://downloads.sourceforge.net/incrtcl/itcl%{version}.tar.gz
Patch1:         itcl-libdir.patch
Patch2:         itcl-soname.patch

BuildRequires:  tcl-devel

Requires:       tcl(abi) = 8.6

%description
[incr Tcl] is Tcl extension that provides object-oriented features that are
missing from the Tcl language.

%files
%dir %{tcl_sitearch}/%{name}%{version}
%{tcl_sitearch}/%{name}%{version}/*.tcl
%{_libdir}/*.so
%{_mandir}/mann/*.n*
%license license.terms
%doc README releasenotes.txt

#--------------------------------------------------------------------

%package devel
Summary:  Development headers and libraries for linking against itcl
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for linking against itcl.

%files devel
%{_includedir}/*.h
%{tcl_sitearch}/%{name}%{version}/*.a
%{_libdir}/itclConfig.sh

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}%{version}

%build
%configure
%make_build
	
%install
%make_install
	
# Patch the updated location of the stub library
sed -i -e "s#%{_libdir}/%{name}%{version}#%{tcl_sitearch}/%{name}%{version}#" \
        $RPM_BUILD_ROOT%{_libdir}/itclConfig.sh

%check
make test
