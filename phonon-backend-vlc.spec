#
# Conditional build:
%bcond_without	qt4	# Qt4 Phonon backend
%bcond_without	qt5	# Qt5 Phonon (Phonon4Qt5) backend

%define		phonon_ver	4.7.0
%define		qt4_ver		4.7.1
%define		qt5_ver		4.7.1
%define		kdever		4.5.5
%define		vlc_ver		2.0.1

Summary:	VLC backend for Phonon
Summary(pl.UTF-8):	Wtyczka VLC dla Phonona
Name:		phonon-backend-vlc
Version:	0.9.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/phonon/phonon-backend-vlc/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5169203a485bf800bdc092e0b6efe646
#URL:		http://
BuildRequires:	cmake >= 2.8.6
BuildRequires:	vlc-devel >= %{vlc_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with qt4}
BuildRequires:	QtCore-devel >= %{qt4_ver}
BuildRequires:	QtGui-devel >= %{qt4_ver}
BuildRequires:	phonon-devel >= %{phonon_ver}
BuildRequires:	qt4-build >= %{qt4_ver}
BuildRequires:	qt4-qmake >= %{qt4_ver}
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	phonon-qt5-devel >= %{phonon_ver}
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-qmake >= %{qt5_ver}
%endif
Requires:	phonon >= %{phonon_ver}
Requires:	vlc >= %{vlc_ver}
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VLC backend for Phonon.

%description -l pl.UTF-8
Wtyczka VLC dla Phonona.

%package -n phonon-qt5-backend-vlc
Summary:	VLC backend for Qt5 Phonon
Summary(pl.UTF-8):	Wtyczka VLC dla Phonona opartego na Qt5
Group:		Libraries
Requires:	phonon-qt5 >= %{phonon_ver}
Requires:	vlc >= %{vlc_ver}
Provides:	qt5-phonon-backend = %{version}

%description -n phonon-qt5-backend-vlc
VLC backend for Qt5 Phonon.

%description -n phonon-qt5-backend-vlc -l pl.UTF-8
Wtyczka VLC dla Phonona opartego na Qt5.

%prep
%setup -q

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake ..
%{__make} -j1
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DPHONON_BUILD_PHONON4QT5=ON
%{__make} -j1
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%files
%defattr(644,root,root,755)
%doc AUTHORS 
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_datadir}/kde4/services/phononbackends/vlc.desktop
%endif

%if %{with qt5}
%files -n phonon-qt5-backend-vlc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/phonon4qt5_backend/phonon_vlc.so
%endif
