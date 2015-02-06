# Generated from crack-0.1.8.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	crack

Summary:	Really simple JSON and XML parsing, ripped from Merb and Rails
Name:		rubygem-%{rbname}

Version:	0.1.8
Release:	3
Group:		Development/Ruby
License:	MIT
URL:		http://github.com/jnunemaker/crack
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Really simple JSON and XML parsing, ripped from Merb and Rails.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/crack
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/crack/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/data
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/data/*.json


%changelog
* Mon Mar 14 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.8-2
+ Revision: 644662
- regenerate spec with gem2rpm5

* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 0.1.8-1mdv2011.0
+ Revision: 584447
- import rubygem-crack

