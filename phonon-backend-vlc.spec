%define		qtver		4.6.3
%define		kdever		4.4.5
%define		vlcver		1.1.0

Summary:	VLC backend for Phonon
Summary(pl.UTF-8):	Wtyczka VLC dla Phonona
Name:		phonon-backend-vlc
Version:	0.2.0
Release:	1
License:	LGPL 2.1
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	33a1ca367989e306507ea633c99b8df5
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	vlc-devel >= %{vlcver}
BuildRequires:	rpmbuild(macros) >= 1.293
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
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

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
