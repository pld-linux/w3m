Summary:	Text based browser for the world wide web
Summary(de.UTF-8):	Text-Browser für das WWW
Summary(es.UTF-8):	w3m es un paginador, pero puede usarse también como un navegador WWW
Summary(fr.UTF-8):	Navigateur en mode texte pour le world wide web
Summary(pl.UTF-8):	Przeglądarka WWW pracująca w trybie tekstowym
Summary(pt_BR.UTF-8):	O w3m é um paginador, mas pode ser usado também como um navegador WWW
Summary(tr.UTF-8):	Metin ekranda WWW tarayıcı
Name:		w3m
Version:	0.5.2
Release:	5
Epoch:		1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/w3m/%{name}-%{version}.tar.gz
# Source0-md5:	ba06992d3207666ed1bf2dcf7c72bf58
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-nolibs.patch
URL:		http://w3m.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gc-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gpm-devel
BuildRequires:	imlib2-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l de.UTF-8
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten
Support für HTML-Textformatierung, Formulare und Tabellen.

%description -l es.UTF-8
w3m es un paginador similar a las órdenes more y less. Este paquete
también puede utilizarse como un visualizador de páginas WWW en modo
texto.

%description -l fr.UTF-8
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l pl.UTF-8
Przeglądarka WWW działającą w trybie tekstowym. Dobrze formatuje tekst
w HTML, ale nie pozwala na wyświetlanie grafiki.

%description -l pt_BR.UTF-8
O w3m é um paginador similar aos comandos more e less. Este pacote
pode ser ainda utilizado como um visualizador de páginas WWW em modo
texto.

%description -l tr.UTF-8
Metin ekranda çalışan bir WWW tarayıcıdır. Şekil gösteremese de,
formlar ve tablolar için desteği vardır.

%package imgdisplay
Summary:	Image display support for w3m
Summary(pl.UTF-8):	Wsparcie dla wyświetlania obrazków dla w3m
Group:		Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description imgdisplay
Install this package if you want to display images in w3m run on xterm
or Linux framebuffer.

%description imgdisplay -l pl.UTF-8
Zainstaluj ten pakiet jeśli chcesz aby w3m wyświetlał obrazki w
xtermie lub na linuksowym framebufferze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# update acinclude.m4 from aclocal.m4 part
head -n 893 aclocal.m4 > acinclude.m4

%build
cp -f /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-gopher \
	--enable-image="x11,fb,fb+s" \
	--enable-keymap=lynx \
	--with-editor=/bin/vi \
	--with-imagelib="gdk-pixbuf" \
	--with-mailer=/bin/mail \
	--with-browser=/usr/bin/mozilla \
	--with-termlib=ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install install-helpfile \
	DESTDIR=$RPM_BUILD_ROOT

# symlink instead of duplicated file
ln -sf w3mhelp-lynx_en.html $RPM_BUILD_ROOT%{_datadir}/w3m/w3mhelp.html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.html doc/{README,keymap,menu}.* NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/w3m
%attr(755,root,root) %{_libdir}/w3m/inflate
%attr(755,root,root) %{_libdir}/w3m/xface2xpm
%dir %{_libdir}/w3m/cgi-bin
%attr(755,root,root) %{_libdir}/w3m/cgi-bin/*.cgi
%attr(755,root,root) %{_libdir}/w3m/cgi-bin/w3mbookmark
%attr(755,root,root) %{_libdir}/w3m/cgi-bin/w3mhelperpanel
%dir %{_datadir}/w3m
%{_datadir}/w3m/w3mhelp.html
%{_datadir}/w3m/w3mhelp*en.*
%lang(ja) %{_datadir}/w3m/w3mhelp*ja.*
%{_datadir}/w3m/w3mhelp-funcname.pl
%{_mandir}/man1/*.1*
%lang(ja) %{_mandir}/ja/man1/*.1*

%files imgdisplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/w3m/w3mimgdisplay
