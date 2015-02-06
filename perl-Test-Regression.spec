%define upstream_name    Test-Regression
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.07
Release:	3

Summary:	Test library to generate and compare output
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Regression-0.07.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)
BuildRequires:	perl(DirHandle)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
Using the various Test:: modules you can compare the output of a function
against what you expect. However if the output is complex and changes from
version to version, maintenance of the expected output could be costly.
This module allows one to use the test code to generate the expected
output, so that if the differences with model output are expected, one can
easily refresh the model output.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 658567
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 657845
- rebuild for updated spec-helper

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 602393
- update to new version 0.06

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 553066
- import perl-Test-Regression


* Wed Jul 14 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

