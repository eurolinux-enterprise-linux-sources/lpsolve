Name:      lpsolve
Summary:   A Mixed Integer Linear Programming (MILP) solver
Version:   5.5.2.0
Release:   6%{?dist}
Source:    http://downloads.sourceforge.net/lpsolve/lp_solve_%{version}_source.tar.gz
Group:     System Environment/Libraries
URL:       http://sourceforge.net/projects/lpsolve
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+

Patch0:    lpsolve-5.5.0.11.cflags.patch

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
Requires: lpsolve = %{version}-%{release}
Summary: Files for developing with lpsolve
Group: Development/Libraries

%description devel
Includes and definitions for developing with lpsolve 

%prep
%setup -q -n lp_solve_5.5
%patch0 -p1 -b .cflags.patch
#sparc and s390 need -fPIC  lets sed it                                              
%ifarch sparcv9 sparc64 s390 s390x                                                   
sed -i -e 's|-fpic|-fPIC|g' lpsolve55/ccc                                            
%endif 

%build
cd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
cd ../lp_solve
sh -x ccc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/lpsolve
install -p -m 755 \
        lp_solve/bin/ux*/lp_solve $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so $RPM_BUILD_ROOT%{_libdir}
install -p -m 644 \
        lp*.h $RPM_BUILD_ROOT%{_includedir}/lpsolve

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt
%{_bindir}/lp_solve
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/lpsolve

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Dan Horák <dan[at]danny.cz> - 5.5.2.0-2
- fix build on s390(x)

* Fri Aug 13 2010 Caolán McNamara <caolanm@redhat.com> - 5.5.2.0-1
- latest version

* Mon Dec 21 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-3
- Preserve timestamps

* Thu Nov 05 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-2
- upstream source silently changed content

* Sat Sep 12 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.15-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-2
- defuzz patch

* Mon Feb 02 2009 Caolán McNamara <caolanm@redhat.com> - 5.5.0.14-1
- latest version

* Fri Jan 02 2009 Dennis Gilmore <dennis@ausil.us> - 5.5.0.13-2
- use -fPIC on sparc and s390 arches

* Mon Aug 04 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.13-1
- latest version

* Sat Aug 02 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.12-2
- Mar 20 upstream tarball now differs from Mar 14 tarball

* Fri Mar 14 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.12-1
- latest version

* Wed Feb 20 2008 Caolán McNamara <caolanm@redhat.com> - 5.5.0.11-1
- initial version
