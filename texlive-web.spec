# revision 23089
# category TLCore
# catalog-ctan /systems/knuth/dist/web
# catalog-date 2011-03-22 20:51:59 +0100
# catalog-license knuth
# catalog-version 4.5
Name:		texlive-web
Version:	4.5
Release:	1
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
This is the system that Knuth developed to support the
development of TeX. Included are weave, which converts a web
source to something that may be typeset (with appropriate macro
support) by Plain TeX, and tangle, which converts a web source
to compilable Pascal.

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
