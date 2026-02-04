Name:           cliphist
Version:        0.7.0
Release:        1%{?dist}
Summary:        Wayland clipboard manager with support for multimedia

License:        GPL-3.0-only
URL:            https://github.com/sentriz/cliphist
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang
# Runtime dependencies
Requires:       wl-clipboard
Requires:       fzf

%description
cliphist is a clipboard history "manager" for Wayland that can write 
clipboard changes to a history file and recall history with dmenu, 
wofi, or fzf. It supports both text and images.

%prep
%autosetup

%build
# Ensure we are using the internal vendor directory if it exists, 
# or letting Go download modules if COPR has network access enabled.
export GOFLAGS="-mod=vendor"
go build -o %{name} .

%install
install -Dpm 0755 %{name} %{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
