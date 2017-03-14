%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name is-my-json-valid

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        2.13.1
Release:        2%{?dist}
Summary:        A JSONSchema validator that uses code generation to be extremely fast

License:        MIT
URL:            https://github.com/mafintosh/is-my-json-valid
Source0:        https://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json formats.js index.js require.js \
    %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tape test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md example.js
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.13.1-2
- Built for RHSCL

* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.13.1-1
- Updated with script

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.12.4-1
- Update to 2.12.4

* Tue Nov 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.12.3-1
- Update to 2.12.3

* Wed Nov 11 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.12.2-1
- Initial packaging
