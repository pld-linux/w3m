Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		w3m
Version:	991203
Release:	1
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ei5nazha.yz.yamagata-u.ac.jp/w3m/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://ei5nazha.yz.yamagata-u.ac.jp/~aito/w3m/eng/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.4-2
BuildRoot:	/tmp/%{name}-%{version}-root

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
sait bien gérer le formatage HTML du texte, les formulaires et les tableaux.

%description -l pl
Przegl±darka WWW dzia³aj±c± w trybie tekstowym. Dobrze formatuje tekst
w HTML, ale nie pozwala na wy¶wietlanie grafiki.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de, formlar ve
tablolar için desteði vardýr.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .wiget

%build
./configure <<EOF;
%{_bindir}
%{_datadir}/w3m
2
y
5
/bin/vi
/bin/mail
/usr/bin/netscape
gcc
$RPM_OPT_FLAGS
-lncurses
-lnsl -lssl -lcrypto

EOF

LDFLAGS="-s"; export LDFLAGS

make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

make install DESTDIR=$RPM_BUILD_ROOT

mv doc/w3m.1 $RPM_BUILD_ROOT%{_mandir}/man1/w3m.1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/w3m
%{_mandir}/man1/*
