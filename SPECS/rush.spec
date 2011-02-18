Name:           rush
Version:        1.7
Release:        1%{?dist}
Summary:        Gives complete user control over remote access command lines

Group:          Applications/System
License:        GPLv3
URL:            http://savannah.gnu.org/projects/rush
Source0:        ftp://ftp.gnu.org/gnu/rush/rush-1.7.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       
Requires(post): info
Requires(preun): info


%description
Rush is a Restricted User Shell. 

It is intended for use with remote access programs. 

Rush gives you complete control over the command lines that users execute

%prep
%setup -q

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/rush.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/rush.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/rush.mo
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/rush.mo
%{_bindir}/*
%{_sbindir}/*
%{_sysconfdir}/*
%{_datadir}/rush/rush-po.awk
%{_infodir}/rush.info.gz

%changelog
* Wed Jan 26 2011 Justin Morgan <jpmorgan@learn.senecac.on.ca> 1.7-1
- Created first working spec file for Rush source

