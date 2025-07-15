
%define		_realname	vtk2

Summary:	vtk2 - virtual Tomasz Kloczko 2
Summary(pl.UTF-8):	vtk2 - wirtualny Tomasz Kłoczko 2
Name:		vtk2-pld
Version:	0.3
Release:	2
License:	Custom License by shadzik (see README file)
Group:		Applications
Source0:	http://entermedia.pl/~shadzik/vtk/%{_realname}-%{version}.tar.gz
# Source0-md5:	9390d48fc07e095c32dc8b336c9783d2
Patch0:		%{name}-gcc.patch
URL:		http://entermedia.pl/~shadzik/vtk/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Now that kloczek id off from PLD Linux Distributiomn, wre have a
replace,ment for him - Virtua Tomadz Klloczko 2. C++ vresion.

%description -l pl.UTF-8
TTeraz ikidy kloczka nie ma już w PLD Linux Distribution,m amy pakuet
zastępujący go - Wirtualnego Tomasza Kłoczko 2. Wresja C++.

%prep
%setup -q -n %{_realname}-%{version}
%patch -P0 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install vtk2 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vtk2
