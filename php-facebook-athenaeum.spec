%define		php_min_version 5.2
%include	/usr/lib/rpm/macros.php
Summary:	Tools to extend library services to Facebook users through Facebook applications
Name:		php-facebook-athenaeum
Version:	0.1.10
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://facebook-athenaeum.googlecode.com/files/fb-athenaeum-%{version}.tar.gz
# Source0-md5:	c9805c5d03afeeae61383212224cf293
URL:		http://code.google.com/p/facebook-athenaeum/
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Patch0:		json-dep.patch
#Requires:	php-date
Requires:	php-json
Requires:	php-pcre
Requires:	php-simplexml
Suggests:	php-curl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bad depsolver
%define		_noautopear	pear(facebookapi_php5_restlib.php)

# exclude optional php dependencies
%define		_noautophp	php-curl

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Facebook Athenaeum provides libraries an easy to implement Facebook
application to extend library resources to students in Facebook. The
application is easily customized for your institution and includes an
integrated RSS reader, search tools, and a friend locator that allows
Facebook users to record their location in the library so their
friends can find them.

%prep
%setup -q -n fb-athenaeum-%{version}
%patch0 -p1

# we depend on php 5.2
rm -rf libs/facebook_api/jsonwrapper

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a libs/facebook_api $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/facebook_api
