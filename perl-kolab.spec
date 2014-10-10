%define upstream_name		kolab
%define upstream_version	2.2.4

%define debug_package %{nil}

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	9
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

