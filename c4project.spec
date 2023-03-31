Name:           c4project
Summary:        Useful CMake scripts
# This project has never been assigned a version. The author really intends it
# for use as a git submodule rather than for system-wide installation.
Group:          Development
Version:        20211228
Release:        2
URL:            https://github.com/biojppm/cmake/
# The entire source is MIT, except Toolchain-PS4.cmake and
# Toolchain-XBoxOne.cmake, which are ASL 2.0.
License:        MIT and ASL 2.0
Source0:        https://github.com/biojppm/cmake/archive/refs/heads/master.tar.gz/cmake-20211228.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       git-core

%description
Useful CMake scripts

%prep
%autosetup -n cmake-master -p1

# For now, we elect not to install the “bm-xp” browser-based benchmark explorer
# tool. It would be inconvenient to package this in a way that was useful in
# practice, and it’s not required by any of the CMake macros that are the real
# point of packaging this.
rm -rvf 'bm-xp'


%build
# Nothing to do


%install
install -t %{buildroot}%{_datadir}/cmake/%{name} -D -p -m 0644 *


%files
%license LICENSE.txt
%doc README.md

%{_datadir}/cmake/%{name}
