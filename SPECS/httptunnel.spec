Name:		httptunnel
Version:	3.0.5 
Release:	1%{?dist}
Summary:	Creates data connection tunneled in HTTP requests	

Group:		Applications/Internet
License:	GPLv3
URL:		http://www.nocrew.org/software/httptunnel.html
Source0:	http://www.nocrew.org/software/httptunnel/httptunnel-3.0.5.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
Creates a bidirectional virtual data connection tunneled via HTTP requests.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_mandir}/*/*



%changelog
* Wed Jan 26 2011 Justin Morgan <jpmorgan@learn.senecac.on.ca> 3.0.5-1
- Created first working spec file for httptunnel source

