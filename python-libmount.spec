# Created by pyp2rpm-3.3.3
%global pypi_name libmount

Name:           python-%{pypi_name}
Version:        0.9
Release:        1%{?dist}
Summary:        A wrapper around libmount, for reading and manipulating filesystem tables

License:        BSD
URL:            https://github.com/oucs/python-libmount
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description
python-libmount A library for reading and manipulating filesystem tables, such
as /etc/fstab.It uses ctypes to wrap libmount, part of util-linux < reading and
manipulation of the filesystem table should take place in a with block to take
the lock:: from libmount import FilesystemTable with FilesystemTable() as
fstab: print fstab[0].targetA FilesystemTable acts like a list, so you can
slice and ...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python-libmount A library for reading and manipulating filesystem tables, such
as /etc/fstab.It uses ctypes to wrap libmount, part of util-linux < reading and
manipulation of the filesystem table should take place in a with block to take
the lock:: from libmount import FilesystemTable with FilesystemTable() as
fstab: print fstab[0].targetA FilesystemTable acts like a list, so you can
slice and ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Dec 29 2019 Bradford Dabbs <bndabbs@gmail.com> - 0.9-1
- Initial commit
