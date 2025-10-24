%global debug_package %{nil}

Name:           matugen
# renovate: datasource=github-releases depName=InioX/matugen
Version:        2.4.1
Release:        0%{?dist}
Summary:        Material you color generation tool with templates

License:        GPL-2.0
URL:            https://github.com/InioX/matugen
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: clang

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup

%build
# using clang here because seems that one of the dependencies fails to build with the default GCC configuration from fedora
CC=clang CXX=clang cargo build --release --locked

%install
install -Dpm0755 -t %{buildroot}%{_bindir}/ target/release/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
