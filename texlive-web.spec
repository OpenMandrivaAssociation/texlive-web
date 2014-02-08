# revision 26689
# category TLCore
# catalog-ctan /systems/knuth/dist/web
# catalog-date 2012-02-22 18:24:24 +0100
# catalog-license knuth
# catalog-version 4.5
Name:		texlive-web
Version:	4.5
Release:	4
Summary:	original web programs tangle and weave
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/web
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/web.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/web.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-web.bin

%description
The system processes 'web' files in two ways: firstly to
rearrange them to produce compilable code (using the program
tangle), and secondly to produce a TeX source (using the
program weave) that may be typeset for comfortable reading.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/tangle.1*
%doc %{_texmfdir}/doc/man/man1/tangle.man1.pdf
%doc %{_mandir}/man1/weave.1*
%doc %{_texmfdir}/doc/man/man1/weave.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.5-3
+ Revision: 813179
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.5-2
+ Revision: 757502
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.5-1
+ Revision: 719906
- texlive-web
- texlive-web
- texlive-web

