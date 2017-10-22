# Conditional build:
%bcond_without	tests		# build without tests

# disable file duplicate packaging error
%define		_duplicate_files_terminate_build   0
%define		bld_ver	11
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 53.0
Summary:	Oracle JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Oracle JDK - środowisko programistyczne Javy dla Linuksa
Name:		oracle-java9
Version:	9.0.1
Release:	1
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Development/Languages/Java
# Download URL (requires JavaScript and interactive license agreement):
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
# Use get-source.sh script to download locally.
Source0:	http://download.oracle.com/otn-pub/java/jdk/%{version}+%{bld_ver}/jdk-%{version}_linux-x64_bin.tar.gz
NoSource:	0
Source1:	Test.java
Source2:	jmc.desktop
Patch0:		jmc-path.patch
URL:		http://www.oracle.com/technetwork/java/javase/overview/index.html
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	rpmbuild(macros) >= 1.453
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javareldir	java9-%{version}
%define		javadir		%{_jvmdir}/%{javareldir}
%define		jvmjardir	%{_jvmjardir}/java9-%{version}

# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libjava_crw_demo_g\.so.*' 'libmawt.so' 'java(ClassDataVersion)'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

# binary packages already stripped
%define		_enable_debug_packages 0

# disable stripping which breaks ie jmap -heap <pid>
# Caused by: java.lang.RuntimeException: unknown CollectedHeap type : class sun.jvm.hotspot.gc_interface.CollectedHeap
%define		no_install_post_strip	1

%description
This package symlinks Oracle Java development tools provided by
java9-jdk-base to system-wide directories like /usr/bin, making Oracle
Java the default JDK.

%description -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi programistycznych
uruchomieniowego Javy firmy Oracle, dostarczanych przez pakiet
java9-jdk-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Oracle Java staje się domyślnym JDK
w systemie.

%package appletviewer
Summary:	Java applet viewer from Oracle Java
Summary(pl.UTF-8):	Przeglądarka appletów Javy Oracle
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}

%description appletviewer
This package contains applet viewer for Oracle Java.

%description appletviewer -l pl.UTF-8
Ten pakiet zawiera przeglądarkę appletów dla Javy Oracle.

%package jdk-base
Summary:	Oracle JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Oracle JDK - środowisko programistyczne Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-8
Provides:	jdk(%{name})

%description jdk-base
Java Development Kit for Linux.

%description jdk-base -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package jre
Summary:	Oracle JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-8
Suggests:	%{name}-jre-X11
Provides:	java
Provides:	java1.4
Provides:	jre = %{version}
Obsoletes:	java-blackdown-jre
Obsoletes:	jre

%description jre
This package symlinks Oracle Java runtime environment tools provided
by java9-jre-base to system-wide directories like /usr/bin, making
Oracle Java the default JRE.

%description jre -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi środowiska
uruchomieniowego Javy firmy Oracle, dostarczanych przez pakiet
java9-jre-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Oracle Java staje się domyślnym JRE
w systemie.

%package jre-base
Summary:	Oracle JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.7.5-8
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(jaas) = %{version}
Provides:	java(jaf) = 1.1.1
Provides:	java(jaxp) = 1.3
Provides:	java(jaxp_parser_impl)
Provides:	java(jce) = %{version}
Provides:	java(jdbc-stdext) = %{version}
Provides:	java(jdbc-stdext) = 3.0
Provides:	java(jmx) = 1.4
Provides:	java(jndi) = %{version}
Provides:	java(jsse) = %{version}
Provides:	jre(%{name})

%description jre-base
Java Runtime Environment for Linux. Does not contain any X11-related
compontents.

%description jre-base -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa. Nie zawiera żadnych
elementów związanych ze środowiskiem X11.

%package jre-X11
Summary:	Oracle JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Provides:	javaws = %{version}
Provides:	jre-X11 = %{version}
Obsoletes:	jre-X11

%description jre-X11
This package symlinks Oracle Java X11 libraries provided by
java9-jre-base-X11 to system-wide directories like /usr/bin, making
Oracle Java the default JRE-X11.

%description jre-X11 -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi X11 Javy firmy
Oracle, dostarczanych przez pakiet java9-jre-base-X11, w standardowych
systemowych ścieżkach takich jak /usr/bin, sprawiając tym samym, że
Oracle Java staje się domyślnym JRE-X11 w systemie.

%package jre-base-X11
Summary:	Oracle JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Oracle JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-X11
X11-related part of Java Runtime Environment for Linux.

%description jre-base-X11 -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa, część związana ze
środowiskiem graficznym X11.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package javafx
Summary:	Oracle JRE (Java Runtime Environment) for Linux - JavaFX runtime binaries
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description javafx
JavaFX is the next step in the evolution of Java as a rich client
platform. It is designed to provide a lightweight,
hardware-accelerated Java UI platform for enterprise business
applications. With JavaFX, developers can preserve existing
investments by reusing Java libraries in their applications. They can
even access native system capabilities, or seamlessly connect to
server-based middleware applications.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	jar
Provides:	java-jre-tools
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-jre-tools

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	jre

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package -n browser-plugin-%{name}
Summary:	Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java-mozilla-plugin
Provides:	mozilla-firefox-plugin-java
Provides:	mozilla-plugin-java
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java-sun-ng
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java-moz-plugin
Obsoletes:	java-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java
Obsoletes:	mozilla-firefox-plugin-gcc3-java
Obsoletes:	mozilla-firefox-plugin-java
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java
Obsoletes:	mozilla-plugin-gcc3-java
Obsoletes:	mozilla-plugin-gcc32-java
Obsoletes:	mozilla-plugin-java
Obsoletes:	mozilla-plugin-java-blackdown

%description -n browser-plugin-%{name}
Java plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla przeglądarek WWW.

%package -n browser-plugin-%{name}-ng
Summary:	Next-Generation Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy Nowej Generacji do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java-mozilla-plugin
Provides:	mozilla-firefox-plugin-java
Provides:	mozilla-plugin-java
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java-moz-plugin
Obsoletes:	java-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java
Obsoletes:	mozilla-firefox-plugin-gcc3-java
Obsoletes:	mozilla-firefox-plugin-java
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java
Obsoletes:	mozilla-plugin-gcc3-java
Obsoletes:	mozilla-plugin-gcc32-java
Obsoletes:	mozilla-plugin-java
Obsoletes:	mozilla-plugin-java-blackdown

%description -n browser-plugin-%{name}-ng
Next-Generation Java plugin for WWW browsers. Works only with
Firefox/Iceweasel 3.x.

%description -n browser-plugin-%{name}-ng -l pl.UTF-8
Wtyczka Nowej Generacji z obsługą Javy dla przeglądarek WWW. Działa
tylko z Firefoksem/Iceweaselem 3.x.

%package sources
Summary:	JRE standard library sources
Summary(pl.UTF-8):	Źródła standardowej biblioteki JRE
Group:		Development/Languages/Java

%description sources
Sources for the standard Java library.

%description sources -l pl.UTF-8
Źródła standardowej bilioteki Java.

%package missioncontrol
Summary:	Java Mission Control tool
Summary(pl.UTF-8):	Narzędzie Java Mission Control
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	xulrunner-libs

%description missioncontrol
This package contains Java Mission Control tool.

%description missioncontrol -l pl.UTF-8
Ten pakiet zawiera narzędzie Java Mission Control.

%prep
%setup -q -n jdk-%{version}
%patch0 -p1

cp -p %{SOURCE1} Test.java

%build
%if %{with tests}
# Make sure we have /proc mounted,
# javac Test.java fails to get lock otherwise and runs forever:
# Java HotSpot(TM) Client VM warning: Can't detect initial thread stack location - find_vma failed
if [ ! -f /proc/cpuinfo ]; then
	echo >&2 "WARNING: /proc not mounted -- compile test may fail"
fi

# CLASSPATH prevents finding Test.class in .
unset CLASSPATH || :
# $ORIGIN does not work on PLD builders. workaround with LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$(pwd)/lib/jli
./bin/javac Test.java
./bin/java Test

classver=$(cat classver)
if [ "$classver" != %{_classdataversion} ]; then
	echo "Set %%define _classdataversion to $classver and rerun."
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{javadir},%{jvmjardir},%{_javadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_browserpluginsdir}}

cp -a bin conf include lib $RPM_BUILD_ROOT%{javadir}

for i in java jjs keytool orbd policytool javaws \
	rmid rmiregistry servertool tnameserv pack200 unpack200; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in appletviewer idlj jaotc jar jarsigner \
	javac javadoc javah javap javapackager jcmd jconsole jdb jdeprscan jdeps jhsdb jimage jinfo jlink \
        jmap jmc jmod jps jrunscript jshell jstack jstat jstatd jweblauncher rmic serialver \
	schemagen wsgen wsimport xjc; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

%ifarch %{ix86}
for i in jcontrol; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif
%ifarch %{x8664}
for i in jcontrol; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif

# Install plugin for browsers
# Plugin in regular location simply does not work (is seen by browsers):
ln -sf %{javadir}/lib//libnpjp2.so $RPM_BUILD_ROOT%{_browserpluginsdir}

cp -a lib/desktop/applications/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p lib/missioncontrol/icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/jmc.xpm
ln -sf %{_pixmapsdir}/jmc.xpm $RPM_BUILD_ROOT%{javadir}/lib/missioncontrol/icon.xpm

ln -sf %{javadir}/lib/javaws.jar $RPM_BUILD_ROOT%{jvmjardir}/javaws.jar

# leave all locale files unchanged in the original location (license
# restrictions) and only link them at the proper locations
for loc in $(ls $RPM_BUILD_ROOT%{javadir}/lib/locale); do
	install -d $RPM_BUILD_ROOT%{_localedir}/$loc/LC_MESSAGES
	ln -sf %{javadir}/lib/locale/$loc/LC_MESSAGES/sunw_java_plugin.mo \
		$RPM_BUILD_ROOT%{_localedir}/$loc/LC_MESSAGES
done

# standardize dir names
mv -f $RPM_BUILD_ROOT%{_localedir}/{zh,zh_CN}
mv -f $RPM_BUILD_ROOT%{_localedir}/{zh_HK.BIG5HK,zh_HK}
rm -rf $RPM_BUILD_ROOT%{_localedir}/{ko.UTF-8,zh.GBK,zh_TW.BIG5}

mv -f $RPM_BUILD_ROOT%{javadir}/lib/src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources

ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java
ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java9
ln -s java9-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/java
ln -s java9-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jre

# ugly hack for libavplugin.so
cp -p $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-56.so \
	$RPM_BUILD_ROOT%{javadir}/lib/libavplugin-57.so
%{__sed} -i -e '
	s#\.so\.56#.so.57#g
	s#LIBAVFORMAT_56#LIBAVFORMAT_57#g
	s#LIBAVCODEC_56#LIBAVCODEC_57#g
' $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-57.so
rm $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-53.so
rm $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-54.so
rm $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-55.so
rm $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-56.so
rm $RPM_BUILD_ROOT%{javadir}/lib/libavplugin-ffmpeg-56.so

# modify RPATH so that javac and friends are able to work when /proc is not
# mounted and we can't append to RPATH (for example to keep previous lookup
# path) as RPATH can't be longer than original
#
# for example:
# old javac: RPATH=$ORIGIN/../lib/i386/jli:$ORIGIN/../jre/lib/i386/jli
# new javac: RPATH=%{_prefix}/lib/jvm/java9-1.6.0/jre/lib/i386/jli

# silly rpath: jre/bin/unpack200: RPATH=$ORIGIN
chrpath -d $RPM_BUILD_ROOT%{javadir}/bin/unpack200

fixrpath() {
	execlist=$(find $RPM_BUILD_ROOT%{javadir} -type f -executable | xargs file | awk -F: '/ELF.*executable/{print $1}')
	for f in $execlist; do
		rpath=$(chrpath -l $f | awk '/(R|RUN)PATH=/ { gsub(/.*RPATH=/,""); gsub(/.*RUNPATH=/,""); gsub(/:/," "); print $0 }')
		[ "$rpath" ] || continue

		# file
		file=${f#$RPM_BUILD_ROOT}
		origin=${file%/*}

		new=
		for a in $rpath; do
			t=$(echo $a | sed -e "s,\$ORIGIN,$origin,g")
			# get rid of ../../
			t=$(set -e; t=$RPM_BUILD_ROOT$t; [ -d $t ] || exit 0; cd $t; pwd)
			# skip inexistent paths
			[ "$t" ] || continue

			t=${t#$RPM_BUILD_ROOT}

			if [[ "$new" != *$t* ]]; then
				# append it now
				new=${new}${new:+:}$t
			fi
		done
		# leave old one if new is too long
		if [ ${#new} -gt ${#rpath} ]; then
			echo "WARNING: New ($new) rpath is too long. Leaving old ($rpath) one." >&2
		else
			chrpath -r ${new} $f
		fi
	done
}

fixrpath

# Java Mission Control segfaults with recent versions of webkit (see
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=404776 for details.
# Workaround with xulrunner provided until working version is
# delivered.
cat <<EOF >> $RPM_BUILD_ROOT%{javadir}/bin/jmc.ini
-Dorg.eclipse.swt.browser.DefaultType=mozilla
-Dorg.eclipse.swt.browser.XULRunnerPath=%{_libdir}/xulrunner/
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post -n browser-plugin-%{name}-ng
%update_browser_plugins

%postun -n browser-plugin-%{name}-ng
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc README.html legal
%{_jvmdir}/java
%{_jvmjardir}/java
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jaotc
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/javapackager
%attr(755,root,root) %{_bindir}/jcmd
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jdeprscan
%attr(755,root,root) %{_bindir}/jdeps
%attr(755,root,root) %{_bindir}/jhsdb
%attr(755,root,root) %{_bindir}/jimage
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jjs
%attr(755,root,root) %{_bindir}/jlink
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jmod
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jshell
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/jweblauncher
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/schemagen
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/unpack200
%attr(755,root,root) %{_bindir}/wsgen
%attr(755,root,root) %{_bindir}/wsimport
%attr(755,root,root) %{_bindir}/xjc

%files jdk-base
%defattr(644,root,root,755)
%{_jvmdir}/java9
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jaotc
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/javapackager
%attr(755,root,root) %{javadir}/bin/jcmd
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jdeprscan
%attr(755,root,root) %{javadir}/bin/jdeps
%attr(755,root,root) %{javadir}/bin/jhsdb
%attr(755,root,root) %{javadir}/bin/jimage
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jjs
%attr(755,root,root) %{javadir}/bin/jlink
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jmod
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jrunscript
%attr(755,root,root) %{javadir}/bin/jshell
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/jweblauncher
%attr(755,root,root) %{javadir}/bin/orbd
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/rmic
%attr(755,root,root) %{javadir}/bin/schemagen
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/servertool
%attr(755,root,root) %{javadir}/bin/tnameserv
%attr(755,root,root) %{javadir}/bin/unpack200
%attr(755,root,root) %{javadir}/bin/wsgen
%attr(755,root,root) %{javadir}/bin/wsimport
%attr(755,root,root) %{javadir}/bin/xjc
%{javadir}/conf/security/javaws.policy
%{javadir}/include
%{javadir}/lib/ct.sym
%{javadir}/lib/*.jar

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{javadir}/bin/appletviewer

%files jre
%defattr(644,root,root,755)
%doc lib/server/Xusage*
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/rmid

%files jre-base
%defattr(644,root,root,755)
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmiregistry
%dir %{javadir}/conf
%{javadir}/conf/*.properties
%{javadir}/conf/management
%dir %{javadir}/conf/security
%{javadir}/conf/security/policy
%{javadir}/conf/security/java.policy
%{javadir}/conf/security/java.security
%dir %{javadir}/lib

%{javadir}/lib/jvm.cfg
%{javadir}/lib/modules
%dir %{javadir}/lib/server
%attr(755,root,root) %{javadir}/lib/server/*
%dir %{javadir}/lib/jli
%attr(755,root,root) %{javadir}/lib/jli/libjli.so

%attr(755,root,root) %{javadir}/lib/lib*.so
%exclude %{javadir}/lib/libjsoundalsa.so
%exclude %{javadir}/lib/libnpjp2.so
%exclude %{javadir}/lib/libsplashscreen.so
%exclude %{javadir}/lib/libglass.so
%exclude %{javadir}/lib/libgstreamer-lite.so
%exclude %{javadir}/lib/libjavafx_*.so
%exclude %{javadir}/lib/libjawt.so
%exclude %{javadir}/lib/libjfx*.so
%exclude %{javadir}/lib/libprism_*.so
%exclude %{javadir}/lib/libfxplugins.so
%exclude %{javadir}/lib/libavplugin-57.so

%{javadir}/lib/deploy
%{javadir}/lib/desktop
%attr(755,root,root) %{javadir}/lib/jexec
%dir %{javadir}/lib/security
%{javadir}/lib/security/*.*
%{javadir}/lib/security/blacklist
%verify(not md5 mtime size) %config(noreplace) %{javadir}/lib/security/cacerts
%{javadir}/lib/*.properties
%{javadir}/lib/tzdb.dat
%exclude %{javadir}/lib/javafx.properties
%lang(ja) %{javadir}/lib/*.properties.ja
%dir %{jvmjardir}
%{javadir}/lib/classlist
%{javadir}/lib/fontconfig.RedHat*.bfc
%{javadir}/lib/fontconfig.RedHat*.properties.src
%{javadir}/lib/fontconfig.SuSE*.bfc
%{javadir}/lib/fontconfig.SuSE*.properties.src
%{javadir}/lib/fontconfig.bfc
%{javadir}/lib/fontconfig.properties.src

%files jre-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/javaws
%attr(755,root,root) %{_bindir}/jcontrol
%{_desktopdir}/sun_java.desktop
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{javadir}/bin/policytool
%lang(de) %{_localedir}/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{_localedir}/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{_localedir}/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{_localedir}/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{_localedir}/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{_localedir}/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(pt_BR) %{_localedir}/pt_BR/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{_localedir}/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_HK) %{_localedir}/zh_HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_CN) %{_localedir}/zh_CN/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{_localedir}/zh_TW/LC_MESSAGES/sunw_java_plugin.mo

%files jre-base-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/bin/jcontrol
%attr(755,root,root) %{javadir}/bin/javaws
%{javadir}/lib/fonts
%{javadir}/lib/oblique-fonts
%attr(755,root,root) %{javadir}/lib/libsplashscreen.so
%{jvmjardir}/javaws.jar
%attr(755,root,root) %{javadir}/lib/libjawt.so
%dir %{javadir}/lib/locale
%lang(de) %{javadir}/lib/locale/de
%lang(es) %{javadir}/lib/locale/es
%lang(fr) %{javadir}/lib/locale/fr
%lang(it) %{javadir}/lib/locale/it
%lang(ja) %{javadir}/lib/locale/ja
%lang(ko) %{javadir}/lib/locale/ko*
%lang(sv) %{javadir}/lib/locale/sv
%lang(zh_CN) %{javadir}/lib/locale/zh
%lang(zh_CN) %{javadir}/lib/locale/zh.*
%lang(zh_HK) %{javadir}/lib/locale/zh_HK*
%lang(zh_TW) %{javadir}/lib/locale/zh_TW*

%files jre-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/lib/libjsoundalsa.so

%files javafx
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/lib/libavplugin-57.so
%attr(755,root,root) %{javadir}/lib/libfxplugins.so
%attr(755,root,root) %{javadir}/lib/libglass.so
%attr(755,root,root) %{javadir}/lib/libgstreamer-lite.so
%attr(755,root,root) %{javadir}/lib/libjavafx_*.so
%attr(755,root,root) %{javadir}/lib/libjfx*.so
%attr(755,root,root) %{javadir}/lib/libprism_*.so
%{javadir}/lib/javafx.properties

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry

%files -n browser-plugin-%{name}-ng
%defattr(644,root,root,755)
%attr(755,root,root) %{javadir}/lib/libnpjp2.so
%attr(755,root,root) %{_browserpluginsdir}/libnpjp2.so

%files sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-sources
%{_prefix}/src/%{name}-sources/src.zip

%files missioncontrol
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jmc
%attr(755,root,root) %{javadir}/bin/jmc
%{javadir}/bin/jmc.ini
%dir %{javadir}/lib/jfr
%{javadir}/lib/jfr/default.jfc
%{javadir}/lib/jfr/profile.jfc
%dir %{javadir}/lib/missioncontrol
%{javadir}/lib/missioncontrol/.eclipseproduct
%{javadir}/lib/missioncontrol/artifacts.xml
%{javadir}/lib/missioncontrol/configuration
%{javadir}/lib/missioncontrol/dropins
%{javadir}/lib/missioncontrol/features
%{javadir}/lib/missioncontrol/icon.xpm
%attr(755,root,root) %{javadir}/lib/missioncontrol/jmc
%{javadir}/lib/missioncontrol/jmc.ini
%{javadir}/lib/missioncontrol/p2
%dir %{javadir}/lib/missioncontrol/plugins
%{javadir}/lib/missioncontrol/plugins/*.jar
%{javadir}/lib/missioncontrol/plugins/com.oracle.jmc.console.ui.notification_*
%{javadir}/lib/missioncontrol/plugins/com.oracle.jmc.rjmx_*
%dir %{javadir}/lib/missioncontrol/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_*
%{javadir}/lib/missioncontrol/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_*/META-INF
%{javadir}/lib/missioncontrol/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_*/about.html
%attr(755,root,root) %{javadir}/lib/missioncontrol/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_*/*.so
%{javadir}/lib/missioncontrol/plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_*/launcher.gtk.linux.x86_64.properties
%{javadir}/lib/missioncontrol/plugins/org.eclipse.ui.themes_*
%{javadir}/lib/missioncontrol/THIRDPARTYLICENSEREADME.txt
%{_desktopdir}/jmc.desktop
%{_pixmapsdir}/jmc.xpm
