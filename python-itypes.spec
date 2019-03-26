# Created by pyp2rpm-3.3.2
%global pypi_name itypes

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Simple immutable types for python

License:        BSD
URL:            http://github.com/tomchristie/itypes
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Mar 22 2019 Mike DePaulo <mikedep333@redhat.com> - 1.1.0-1
- Initial package.