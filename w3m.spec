# Conditional build:
%bcond_without	image 	# build without image support

Summary:	Text based browser for the world wide web
Summary(de.UTF-8):	Text-Browser für das WWW
Summary(es.UTF-8):	w3m es un paginador, pero puede usarse también como un navegador WWW
Summary(fr.UTF-8):	Navigateur en mode texte pour le world wide web
Summary(pl.UTF-8):	Przeglądarka WWW pracująca w trybie tekstowym
Summary(pt_BR.UTF-8):	O w3m é um paginador, mas pode ser usado também como um navegador WWW
Summary(tr.UTF-8):	Metin ekranda WWW tarayıcı
Name:		w3m
Version:	0.5.3
Release:	10
Epoch:		1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://downloads.sourceforge.net/w3m/%{name}-%{version}.tar.gz
# Source0-md5:	1b845a983a50b8dec0169ac48479eacc
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-0.5.3-parallel-make.patch
Patch3:		%{name}-0.5.2-fix_gcc_error.patch
Patch4:		%{name}-gc.patch
Patch5:		format-security.patch
Patch6:		ac-gettext.patch
Patch7:		openssl.patch
Patch8:		%{name}-configure.patch
Patch9:		%{name}-x11.patch
Patch10:	imlib2-pc.patch
Patch11:	parallel-build.patch
URL:		http://w3m.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gc-devel
BuildRequires:	gettext-tools
BuildRequires:	gpm-devel
%if %{with image}
BuildRequires:	imlib2-devel >= 1.1.0
BuildRequires:	xorg-lib-libX11-devel
%endif
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
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
Summary(pl.UTF-8):	Wyświetlanie obrazków dla w3m
Group:		Applications/Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	imlib2 >= 1.1.0

%description imgdisplay
Install this package if you want to display images in w3m run on xterm
or Linux framebuffer.

%description imgdisplay -l pl.UTF-8
Ten pakiet pozwala przeglądarce w3m wyświetlać obrazki w xtermie lub
na linuksowym framebufferze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%{__sed} '/^AC_PROG_CXX$/d' -i configure.ac

%build
cp -f /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure \
	mkdir_p="mkdir -p" \
	--enable-gopher \
%if %{with image}
	--enable-image="x11,fb,fb+s" \
	--with-imagelib="imlib2" \
%else
	--disable-image \
%endif
	--enable-keymap=lynx \
	--with-editor=/bin/vi \
	--with-mailer=/bin/mail \
	--with-browser=%{_bindir}/mozilla \
	--with-termlib=ncurses

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
%attr(755,root,root) %{_bindir}/w3m
%attr(755,root,root) %{_bindir}/w3mman
%dir %{_libexecdir}/w3m
%attr(755,root,root) %{_libexecdir}/w3m/inflate
%attr(755,root,root) %{_libexecdir}/w3m/xface2xpm
%dir %{_libexecdir}/w3m/cgi-bin
%attr(755,root,root) %{_libexecdir}/w3m/cgi-bin/*.cgi
%attr(755,root,root) %{_libexecdir}/w3m/cgi-bin/w3mbookmark
%attr(755,root,root) %{_libexecdir}/w3m/cgi-bin/w3mhelperpanel
%dir %{_datadir}/w3m
%{_datadir}/w3m/w3mhelp.html
%{_datadir}/w3m/w3mhelp*en.*
%lang(ja) %{_datadir}/w3m/w3mhelp*ja.*
%{_datadir}/w3m/w3mhelp-funcname.pl
%{_mandir}/man1/w3m.1*
%{_mandir}/man1/w3mman.1*
%lang(ja) %{_mandir}/ja/man1/w3m.1*

%if %{with image}
%files imgdisplay
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/w3m/w3mimgdisplay
%endif
