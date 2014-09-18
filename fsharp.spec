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

Name:           fsharp
Version:        3.1.1.26
Release:        0
License:        Apache-2.0
Summary:        F# compiler, core library and core tools
Url:            http://fsharp.github.io/fsharp/
Group:          Development/Languages/Other
Source:         %{name}_%{version}+dfsg.orig.tar.gz
BuildRequires:  automake
BuildRequires:  mono-devel >= 3.0.0
BuildArch:      noarch
Patch0:         dont-build-monodroid-monotouch.patch

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
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild

%files
%defattr(-,root,root)
%{_bindir}/fsharpc
%{_bindir}/fsharpi
%{_bindir}/fsharpiAnyCpu
%{_prefix}/lib/mono/2.0/FSharp.Core.dll
%{_prefix}/lib/mono/2.0/FSharp.Core.xml
%{_prefix}/lib/mono/2.0/FSharp.Core.optdata
%{_prefix}/lib/mono/2.0/FSharp.Core.sigdata
%{_prefix}/lib/mono/2.0/policy.2.0.FSharp.Core.dll
%{_prefix}/lib/mono/2.0/policy.2.3.FSharp.Core.dll
%{_prefix}/lib/mono/2.0/policy.2.3.FSharp.Core.dll
%{_prefix}/lib/mono/4.0/FSharp.Build.dll
%{_prefix}/lib/mono/4.0/FSharp.Build.xml
%{_prefix}/lib/mono/4.0/FSharp.Compiler.Interactive.Settings.dll
%{_prefix}/lib/mono/4.0/FSharp.Compiler.Interactive.Settings.xml
%{_prefix}/lib/mono/4.0/FSharp.Compiler.Server.Shared.dll
%{_prefix}/lib/mono/4.0/FSharp.Compiler.Server.Shared.xml
%{_prefix}/lib/mono/4.0/FSharp.Compiler.dll
%{_prefix}/lib/mono/4.0/FSharp.Compiler.xml
%{_prefix}/lib/mono/4.0/FSharp.Core.dll
%{_prefix}/lib/mono/4.0/FSharp.Core.xml
%{_prefix}/lib/mono/4.0/FSharp.Core.optdata
%{_prefix}/lib/mono/4.0/FSharp.Core.sigdata
%{_prefix}/lib/mono/4.0/FSharp.Data.TypeProviders.dll
%{_prefix}/lib/mono/4.0/FSharp.Data.TypeProviders.xml
%{_prefix}/lib/mono/4.0/Microsoft.FSharp.Targets
%{_prefix}/lib/mono/4.0/Microsoft.Portable.FSharp.Targets
%{_prefix}/lib/mono/4.0/fsc.exe
%{_prefix}/lib/mono/4.0/fsi.exe
%{_prefix}/lib/mono/4.0/fsiAnyCpu.exe
%{_prefix}/lib/mono/4.0/policy.2.0.FSharp.Core.dll
%{_prefix}/lib/mono/4.0/policy.2.3.FSharp.Core.dll
%{_prefix}/lib/mono/4.0/policy.3.3.FSharp.Core.dll
%{_prefix}/lib/mono/4.0/policy.4.0.FSharp.Core.dll
%{_prefix}/lib/mono/4.0/policy.4.3.FSharp.Core.dll
%{_prefix}/lib/mono/Microsoft*
%{_prefix}/lib/mono/gac/FSharp.Compiler.Interactive.Settings/
%{_prefix}/lib/mono/gac/FSharp.Compiler.Server.Shared/
%{_prefix}/lib/mono/gac/FSharp.Compiler/
%{_prefix}/lib/mono/gac/FSharp.Core/
%{_prefix}/lib/mono/gac/FSharp.Data.TypeProviders/
%{_prefix}/lib/mono/gac/policy.2.0.FSharp.Core/
%{_prefix}/lib/mono/gac/policy.2.3.FSharp.Core/
%{_prefix}/lib/mono/gac/policy.3.3.FSharp.Core/
%{_prefix}/lib/mono/gac/policy.4.0.FSharp.Core/
%{_prefix}/lib/mono/gac/policy.4.3.FSharp.Core/

