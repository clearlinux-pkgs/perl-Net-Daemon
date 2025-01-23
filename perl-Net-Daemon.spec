#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Net-Daemon
Version  : 0.49
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Net-Daemon-0.49.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Net-Daemon-0.49.tar.gz
Summary  : 'Perl extension for portable daemons'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-Daemon-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Net::Daemon - Perl extension for portable daemons
SYNOPSIS
# Create a subclass of Net::Daemon
require Net::Daemon;
package MyDaemon;
@MyDaemon::ISA = qw(Net::Daemon);

%package dev
Summary: dev components for the perl-Net-Daemon package.
Group: Development
Provides: perl-Net-Daemon-devel = %{version}-%{release}
Requires: perl-Net-Daemon = %{version}-%{release}

%description dev
dev components for the perl-Net-Daemon package.


%package perl
Summary: perl components for the perl-Net-Daemon package.
Group: Default
Requires: perl-Net-Daemon = %{version}-%{release}

%description perl
perl components for the perl-Net-Daemon package.


%prep
%setup -q -n Net-Daemon-0.49
cd %{_builddir}/Net-Daemon-0.49

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::Daemon.3
/usr/share/man/man3/Net::Daemon::Log.3
/usr/share/man/man3/Net::Daemon::Test.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
