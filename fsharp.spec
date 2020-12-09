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
Version:	5.0.0.0
Release:	0.xamarin.7
License:        Apache-2.0
Summary:        F# compiler, core library and core tools
Url:            http://fsharp.github.io/fsharp/
Group:          Development/Languages/Other
Source0:        %{name}-%{version}.tar.xz
Source1:        wrapper.sh
Source2:        Microsoft.FSharp.rtf
Source3:        Microsoft.Portable.FSharp.rtf
BuildRequires:  automake
BuildRequires:  nuget
BuildRequires:  msbuild
BuildRequires:  libicu-devel
BuildRequires:  referenceassemblies-pcl
BuildRequires:  mono-devel >= 4.0.0
BuildRequires:  mono-wcf   >= 4.0.0
BuildArch:      noarch
Patch0:		fsharp-netfx-multitarget.patch
Patch1:		fsharp-portable-pdb.patch

%define _use_internal_dependency_generator 0
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/redhat/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v 2\\.0\\.5 | grep -v \\(System.Collections\\) | grep -v \\(System.Collections.Immutable\\) | grep -v \\(System.Diagnostics.Debug\\) | grep -v \\(System.Dynamic.Runtime\\) | grep -v \\(System.Globalization\\) | grep -v \\(System.IO\\) | grep -v \\(System.Linq\\) | grep -v \\(System.Linq.Expressions\\) | grep -v \\(System.Linq.Queryable\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.Reflection\\) | grep -v \\(System.Reflection.Extensions\\) | grep -v \\(System.Reflection.Primitives\\) | grep -v \\(System.Resources.ResourceManager\\) | grep -v \\(System.Runtime\\) | grep -v \\(System.Runtime.Extensions\\) | grep -v \\(System.Runtime.InteropServices\\) | grep -v \\(System.Runtime.Numerics\\) | grep -v \\(System.Text.Encoding\\) | grep -v \\(System.Text.Encoding.Extensions\\) | grep -v \\(System.Text.RegularExpressions\\) | grep -v \\(System.Threading\\) | grep -v \\(System.Threading.Tasks\\) | grep -v \\(System.Threading.Tasks.Parallel\\) | grep -v \\(System.ValueTuple\\) | grep -v \\(System.Collections.Concurrent\\)'
%else
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/mono-find-requires ; } | sort | uniq | grep -v 2\\.0\\.5 | grep -v \\(System.Collections\\) | grep -v \\(System.Collections.Immutable\\) | grep -v \\(System.Diagnostics.Debug\\) | grep -v \\(System.Dynamic.Runtime\\) | grep -v \\(System.Globalization\\) | grep -v \\(System.IO\\) | grep -v \\(System.Linq\\) | grep -v \\(System.Linq.Expressions\\) | grep -v \\(System.Linq.Queryable\\) | grep -v \\(System.Net.Requests\\) | grep -v \\(System.Reflection\\) | grep -v \\(System.Reflection.Extensions\\) | grep -v \\(System.Reflection.Primitives\\) | grep -v \\(System.Resources.ResourceManager\\) | grep -v \\(System.Runtime\\) | grep -v \\(System.Runtime.Extensions\\) | grep -v \\(System.Runtime.InteropServices\\) | grep -v \\(System.Runtime.Numerics\\) | grep -v \\(System.Text.Encoding\\) | grep -v \\(System.Text.Encoding.Extensions\\) | grep -v \\(System.Text.RegularExpressions\\) | grep -v \\(System.Threading\\) | grep -v \\(System.Threading.Tasks\\) | grep -v \\(System.Threading.Tasks.Parallel\\) | grep -v \\(System.ValueTuple\\) | grep -v \\(System.Collections.Concurrent\\)'
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
%patch1 -p1

%build
version= ./build.sh -c Release && version= ./.dotnet/dotnet restore setup/Swix/Microsoft.FSharp.SDK/Microsoft.FSharp.SDK.csproj --packages fsharp-nugets

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/bin/
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.3.0.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.3.1.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.0.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.1.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.3.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.5.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.3.1.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.7.4.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.3.1
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.4.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.259.4.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.7.41.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.41.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.259.41.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/2.3.5.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/2.3.5.1
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/3.47.4.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/3.47.41.0
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v11.0/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v12.0/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v14.0/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v15.0/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v16.0/FSharp
%{__mkdir_p} "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft F#/v4.0"
%{__mkdir_p} "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/3.0/Framework/v4.0"
%{__mkdir_p} "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/3.1/Framework/v4.0"
%{__mkdir_p} "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/4.0/Framework/v4.0"
%{__mkdir_p} "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/4.1/Framework/v4.0"
sed -e 's#%EXENAME%#fsc.exe#' %{SOURCE1} > ${RPM_BUILD_ROOT}%{_prefix}/bin/fsharpc
sed -e 's#%EXENAME%#fsi.exe#' %{SOURCE1} > ${RPM_BUILD_ROOT}%{_prefix}/bin/fsharpi
sed -e 's#%EXENAME%#fsiAnyCpu.exe#' %{SOURCE1} > ${RPM_BUILD_ROOT}%{_prefix}/bin/fsharpiAnyCpu
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.sigdata ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Core.optdata ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
ln -sf %{_prefix}/lib/mono/fsharp/FSharp.Compiler.Interactive.Settings.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/4.5/
%{__cp} artifacts/bin/fsc/Release/net472/fsc.exe ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/fsc.exe.config ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Build.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Build.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Compiler.Private.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Compiler.Private.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Core.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/FSharp.Core.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.Portable.FSharp.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.Build.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.Build.Framework.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.Build.Tasks.Core.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.Build.Utilities.Core.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Buffers.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Collections.Immutable.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Memory.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Numerics.Vectors.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Reflection.Metadata.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Reflection.TypeExtensions.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Resources.Extensions.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Runtime.CompilerServices.Unsafe.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsc/Release/net472/System.Threading.Tasks.Dataflow.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/fsi.exe ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/fsi.exe.config ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsiAnyCpu/Release/net472/fsiAnyCpu.exe ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsiAnyCpu/Release/net472/fsiAnyCpu.exe.config ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.Compiler.Interactive.Settings.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.Compiler.Interactive.Settings.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.Compiler.Server.Shared.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.Compiler.Server.Shared.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.DependencyManager.Nuget.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/FSharp.DependencyManager.Nuget.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/Microsoft.DotNet.DependencyManager.dll ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} artifacts/bin/fsi/Release/net472/Microsoft.DotNet.DependencyManager.xml ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETFramework/v4.0/4.3.0.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.3.0.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETFramework/v4.0/4.3.1.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.3.1.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETFramework/v4.0/4.4.0.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.0.0/
%{__cp} fsharp-nugets/microsoft.portable.fsharp.core/10.1.0/lib/versions/4.4.1.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.1.0/
%{__cp} fsharp-nugets/fsharp.core/4.3.4/lib/net45/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.3.0/
%{__cp} fsharp-nugets/fsharp.core/4.3.4/lib/net45/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETFramework/v4.0/4.4.5.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETCore/3.3.1.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.3.1.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETCore/3.7.4.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.7.4.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETCore/3.78.3.1/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.3.1/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETCore/3.78.4.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.4.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETCore/3.259.4.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.259.4.0/
%{__cp} fsharp-nugets/microsoft.portable.fsharp.core/10.1.0/lib/profiles/portable-net45+netcore45/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.7.41.0/
%{__cp} fsharp-nugets/microsoft.portable.fsharp.core/10.1.0/lib/profiles/portable-net45+netcore45+wp8/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.78.41.0/
%{__cp} fsharp-nugets/microsoft.portable.fsharp.core/10.1.0/lib/profiles/portable-net45+netcore45+wpa81+wp8/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETCore/3.259.41.0/
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETPortable/2.3.5.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/2.3.5.0
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETPortable/2.3.5.1/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/2.3.5.1
%{__cp} fsharp-nugets/microsoft.visualfsharp.core.redist/1.0.0/content/.NETPortable/3.47.4.0/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/3.47.4.0
%{__cp} fsharp-nugets/microsoft.portable.fsharp.core/10.1.0/lib/profiles/portable-net45+sl5+netcore45/FSharp.Core.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/fsharp/api/.NETPortable/3.47.41.0
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v/FSharp
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v11.0/FSharp
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v12.0/FSharp
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v14.0/FSharp
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v15.0/FSharp
%{__cp} artifacts/bin/fsc/Release/net472/Microsoft.FSharp.*NetSdk.* ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v16.0/FSharp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_prefix}/tmp/
%{__cp} %{SOURCE2} ${RPM_BUILD_ROOT}%{_prefix}/tmp/`basename %{SOURCE2}`.Targets
%{__cp} %{SOURCE3} ${RPM_BUILD_ROOT}%{_prefix}/tmp/`basename %{SOURCE3}`.Targets
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft F#/v4.0"
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/3.0/Framework/v4.0"
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/3.1/Framework/v4.0"
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/4.0/Framework/v4.0"
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets "${RPM_BUILD_ROOT}%{_prefix}/lib/mono/Microsoft SDKs/F#/4.1/Framework/v4.0"
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v/FSharp
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v11.0/FSharp
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v12.0/FSharp
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v14.0/FSharp
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v15.0/FSharp
%{__cp} ${RPM_BUILD_ROOT}%{_prefix}/tmp/*.Targets ${RPM_BUILD_ROOT}%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/v16.0/FSharp

%files
%defattr(-,root,root)
%{_bindir}/fsharp*
%{_prefix}/lib/mono/4.5/*
%{_prefix}/lib/mono/fsharp/
%{_prefix}/lib/mono/Microsoft*
%{_prefix}/lib/mono/xbuild/Microsoft/VisualStudio/
