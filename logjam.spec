Summary:	The GTK+2-client for LiveJournal
Summary(pl):	Oparty na GTK+2 klient do LiveJournala
Name:		logjam
Version:	4.3.0
%define pre pre1
Release:	0.%{pre}.1
License:	GPL
Group:		X11/Applications
Source0:	http://logjam.danga.com/download/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	1914079d642c0114d43170d9625663ae
Source1:	%{name}.desktop
URL:		http://logjam.danga.com/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtkhtml-devel >= 3.0
BuildRequires:	gtkspell-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.2.3
BuildRequires:	libxml2-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the new GTK+2 client for LiveJournal
(http://www.livejournal.com/).

%description -l pl
To jest nowy, oparty na GTK+2, klient dla LiveJournala
(http://www.livejournal.com/).

%prep
%setup -q 

%build
%configure \
	--with-xmms=runtime
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog doc
%attr(755,root,root) %{_bindir}/logjam
%{_mandir}/man1/logjam.1*
%{_desktopdir}/logjam.desktop
%{_pixmapsdir}/logjam*.png
