%define		phonon_ver	4.7.0
%define		qt_ver		4.7.1
%define		kdever		4.5.5
%define		vlc_ver		2.0.1

Summary:	VLC backend for Phonon
Summary(pl.UTF-8):	Wtyczka VLC dla Phonona
Name:		phonon-backend-vlc
Version:	0.8.2
Release:	2
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	3937517ce4929dea4398ad9834507f97
#URL:		http://
BuildRequires:	cmake >= 2.8.6
BuildRequires:	phonon-devel >= %{phonon_ver}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	vlc-devel >= %{vlc_ver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	phonon >= %{phonon_ver}
Requires:	vlc >= %{vlc_ver}
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
%doc AUTHORS 
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop
