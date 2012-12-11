%define upstream_name		kolab
%define upstream_version	2.2.4


Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	8
Epoch:		2
Summary:	Perl Modules for use with the Kolab Server
License:	GPL
Group:		Development/Perl
Url:		http://kolab.org/cgi-bin/viewcvs-kolab.cgi/server/perl-kolab/
Source0:	%{name}-%{version}.tar.gz
Patch0:		Makefile.PL.diff
Patch1:		kolab_bootstrap.diff
BuildRequires:	perl-devel
BuildRequires:	perl-ldap
BuildRequires:	perl(URI)

Requires:	perl-Mail-IMAPClient
Requires:	perl-Convert-ASN1
Requires:	perl-Cyrus
Requires:	perl-MIME-tools
Requires:	perl-ldap
Requires:	perl-URI
Requires:	perl-XML-SAX
Requires:	perl-ldap


%description
Perl Modules for use with the Kolab Server

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
perl Makefile.PL \
   --config %{_sysconfdir}/kolab  --bin %{_bindir} --sbin %{_sbindir}  --etc %{_sysconfdir}/kolab
make
make test

%install
%makeinstall_std

# make some directories
install -d %{buildroot}%{_initrddir}

# make symlinks for kolabd, because it is used from the intidir
%__ln_s %{_bindir}/kolabd  %{buildroot}%{_initrddir}/kolabd

%files
%dir %{perl_vendorlib}/Kolab
%dir %{perl_vendorlib}/Kolab/LDAP
%dir %{perl_vendorlib}/Kolab/LDAP/Backend
%{perl_vendorlib}/Kolab.pm
%{perl_vendorlib}/Kolab/Conf.pm
%{perl_vendorlib}/Kolab/Cyrus.pm
%{perl_vendorlib}/Kolab/LDAP.pm
%{perl_vendorlib}/Kolab/LDAP/Backend.pm
%{perl_vendorlib}/Kolab/LDAP/Backend/ad.pm
%{perl_vendorlib}/Kolab/LDAP/Backend/fds.pm
%{perl_vendorlib}/Kolab/LDAP/Backend/slurpd.pm
%{perl_vendorlib}/Kolab/LDAP/Backend/syncrepl.pm
%{perl_vendorlib}/Kolab/Util.pm
%{_sysconfdir}/kolab/quotawarning.txt
%{_initrddir}/kolabd
%{_bindir}/kolab_smtpdpolicy
%{_bindir}/kolabdcachetool
%{_bindir}/kolabpasswd
%{_bindir}/kolabquotareport
%{_bindir}/kolabquotawarn
%{_sbindir}/kolab_bootstrap
%{_sbindir}/kolabcheckperm
%{_sbindir}/kolabconf
%{_sbindir}/kolabd
%{_mandir}/man3/*
%{_mandir}/man1/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2:2.2.4-7mdv2012.0
+ Revision: 765385
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 2:2.2.4-5
+ Revision: 669246
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Sep 11 2010 Thomas Spuhler <tspuhler@mandriva.org> 2:2.2.4-4mdv2011.0
+ Revision: 577597
- rebuilt against per-5.12.2

* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 2:2.2.4-3mdv2011.0
+ Revision: 560273
- recommit
- increase release to 3

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Wed Jul 14 2010 Thomas Spuhler <tspuhler@mandriva.org> 2:2.2.4-1mdv2011.0
+ Revision: 553001
- Updated to upstream version 2.2.4
- Updated to upstream version 2.2.4

* Sun Apr 11 2010 Thomas Spuhler <tspuhler@mandriva.org> 2:2.2.3-1mdv2010.1
+ Revision: 533606
- Upgrade to version 2.2.3
  This is now a perl package and has now the same version as the corresponding kolab package

* Wed Aug 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:5.8.7-9mdv2010.0
+ Revision: 417889
- don't duplicate spec-helper job

  + Thomas Spuhler <tspuhler@mandriva.org>
    - bumped the version to 9 for cooker
    - downgraded release to original and added subrel 1
    - Synched License with source, added Epoch 1
    - Add script for syncrepl (syncrepl.pm) and working path on LDAP.pm for *cache.db

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 5.8.7-8mdv2009.0
+ Revision: 223805
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-7mdv2008.1
+ Revision: 180354
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-6mdv2008.0
+ Revision: 33633
- new mandriva file

* Thu May 31 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-5mdv2008.0
+ Revision: 33136
- bump release
- make it use the same prefork values as our cyrus-imapd package

* Sat May 26 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-4mdv2008.0
+ Revision: 31493
- fixed correct ownership of the certs

* Fri May 25 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-3mdv2008.0
+ Revision: 31166
- update the mandriva file a bit more

* Fri May 25 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-2mdv2008.0
+ Revision: 31149
- update the mandriva file a bit

* Tue May 22 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-1mdv2008.0
+ Revision: 29701
- Import perl-kolab



* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 5.8.7-1mdv2007.1
- initial Mandriva package
