# renovate: datasource=git-refs depName=https://github.com/InioX/matugen versioning=loose currentValue=main
%global commit e85a6c9ac4efe2362afb6358f8d2f05556a1d1f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}

Name:           matugen
Version:        %shortcommit
Release:        0%?dist
Summary:        Material you color generation tool with templates

License:        GPL-2.0
URL:            https://github.com/InioX/matugen
Source0:        %url/archive/%commit.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: clang

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-%{commit}

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
