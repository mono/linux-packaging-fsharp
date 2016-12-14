#
# spec file for package fsharp (Version 3.1.1.26)
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global _default_patch_fuzz 2

Name:           fsharp
Version:        4.0.1.20
Release:        0.xamarin.1
License:        Apache-2.0
Summary:        F# compiler, core library and core tools
Url:            http://fsharp.github.io/fsharp/
Group:          Development/Languages/Other
Source:         %{name}_%{version}.orig.tar.bz2
BuildRequires:  automake
BuildRequires:  nuget
BuildRequires:  mono-devel >= 4.0.0
BuildRequires:  mono-wcf   >= 4.0.0
BuildArch:      noarch
Patch0:		fix-bootstrap-src-targets-path.patch

%description
F# is a mature, open source, functional-first programming language
which empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code. It is used in
a wide range of application areas and is available across multiple
platforms.

%prep
%setup -q
%patch0 -p1

%build
autoreconf
%configure --libexecdir=%{_prefix}/lib --libdir=%{_prefix}/lib
make

%install
%make_install
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monodroid
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monotouch

%files
%defattr(-,root,root)
%{_bindir}/fsharp*
%{_prefix}/lib/mono/4.5/*
%{_prefix}/lib/mono/fsharp/
%{_prefix}/lib/mono/Microsoft*
%{_prefix}/lib/mono/gac/FSharp.*/
%{_prefix}/lib/mono/gac/policy.*.FSharp.Core/
%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/
"%{_prefix}/lib/mono/Reference Assemblies/Microsoft/FSharp/"
