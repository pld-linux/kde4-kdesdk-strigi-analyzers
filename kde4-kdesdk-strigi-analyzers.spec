#
# TODO:
# - add man files
#
%define		orgname		kdesdk-strigi-analyzers
%define		_state		stable
%define		qtver		4.8.1

Summary:	Strigi Analyzers
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	fb9f07e55f0d8efb061fe282ba876b36
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	strigi-devel >= 0.7.2
Obsoletes:	kde4-kdesdk-strigi-analyzer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strigi Analyzers.

%description -l pl.UTF-8
Strigi Analyzers.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/strigi/strigila_diff.so
%attr(755,root,root) %{_libdir}/strigi/strigita_ts.so
%attr(755,root,root) %{_libdir}/strigi/strigila_po.so
%attr(755,root,root) %{_libdir}/strigi/strigita_xlf.so
%{_datadir}/strigi/fieldproperties/strigi_translation.fieldproperties
