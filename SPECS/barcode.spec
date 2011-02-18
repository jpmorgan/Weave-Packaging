Name:           barcode
Version:   	0.98     
Release:        1%{?dist}
Summary:        Converts text strings to printed bars

Group:         	Applications/Text 
License:        GPLv2
URL:            http://directory.fsf.org/project/barcode/ 
Source0:        ftp://ftp.gnu.org/gnu/barcode/barcode-0.98.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:
#Requires:       

%description
GNU barcode is a tool to convert text strings to printed bars. It supports a variety of standard code to represent the strings and creates postscript output. 

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
