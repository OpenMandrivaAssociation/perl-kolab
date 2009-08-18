Summary:	Kolab - Perl extension for general Kolab settings
Name:		perl-kolab
Version:	5.8.7
Release:	%mkrel 9
Epoch:        	0
License:	GPL
Group:		Development/Perl
URL:		http://kolab.org/cgi-bin/viewcvs-kolab.cgi/server/perl-kolab/
Source0:	%{name}-%{version}.tar.bz2
Source1:	mandriva
Source2:	syncrepl.pm
Patch0:		perl-kolab-mdv_conf.diff
Patch1:		perl-kolab-cyrus-imapd_prefork.diff
Patch2:		LDAP.pm.in.diff
Patch3:		Makefile.in.diff
BuildRequires:	perl-devel
BuildRequires:	perl
BuildArch:	noarch
Provides:	perl-Kolab = %{version}
Provides:	perl-Kolab-Conf = %{version}
Provides:	perl-Kolab-Cyrus = %{version}
Provides:	perl-Kolab-DirServ = %{version}
Provides:	perl-Kolab-LDAP = %{version}
Provides:	perl-Kolab-LDAP-Backend = %{version}
Provides:	perl-Kolab-LDAP-Backend-dirservd = %{version}
Provides:	perl-Kolab-LDAP-Backend-slurpd = %{version}
Provides:	perl-Kolab-LDAP-Backend-syncrelpl = %{version}
Provides:	perl-Kolab-Mailer = %{version}
Provides:	perl-Kolab-Util = %{version}
Obsoletes:	perl-Kolab
Obsoletes:	perl-Kolab-Conf
Obsoletes:	perl-Kolab-Cyrus
Obsoletes:	perl-Kolab-DirServ
Obsoletes:	perl-Kolab-LDAP
Obsoletes:	perl-Kolab-LDAP-Backend
Obsoletes:	perl-Kolab-LDAP-Backend-dirservd
Obsoletes:	perl-Kolab-LDAP-Backend-slurpd
Obsoletes:	perl-Kolab-Mailer
Obsoletes:	perl-Kolab-Util
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
 * Kolab contains code used for loading the configuration values from
   kolab.conf and LDAP, as well as functions for logging.

 * Kolab::Conf handles the generation of template files, used by kolabconf.

 * Kolab::Cyrus contains cyrus-related functions, such as adding/deleting
   mailboxes, etc.

 * The Kolab::DirServ module provides a mechanism for Kolab servers to publish
   address book data to a list of peers. These peers receive notification of
   new, updated and removed mailboxes and update their address books
   accordingly.

 * Kolab::LDAP contains functions used to create/delete objects, as well as
   synchronise LDAP and Cyrus.

 * Kolab::LDAP::Backend is basically an interface to the various directory
   service backends that are available.

 * Kolab::LDAP::Backend::ad handles an Active Directory backend to the kolab
   daemon.

 * Kolab::LDAP::Backend::dirservd module for use with Kolab.

 * Kolab::Mailer allows callers to send out various types of email, namely
   plain, multipart & binary through sendmail.

 * Kolab::Util contains several basic utility functions.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

cp %{SOURCE1} dist_conf/mandriva
cp %{SOURCE2} Kolab-LDAP-Backend/syncrepl.pm.in

# cleanup
for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# fix perl_vendordir
perl -pi -e "s|perl_vendorlib|%{perl_vendorlib}|g" dist_conf/mandriva

%build

%configure2_5x \
    --with-dist=mandriva

%make

# make some manpages
mkdir -p man

pod2man Kolab/Kolab.pm > man/Kolab.3
pod2man Kolab-Conf/Conf.pm > man/Kolab::Conf.3
pod2man Kolab-Cyrus/Cyrus.pm > man/Kolab::Cyrus.3
pod2man Kolab-DirServ/DirServ.pm > man/Kolab::DirServ.3
pod2man Kolab-LDAP/LDAP.pm > man/Kolab::LDAP.3
pod2man Kolab-LDAP-Backend/Backend.pm > man/Kolab::LDAP::Backend.3
pod2man Kolab-LDAP-Backend-ad/ad.pm > man/Kolab::LDAP::Backend::ad.3
pod2man Kolab-LDAP-Backend-dirservd/dirservd.pm > man/Kolab::LDAP::Backend::dirservd.3
pod2man Kolab-Mailer/Mailer.pm > man/Kolab::Mailer.3
pod2man Kolab-Util/Util.pm > man/Kolab::Util.3

%install
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m0644 man/*.3 %{buildroot}%{_mandir}/man3/

# cleanup
rm -rf %{buildroot}%{_datadir}/doc/kolab/perl-kolab

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%dir %{perl_vendorlib}/Kolab
%dir %{perl_vendorlib}/Kolab/LDAP
%dir %{perl_vendorlib}/Kolab/LDAP/Backend
%{perl_vendorlib}/Kolab.pm
%{perl_vendorlib}/Kolab/*.pm
%{perl_vendorlib}/Kolab/LDAP/Backend/*.pm
%{perl_vendorlib}/Kolab/LDAP/Backend.pm

%{_mandir}/man3/*
