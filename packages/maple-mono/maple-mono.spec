%global fontlicense OFL-1.1
%global fontlicenses maplemono-variable/LICENSE.txt

%global fontfamily0 Maple Mono
%global fontsummary0 Open source monospace font with round corner and ligatures for IDE and terminal, fine-grained customization options.
%global fonts0 maplemono-variable/*.ttf

%global fontfamily1 Maple Mono NF
%global fontsummary1 Open source monospace font with round corner, ligatures and Nerd-Font icons for IDE and terminal, fine-grained customization options.
%global fonts1 maplemono-nf/*.ttf

# renovate: datasource=github-releases depName=subframe7536/maple-font versioning=loose
Version: 7.9
Release: 0%{?dist}

Url: https://github.com/subframe7536/maple-font
Source0: %{url}/releases/download/v%{version}/MapleMono-Variable.zip
Source1: %{url}/releases/download/v%{version}/MapleMono-NF.zip

BuildRequires: fontpackages-devel
Requires: fontconfig
Requires(post): fontconfig

%fontpkg -a

%prep
unzip $RPM_SOURCE_DIR/MapleMono-Variable.zip -d maplemono-variable
unzip $RPM_SOURCE_DIR/MapleMono-NF.zip -d maplemono-nf

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
