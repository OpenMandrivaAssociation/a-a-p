Summary:	Construction tool
Name:		a-a-p
Version:	1.093
Release:	1
Source0:	http://heanet.dl.sourceforge.net/project/%{name}/Aap/1.093/aap-%{version}.zip
License:	GPLv2
Group:		Development/Other

BuildArch:	noarch
BuildRequires:	python-devel
Requires:	python
Url:		http://www.a-a-p.org/
Provides:	aap = %{version}-%{release}

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


%install
export PYTHONOPTIMIZE=1
mkdir -p %{buildroot}/%{_prefix}
./aap PREFIX=%{buildroot}/%{_prefix} install

(
cd %{buildroot}/%{_bindir}
rm aap
ln -s %{_prefix}/lib/aap/Exec-%{version}/aap aap
)

mkdir -p %{buildroot}/%{_datadir}
mv %{buildroot}/%{_prefix}/man %{buildroot}/%{_mandir}
mkdir -p %{buildroot}/%{_docdir}/aap-%{version}
mv %{buildroot}/%{_prefix}/lib/aap/Exec-%{version}/doc %{buildroot}/%{_docdir}/aap-%{version}

%check
./aap test


%files
%{_bindir}/*
%{_prefix}/lib/aap
%{_mandir}/man*/*
%{_docdir}/aap-%{version}


