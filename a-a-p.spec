
Summary: Open Source software construction tool
Name: a-a-p
Version: 1.090
Release: %mkrel 1
Source0: http://belnet.dl.sourceforge.net/sourceforge/a-a-p/aap-%{version}.zip
License: GPL
Group: Development/Other
BuildArchitectures: noarch
BuildRequires: python-devel
Requires: python
Url: http://www.a-a-p.org/
Provides: aap = %{version}-%{release}

%description
A-A-P is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software.  

a-a-p "configuration files" are similar to makefile but they can include
Python.
a-a-p uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched.  a-a-p
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.  Most of the a-a-p logic is object
oriented, including default build rules for many types of program,  they are
all overloadable also.

%prep
%setup -q -n aap-%{version} -c aap-%{version}

%build
# nothing to do !

%install
rm -rf $RPM_BUILD_ROOT
export PYTHONOPTIMIZE=1
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
./aap PREFIX=$RPM_BUILD_ROOT/%{_prefix} install

(
cd $RPM_BUILD_ROOT/%{_bindir}
rm aap
ln -s %{_prefix}/lib/aap/Exec-%{version}/aap aap
)

mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/%{_prefix}/man $RPM_BUILD_ROOT/%{_mandir}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/aap-%{version}
mv $RPM_BUILD_ROOT/%{_prefix}/lib/aap/Exec-%{version}/doc $RPM_BUILD_ROOT/%{_docdir}/aap-%{version}

%check
./aap test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,755)
%{_bindir}/*
%{_prefix}/lib/aap
%{_mandir}/man*/*
%{_docdir}/aap-%{version}




