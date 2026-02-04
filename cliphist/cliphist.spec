%global goipath         github.com/sentriz/cliphist
Version:                0.7.0
%gometa

Name:           cliphist
Release:        1%{?dist}
Summary:        Wayland clipboard manager with support for multimedia
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang-rpm-macros
BuildRequires:  go-rpm-macros
# cliphist requires wl-clipboard for functionality
Requires:       wl-clipboard

%description
cliphist is a clipboard history manager for Wayland that supports 
both text and images. It is designed to work with any picker 
like dmenu, rofi, or wofi.

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/cliphist %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc readme.md CHANGELOG.md
%{_bindir}/cliphist

%changelog
* Wed Feb 04 2026 Your Name <you@example.com> - 0.7.0-1
- Initial package for cliphist
