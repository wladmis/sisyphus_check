# $Id$

Name: sisyphus_check
Version: 0.7.8
Release: alt1

Summary: package checker for Sisyphus
License: GPL
Group: Development/Other
BuildArch: noarch

Requires: getopt, mktemp >= 1:1.3.1
Conflicts: sisyphus < 0.7.2

# get the source from our cvs repository
Source: %name-%version.tar.bz2

%description
This package contains sisyphus_check utility.

%prep
%setup -q

%install
%__install -pD -m644 fhs $RPM_BUILD_ROOT%_sysconfdir/%name/fhs
%__install -pD -m755 %name $RPM_BUILD_ROOT%_bindir/%name

%files
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/fhs
%_bindir/*

%changelog
* Fri Oct 22 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.8-alt1
- Implemented support for check_gpgname() exceptions (legion).

* Wed Sep 01 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.7-alt1
- check_content, check_fhs: enhanced error diagnostics.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- check_gpgname: made the check case-insensitive.
- check_fhs: added /lib64 and /usr/lib64 to builtin list.

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- New option: --trust-gpg-names.

* Wed Aug 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.4.1-alt1
- check_gpgname: enhanced error diagnostics.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- check_gpgname: new check.

* Wed Jul 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- check_fhs,check_intersects: do not use command substitutions.
- Enhanced error diagnostics a bit.

* Thu Jun 24 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- Moved sisyphus_check to separate subpackage.

* Mon Jun 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- functions: fixed quiet mode.
- sisyphus_check: added new option: verbose.
- sisyphus_add_new: enabled quiet mode by default.

* Sat Jun 05 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- functions: optimized, thanks to legion@.
- functions/check_buildtime: new check.
- functions/check: use it.
- sisyphus_check: added new options:
  quiet, fast-check, show-bad-files.

* Thu May 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.0-alt1
- sisyphus_relink: added support for new style lists.
- functions/{check_summary,check_description}: new checks.
- functions/check: use them.

* Thu Feb 19 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- functions/check_changelog: added check for empty changelog text.

* Mon Feb 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.5-alt1
- functions/check_deps:
  + added initscripts to the list of forbidden dependencies.
- functions/check_nvr:
  + new check (for invalid name-version-release).
- functions/check:
  + use it.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4-alt1
- functions/check_content: new check (forbidden .la files).
- config:
  + define VERSION;
  + added --no-oldhashfile to GENBASEDIR_OPT_ARGS.
- sisyphus_genhash: pass architecture and version to genbasedir.

* Sun Nov 02 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.3-alt1
- sisyphus_check:
  + new option: --no-check=LIST;
  + better error diagnostics.

* Tue Oct 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- sisyphus/fhs: new file.
- functions: use it.
- sisyphus_check,sisyphus_add_new: turn into bash script.
- functions/check_gpg: ignore default keyring.
- functions/check*: better error checking.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- functions/check_changelog: added check for packager format.
- functions,sisyphus_check: added support to skip some checks.
- functions/check*: better error checking.

* Tue Sep 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.10-alt1
- functions/check_deps: added check for invalid dependencies.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.9-alt1
- functions/check_printable: new check.
- functions/check: use it (#932).
- functions/upload_{src,bin}: remove unused functions.
- functions/check*: better error checking.

* Tue Sep 09 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.8-alt1
- functions/check_buildhost: new check.
- functions/check: use it.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.7-alt1
- sisyphus_gen_contents: new script.
- functions/check_fhs: fixed possible false alarms on empty list.
- functions/check_deps: added to forbidden requires:
  fileutils, sh-utils, textutils.

* Thu Jun 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.6-alt1.1
- sync

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.6-alt1
- sisyphus_check: check deps.

* Tue Apr 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt1
- sisyphus_check: check permisions in source archive.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Updated.

* Wed Feb 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.3-alt1
- sync. new checks (FHS)

* Tue Dec 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt1
- sync. new relink algo by ldv. unset LC_*

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt5
- sync

* Fri Sep 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt4
- sync

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt3
- sync with latest changes:
- new utils:
	sisyphus_relink
	sisyphus_add_new

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt2
- rebuild to fix deps

* Mon Aug 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- sync last changes
- added changelog checking

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- sync last changes
- added symlink incoming_cleanup to sisyphus_cleanup_incoming
- added automatic package group check, suid/sgid check
- added sisyphus_check utility
- check() moved to functions
- /etc/sisyphus/functions no config(noreplace) now

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- More code cleanup.

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Specfile and code cleanup.

* Mon Jun 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- added master repository
- added cleanup dups script

* Wed Jun 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt1
- Inital release for Sisyphus
