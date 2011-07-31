# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Perms
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Permissions System
Name:		php-horde-Horde_Perms
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	e9bbf7140a6ab93c5c3c2695807a487c
URL:		https://github.com/horde/horde/tree/master/framework/Perms/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Db < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Group < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_DataTree
Suggests:	php-horde-Horde_Tree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/DataTree.*) pear(Horde/Tree.*)

%description
The Perms package provides an interface to the Horde permissions
system.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Perms.php
%{php_pear_dir}/Horde/Perms
%{php_pear_dir}/data/Horde_Perms
