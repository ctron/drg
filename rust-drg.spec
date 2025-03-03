# Generated by rust2rpm 16
%bcond_without check
%global __cargo_skip_build 0

%global crate drg

Name:           rust-%{crate}
Version:        0.4.1
Release:        1.20210406114535497168.main.19.ga7278ba%{?dist}
Summary:        Command line tool to interact with a drogue-cloud instance

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/drg
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Command line tool to interact with a drogue-cloud instance.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/drg

%prep
%autosetup -p1 -n %{crate}-%{version}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Apr 06 2021 Jens Reimann <jreimann@redhat.com> - 0.3.0-1.20210406114535497168.main.19.ga7278ba
- Drop github actions snap workflow (Jens Reimann)
- workflow name (Jean-Baptiste Trystram)
- do snap build only on tags. Fixes #36 (Jean-Baptiste Trystram)
- merge update and edit and use the file flag as differenciator (Jean-Baptiste Trystram)
- update doc (Jean-Baptiste Trystram)
- added update subcommand to load json file (Jean-Baptiste Trystram)
- rename artifact to match published snap file name (Jean-Baptiste Trystram)
- fix snap file path (Jean-Baptiste Trystram)
- Fix reference (Jens Reimann)
- Set id for build step (Jens Reimann)
- Try different syntax (Jens Reimann)
- Automatically publish (Jens Reimann)
- experiment with snaps (Jens Reimann)
- Create parent directory of configuration if it doesn't exists (Jens Reimann)
- update Cargo.lock (Jens Reimann)
- add the actual Cargo.lock (Jens Reimann)
- commit Cargo.lock as this is a binary (Jens Reimann)
- make use of the default app setting (Jean-Baptiste Trystram)
- Automatic browser open to login (#28) (Vedang Joshi)

