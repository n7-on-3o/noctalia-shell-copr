%global goipath         github.com/sentriz/cliphist
Version:                0.7.0
%gometa

Name:           cliphist
Release:        1%{?dist}
Summary:        Wayland clipboard manager with support for multimedia
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang
BuildRequires:  go-rpm-macros
Requires:       wl-clipboard
Requires:       xdg-utils

%description
cliphist is a clipboard history manager for Wayland that supports 
both text and images. It is designed to work with any picker 
like dmenu, rofi, or wofi.

%prep
%autosetup -n cliphist-%{version}

%build
export GO111MODULE=on
export GOPROXY=https://proxy.golang.org,direct
go build -v -o cliphist .

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp cliphist %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc readme.md
%{_bindir}/cliphist

%changelog
%autochangelog
