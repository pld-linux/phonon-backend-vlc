%define		qtver		4.7.1
%define		kdever		4.5.5
%define		vlcver		1.1.0

Summary:	VLC backend for Phonon
Summary(pl.UTF-8):	Wtyczka VLC dla Phonona
Name:		phonon-backend-vlc
Version:	0.6.2
Release:	1
License:	LGPL 2.1
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{name}/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	1ae8b15594714841d2bcf8c72813a176
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.5.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	vlc-devel >= %{vlcver}
BuildRequires:	rpmbuild(macros) >= 1.600
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VLC backend for Phonon.

%description -l pl.UTF-8
Wtyczka VLC dla Phonona.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop
