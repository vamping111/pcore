%global project_name pcore
%global project_description %{expand:
A Python package that provides various core tools}

Name:    python-%project_name
Version: 0.2
Release: 3.ROCKIT5Test%{?dist}
Summary: A Python package that provides various core tools

Group:   Development/Languages
License: MIT
URL:     http://github.com/KonishchevDmitry/%project_name
Source:  http://pypi.python.org/packages/source/p/%project_name/%project_name-%{version}.tar.gz

BuildArch:     noarch

%description %{project_description}


%package -n python%{python3_pkgversion}-%project_name
Summary: %{summary}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: dnf-utils
Obsoletes: python36-%project_name
Conflicts: python36-%project_name

%description -n python%{python3_pkgversion}-%project_name %{project_description}

%prep
%setup -n %project_name-%version -q


%build
%py3_build


%install
%py3_install

%files -n python%{python3_pkgversion}-%project_name
%defattr(-,root,root,-)
%{python3_sitelib}/pcore
%{python3_sitelib}/pcore-*.egg-info
%doc ChangeLog README INSTALL

%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"


%changelog
* Tue Jan 23 2023 Andrey Kulaev <adkulaev@gmail.com> - 0.2-3
- Add centos 8.4 support

* Wed Jan 09 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.2-2
- Add python3 package build for EPEL

* Tue Apr 26 2016 Dmitry Konishchev <konishchev@gmail.com> - 0.2-1
- Add GIGABYTE and TERABYTE constants

* Mon Nov 18 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.1-1
- New package
