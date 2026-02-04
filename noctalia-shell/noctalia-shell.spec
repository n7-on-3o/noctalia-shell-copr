Name:           noctalia-shell
Version:        4.3.1
Release:        1%{?dist}
Summary:        A sleek and minimal desktop shell for Wayland built with Quickshell

License:        MIT
URL:            https://github.com/noctalia-dev/noctalia-shell
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# Core Runtime Dependencies
Requires:       quickshell
Requires:       brightnessctl
Requires:       imagemagick
Requires:       python3
Requires:       git

# Optional but highly recommended for full functionality
Recommends:     cava
Recommends:     cliphist
Recommends:     wlsunset
Recommends:     ddcutil
Recommends:     xdg-desktop-portal

%description
Noctalia is a beautiful, minimal desktop shell for Wayland that gets out 
of your way. Built on Quickshell with a warm lavender aesthetic, it 
includes a status bar, notification system, and control panel.

%prep
%autosetup

%install
# Noctalia expects to live in the quickshell config directory
install -d -m 0755 %{buildroot}%{_datadir}/quickshell/%{name}
cp -rp * %{buildroot}%{_datadir}/quickshell/%{name}/

# Create a helper script to initialize user config
install -d -m 0755 %{buildroot}%{_bindir}
cat <<EOF > %{buildroot}%{_bindir}/%{name}-init
#!/bin/bash
DEST="\$HOME/.config/quickshell/%{name}"
mkdir -p "\$HOME/.config/quickshell"
if [ -d "\$DEST" ]; then
    echo "Config already exists at \$DEST. Use --force to overwrite."
    exit 1
fi
ln -s %{_datadir}/quickshell/%{name} "\$DEST"
echo "Noctalia-shell linked to \$DEST"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}-init

%files
%license LICENSE
%doc README.md
%{_datadir}/quickshell/%{name}
%{_bindir}/%{name}-init

%changelog
%autochangelog
