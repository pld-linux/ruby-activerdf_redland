Summary:	ActiveRDF adaptor for Redland bindings
Name:		ruby-activerdf_redland
Version:	1.2.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/activerdf_redland-%{version}.gem
# Source0-md5:	c19344995e2a5e336dc3cb63205b1594
Patch0:		%{name}-pathfix.patch
URL:		http://activerdf.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
Requires:	ruby-redland
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ActiveRDF adaptor for Redland bindings.

%prep
%setup -q -c
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .
%patch0 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/created.rid
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/activerdf_redland*
%{ruby_ridir}/*
