%global debug_package %{nil}

Name:           iio-niri
# renovate: datasource=github-releases depName=Zhaith-Izaliel/iio-niri
Version:        2.0.0
Release:        0%{?dist}
Summary:        Material you color generation tool with templates

License:       MIT
URL:           https://github.com/Zhaith-Izaliel/iio-niri
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: dbus-devel
Requires:      iio-sensor-proxy

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup

%build
cargo build --release

%install
install -Dpm0755 -t %{buildroot}%{_bindir}/ target/release/%{name}

%files
%{_bindir}/%{name}

%changelog
%autochangelog
