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
Version:	4.1.25
Release:	0.xamarin.1
License:        Apache-2.0
Summary:        F# compiler, core library and core tools
Url:            http://fsharp.github.io/fsharp/
Group:          Development/Languages/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  nuget
BuildRequires:  referenceassemblies-pcl
BuildRequires:  mono-devel >= 4.0.0
BuildRequires:  mono-wcf   >= 4.0.0
BuildArch:      noarch
Patch0:		fix-bootstrap-src-targets-path.patch
Patch2:		fsharp-fix-mdb-support.patch
Patch3:		fsharp-fix-xbuild-check.patch
Patch4:		fsharp-install-netsdk-targets.patch

%define _use_internal_dependency_generator 0
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v 2\\.0\\.5 | grep -v \\(System.Collections\\) | grep -v \\(System.Collections.Immutable\\) | grep -v \\(System.Diagnostics.Debug\\) | grep -v \\(System.Dynamic.Runtime\\) | grep -v \\(System.Globalization\\) | grep -v \\(System.IO\\) | grep -v \\(System.Linq\\) | grep -v \\(System.Linq.Expressions\\) | grep -v \\(System.Linq.Queryable\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.Reflection\\) | grep -v \\(System.Reflection.Extensions\\) | grep -v \\(System.Reflection.Primitives\\) | grep -v \\(System.Resources.ResourceManager\\) | grep -v \\(System.Runtime\\) | grep -v \\(System.Runtime.Extensions\\) | grep -v \\(System.Runtime.InteropServices\\) | grep -v \\(System.Runtime.Numerics\\) | grep -v \\(System.Text.Encoding\\) | grep -v \\(System.Text.Encoding.Extensions\\) | grep -v \\(System.Text.RegularExpressions\\) | grep -v \\(System.Threading\\) | grep -v \\(System.Threading.Tasks\\) | grep -v \\(System.Threading.Tasks.Parallel\\) | grep -v \\(System.Collections.Concurrent\\)'
%else
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v 2\\.0\\.5 | grep -v \\(System.Collections\\) | grep -v \\(System.Collections.Immutable\\) | grep -v \\(System.Diagnostics.Debug\\) | grep -v \\(System.Dynamic.Runtime\\) | grep -v \\(System.Globalization\\) | grep -v \\(System.IO\\) | grep -v \\(System.Linq\\) | grep -v \\(System.Linq.Expressions\\) | grep -v \\(System.Linq.Queryable\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.Reflection\\) | grep -v \\(System.Reflection.Extensions\\) | grep -v \\(System.Reflection.Primitives\\) | grep -v \\(System.Resources.ResourceManager\\) | grep -v \\(System.Runtime\\) | grep -v \\(System.Runtime.Extensions\\) | grep -v \\(System.Runtime.InteropServices\\) | grep -v \\(System.Runtime.Numerics\\) | grep -v \\(System.Text.Encoding\\) | grep -v \\(System.Text.Encoding.Extensions\\) | grep -v \\(System.Text.RegularExpressions\\) | grep -v \\(System.Threading\\) | grep -v \\(System.Threading.Tasks\\) | grep -v \\(System.Threading.Tasks.Parallel\\) | grep -v \\(System.Collections.Concurrent\\)'
%endif

%description
F# is a mature, open source, functional-first programming language
which empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code. It is used in
a wide range of application areas and is available across multiple
platforms.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf
%configure --libexecdir=%{_prefix}/lib --libdir=%{_prefix}/lib
make

%install
%make_install
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monodroid
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/monotouch
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.sigdata ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.optdata ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Compiler.Interactive.Settings.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/

%files
%defattr(-,root,root)
%{_bindir}/fsharp*
%{_prefix}/lib/mono/4.5/*
%{_prefix}/lib/mono/fsharp/
%{_prefix}/lib/mono/Microsoft*
%{_prefix}/lib/mono/gac/FSharp.*/
%{_prefix}/lib/mono/gac/policy.*.FSharp.Core/
%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/
