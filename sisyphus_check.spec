# $Id$

Name: sisyphus
Version: 0.5.2
Release: alt1

Summary: Helpers for Sisyphus
License: GPL
Group: Development/Other
BuildArch: noarch

# get the source from our cvs repository
Source: %name-%version.tar.bz2

%description
This package contains utilities to ease Sisyphus maintainance.

%prep
%setup -q

%install
%__mkdir_p $RPM_BUILD_ROOT%_sysconfdir/%name
%__install -p -m644 etc/* $RPM_BUILD_ROOT%_sysconfdir/%name/

%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__install -p -m755 bin/* $RPM_BUILD_ROOT%_bindir/

%__ln_s sisyphus_cleanup_incoming $RPM_BUILD_ROOT%_bindir/incoming_cleanup

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%config %_sysconfdir/%name/fhs
%config %_sysconfdir/%name/functions
%_bindir/*

%changelog
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
