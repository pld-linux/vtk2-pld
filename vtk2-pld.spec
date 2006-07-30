Summary:	vtk2 - virtual Tomasz K這czko 2
Summary(pl):	vtk2 - wirtualny Tomasz K這czko 2
Name:		vtk2
Version:	0.2
Release:	1
License:	Custom License by shadzik (see README file)
Group:		Applications
Source0:	http://entermedia.pl/~shadzik/vtk/%{name}-%{version}.tar.gz
# Source0-md5:	0bc7c4965fbc7e784562b3b210db21da
URL:		http://entermedia.pl/~shadzik/vtk/
BuildRequires:	libstdc++-devel
BuildRequires:	make
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual Tomasz K這czko

%description -l pl
Wirtualny Tomasz K這czko

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
