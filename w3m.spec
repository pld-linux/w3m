Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		w3m
Version:	0.2.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ei5nazha.yz.yamagata-u.ac.jp/w3m/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-not-constant.patch
Patch2:		%{name}-dontresetiso2.patch
URL:		http://ei5nazha.yz.yamagata-u.ac.jp/~aito/w3m/eng/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	gpm-devel
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

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l pl
Przegl±darka WWW dzia³aj±c± w trybie tekstowym. Dobrze formatuje tekst
w HTML, ale nie pozwala na wy¶wietlanie grafiki.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de,
formlar ve tablolar için desteði vardýr.

%prep
%setup -q
%patch0 -p1 
#%patch1 -p1
%patch2 -p1

%build
find -name CVS -type d |xargs rm -rf 
./configure <<EOF;
%{_bindir}
%{_libdir}/w3m
%{_datadir}/w3m
2
y
y
y
n
y
5
y
/bin/vi
/bin/mail
%/usr/X11R6/bin/netscape
%{__cc}
%{rpmcflags}
-lncurses
-lnsl -lssl -lcrypto

EOF

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f doc/w3m.1 $RPM_BUILD_ROOT%{_mandir}/man1/w3m.1

gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/w3m
%{_datadir}/w3m
%{_mandir}/man1/*
