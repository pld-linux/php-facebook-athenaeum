Summary:	Tools to extend library services to Facebook users through Facebook applications
Name:		php-facebook-athenaeum
Version:	0.1.8
Release:	0.2
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://facebook-athenaeum.googlecode.com/files/fb-athenaeum-%{version}.tar.gz
# Source0-md5:	a571a6ee843ebebb1740d42a14779783
URL:		http://code.google.com/p/facebook-athenaeum/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:5.0.0
Requires:	php-json
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Facebook Athenaeum provides libraries an easy to implement Facebook
application to extend library resources to students in Facebook. The
application is easily customized for your institution and includes an
integrated RSS reader, search tools, and a friend locator that allows
Facebook users to record their location in the library so their
friends can find them.

%prep
%setup -q -n fb-athenaeum-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a libs/facebook_api $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/facebook_api
