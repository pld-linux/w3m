Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW
Summary(es):	w3m es un paginador, pero puede usarse también como un navegador WWW
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(pt_BR):	O w3m é um paginador, mas pode ser usado também como um navegador WWW
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		w3m
Version:	0.3.2.2
Release:	1
Epoch:		1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/w3m/%{name}-%{version}.tar.gz
Patch0:		%{name}-dontresetiso2.patch
Patch1:		%{name}-gzip_fallback.patch
Patch2:		%{name}-nolibs.patch
URL:		http://w3m.sourceforge.net/
BuildRequires:	gpm-devel
BuildRequires:	imlib-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten
Support für HTML-Textformatierung, Formulare und Tabellen.

%description -l es
w3m es un paginador similar a las órdenes more y less. Este paquete
también puede utilizarse como un visualizador de páginas WWW en modo
texto.

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l pl
Przegl±darka WWW dzia³aj±c± w trybie tekstowym. Dobrze formatuje tekst
w HTML, ale nie pozwala na wy¶wietlanie grafiki.

%description -l pt_BR
O w3m é um paginador similar aos comandos more e less. Este pacote
pode ser ainda utilizado como um visualizador de páginas WWW em modo
texto.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de,
formlar ve tablolar için desteði vardýr.

%package imgdisplay
Summary:	Image display support for w3m
Summary(pl):	Wsparcie dla wy¶wietlania obrazków dla w3m
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description imgdisplay
Install this package if you want to display images in xterm(!!!) w3m
session.

%description imgdisplay -l pl
Zainstaluj ten pakiet je¶li chcesz aby w3m wy¶wietla³ obrazki w
xtermie(!!!).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
use_ipv6=y; export use_ipv6
./configure <<EOF
%{_bindir}
%{_libdir}/w3m
%{_datadir}/w3m
%{_mandir}
%{_sysconfdir}/w3m
2
y
5
y
y
y
y
y
y
n
y
y
y
y
y
y
y
/bin/vi
/usr/X11R6/bin/netscape
%{__cc}
%{rpmcflags}
-lncurses
%{rpmldflags}
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install install-helpfile DESTDIR=$RPM_BUILD_ROOT

# symlink instead of duplicated file
ln -sf w3mhelp-lynx_en.html $RPM_BUILD_ROOT%{_datadir}/w3m/w3mhelp.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html doc/{README,keymap,menu}.* NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/w3m
%attr(755,root,root) %{_libdir}/w3m/*.cgi
%attr(755,root,root) %{_libdir}/w3m/inflate
%attr(755,root,root) %{_libdir}/w3m/w3mbookmark
%attr(755,root,root) %{_libdir}/w3m/w3mhelperpanel
%attr(755,root,root) %{_libdir}/w3m/xface2xpm
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
