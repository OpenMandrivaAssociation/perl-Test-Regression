%define upstream_name    Test-Regression
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Test library to generate and compare output
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Algorithm::Diff)
BuildRequires: perl(DirHandle)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FileHandle)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


