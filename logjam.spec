Summary:	The GTK+2-client for LiveJournal
Summary(pl):	Oparty na GTK+2 klient do LiveJournala
Name:		logjam
Version:	4.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://neugierig.org/software/logjam/download/%{name}-%{version}.tar.bz2
# Source0-md5:	ccae70dc36644cd1529c581443484ebe
Source1:	%{name}.desktop
Patch0:		%{name}-locale_names.patch
URL:		http://logjam.danga.com/
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtkhtml-devel >= 3.0
BuildRequires:	gtkspell-devel >= 2.0
BuildRequires:	intltool
BuildRequires:	librsvg-devel >= 2.2.3
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	sqlite3-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the new GTK+2 client for LiveJournal
(http://www.livejournal.com/).

%description -l pl
To jest nowy, oparty na GTK+2, klient dla LiveJournala
(http://www.livejournal.com/).

%prep
%setup -q 
%patch0 -p1
mv -f po/{uk_UA,uk}.po
mv -f po/{ru_RU,ru}.po
mv -f po/en_US{.UTF-8,}.po

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--with-xmms=runtime \
	--with-sqlite3
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
