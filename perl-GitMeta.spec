%define upstream_name GitMeta
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Clone/update many Git repositories using Meta repos
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~mschilli/%{upstream_name}-%{upstream_version}/lib/%{upstream_name}.pm
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Sysadm::Install)

%description
GetMeta allows you to work on dozens of git repositories hosted
on different servers, and update all of your local copies with a
single command. It defines a new syntax, called GMF (git meta format),
to configure many different remote git repository locations and
provides a script, gitmeta-update, to create local copies of all
of these repos or updates them if they already exist. This is useful
to periodically update your local clones while you have an Internet
connection going so they're up-to-date later when you're offline, or
to move to a new system and create clones of all of your favorite
git repos with a single command.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build 
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files 
%doc Changes README
%{_bindir}/gitmeta-update
%{_mandir}/man1/gitmeta-update.1.xz
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 658571
- import perl-GitMeta

