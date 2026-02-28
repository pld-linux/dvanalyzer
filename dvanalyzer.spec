Summary:	Technical and tag information about video or audio file (CLI)
Summary(pl.UTF-8):	Informacje techniczne i oznaczenia dotyczące pliku wideo lub audio (CLI)
Name:		dvanalyzer
Version:	1.4.2
Release:	2
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://mediaarea.net/download/source/dvanalyzer/%{version}/%{name}_%{version}.tar.xz
# Source0-md5:	207b881f4762cc06cb5652fdddcb60ee
URL:		https://mediaarea.net/DVAnalyzer
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libmediainfo-devel >= 0.7.99
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libzen-devel >= 0.4.37
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libmediainfo >= 0.7.99
Requires:	libzen >= 0.4.37
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DV Analyzer is a technical quality control and reporting tool that
examines DV streams in order to report errors in the tape-to-file
transfer process, such as video error concealment information, invalid
audio samples, timecode inconsistency, inconsistent use of arbitrary
bits in video DIF blocks, and DIF structural problems. DV Analyzer
also reports on patterns within DV streams such as changes in DV time
code, changes in recording date and time markers, first and last frame
markers within individual recordings, and more.

%description -l pl.UTF-8
DV Analyzer to narzędzie do sprawdzania i raportowania jakości
technicznej strumieni DV w celu raportowania błędów w procesie
przenoszenia z taśmy do pliku, takie jak informacje o ukrywaniu
błędów, błędne próbki dźwiękowe, niezgodność kodowania czasu,
niespójne użycie określonych bitów w blokach DIF obrazu oraz problemy
ze strukturą DIF. DV Analyzer informuje także o wzorcach w
strumieniach DV, takich jak zmiany w kodowaniu czasu, zmiany w
znacznikach daty i czasu nagrania, znaczniki pierwszej i ostatniej
klatki w poszczególnych nagraniach itd.

%package gui
Summary:	Technical and tag information about video or audio file (GUI)
Summary(pl.UTF-8):	Informacje techniczne i oznaczenia dotyczące pliku wideo lub audio (GUI)
Group:		X11/Applications/Multimedia
Requires:	libmediainfo >= 0.7.99
Requires:	libzen >= 0.4.37

%description gui
DV Analyzer is a technical quality control and reporting tool that
examines DV streams in order to report errors in the tape-to-file
transfer process, such as video error concealment information, invalid
audio samples, timecode inconsistency, inconsistent use of arbitrary
bits in video DIF blocks, and DIF structural problems. DV Analyzer
also reports on patterns within DV streams such as changes in DV time
code, changes in recording date and time markers, first and last frame
markers within individual recordings, and more.

%description gui -l pl.UTF-8
DV Analyzer to narzędzie do sprawdzania i raportowania jakości
technicznej strumieni DV w celu raportowania błędów w procesie
przenoszenia z taśmy do pliku, takie jak informacje o ukrywaniu
błędów, błędne próbki dźwiękowe, niezgodność kodowania czasu,
niespójne użycie określonych bitów w blokach DIF obrazu oraz problemy
ze strukturą DIF. DV Analyzer informuje także o wzorcach w
strumieniach DV, takich jak zmiany w kodowaniu czasu, zmiany w
znacznikach daty i czasu nagrania, znaczniki pierwszej i ostatniej
klatki w poszczególnych nagraniach itd.

%prep
%setup -q -n AVPS_DV_Analyzer
%undos *.html *.txt Release/*.txt
chmod 644 *.html *.txt Release/*.txt

%build
# build CLI
cd Project/GNU/CLI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
# now build GUI
cd ../../../Project/GNU/GUI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# Qt5Core with -reduce-relocations requires PIC code
%configure \
	CXXFLAGS="%{rpmcxxflags} -fPIC"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Project/GNU/CLI install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Project/GNU/GUI install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_iconsdir}/hicolor/128x128/apps}
cp -p Project/GNU/GUI/dvanalyzer-gui.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p Source/Resource/Image/AVPS/logo_sign_alpha_square.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps/dvanalyzer.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.html History_CLI.txt Release/ReadMe_CLI_Linux.txt
%attr(755,root,root) %{_bindir}/dvanalyzer

%files gui
%defattr(644,root,root,755)
%doc License.html History_GUI.txt Release/ReadMe_GUI_Linux.txt
%attr(755,root,root) %{_bindir}/dvanalyzer-gui
%{_desktopdir}/dvanalyzer-gui.desktop
%{_iconsdir}/hicolor/128x128/apps/dvanalyzer.png
