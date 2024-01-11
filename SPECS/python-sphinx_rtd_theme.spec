%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_py3 1
%global with_py2 0
%endif

%global srcname sphinx_rtd_theme

Name:           python-%{srcname}
Version:        0.3.1
Release:        3%{?dist}
Summary:        Sphinx theme for readthedocs.org

License:        MIT
URL:            https://github.com/snide/sphinx_rtd_theme
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?with_py2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if 0%{?with_py3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%if 0%{?with_py2}
%package -n python2-%{srcname}
Summary:        Sphinx theme for readthedocs.org
Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.
%endif

%if 0%{?with_py3}
%package -n python3-%{srcname}
Summary:        Sphinx theme for readthedocs.org
Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.
%endif

%prep
%setup -q -c

# Prepare for python3 build
cp -a %{srcname}-%{version} python3-%{srcname}-%{version}

%build
%if 0%{?with_py2}
# Python 2 build
pushd %{srcname}-%{version}
%py2_build
popd
%endif

%if 0%{?with_py3}
# Python 3 build
pushd python3-%{srcname}-%{version}
%py3_build
popd
%endif

%install
%if 0%{?with_py2}
# Python 2 install
pushd %{srcname}-%{version}
%py2_install
popd

# Don't use the bundled fonts
pushd %{buildroot}/%{python2_sitelib}/%{srcname}/static/fonts
rm fontawesome-webfont.* Lato*.ttf RobotoSlab*.ttf
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2 .
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Bold.ttf .
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Regular.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Bold.ttf .
ln -s %{_datadir}/fonts/lato/Lato-BoldItalic.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Italic.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Regular.ttf .
popd
%endif

%if 0%{?with_py3}
# Python 3 install
pushd python3-%{srcname}-%{version}
%py3_install
popd

# Don't use the bundled fonts
pushd %{buildroot}/%{python3_sitelib}/%{srcname}/static/fonts
rm fontawesome-webfont.* Lato*.ttf RobotoSlab*.ttf
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2 .
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Bold.ttf .
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Regular.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Bold.ttf .
ln -s %{_datadir}/fonts/lato/Lato-BoldItalic.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Italic.ttf .
ln -s %{_datadir}/fonts/lato/Lato-Regular.ttf .
popd
%endif

%if 0%{?with_py2}
%files -n python2-%{srcname}
%doc %{srcname}-%{version}/README.rst
%license %{srcname}-%{version}/LICENSE
%{python2_sitelib}/%{srcname}*
%endif

%if 0%{?with_py3}
%files -n python3-%{srcname}
%doc python3-%{srcname}-%{version}/README.rst
%license python3-%{srcname}-%{version}/LICENSE
%{python3_sitelib}/%{srcname}*
%endif

%changelog
* Mon Jun 18 2018 Lumír Balhar <lbalhar@redhat.com> - 0.3.1-3
- Python 2 subpackage disabled

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.7

* Wed May  2 2018 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- New upstream version

* Sat Apr  7 2018 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar  6 2017 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- New upstream version

* Sat Mar  4 2017 Jerry James <loganjerry@gmail.com> - 0.2.2-1
- New upstream version

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 0.2.0-1
- New upstream version
- Unbundle the roboto fonts

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.1.9-3
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 0.1.9-1
- Comply with latest python packaging guidelines

* Tue Nov 24 2015 Jerry James <loganjerry@gmail.com> - 0.1.9-1
- New upstream version

* Mon Nov 16 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.1.8-4
- Add Requires: fontawesome-web (rhbz#1282297)

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 0.1.8-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- New upstream version
- Unbundle the Lato fonts

* Wed Mar 11 2015 Jerry James <loganjerry@gmail.com> - 0.1.7-1
- New upstream version

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.1.6-2
- Use license macro

* Thu Jul  3 2014 Jerry James <loganjerry@gmail.com> - 0.1.6-1
- Initial RPM
