Name:		logjam
Version:	4.2.3
Summary:	The GTK2-client for LiveJournal
Release:	0
Source0:	http://logjam.danga.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	9eec6b02a8ac34ade861f5c6b19cf3e1
Source1:	%{name}.desktop
BuildRequires: curl-devel
BuildRequires: gtk+2-devel
BuildRequires: gtkspell-devel
URL:		http://logjam.danga.com/
License:	GPL
Group:		X11/Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the new GTK2 client for LiveJournal
(http://www.livejournal.com).

%prep
%setup -q 

%build
%configure --with-xmms=runtime
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/logjam
%{_mandir}/man1/logjam.1.gz
%{_datadir}/applications/logjam.desktop
%{_datadir}/locale/*
%{_datadir}/pixmaps/logjam*.png
%doc README AUTHORS COPYING INSTALL NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT
