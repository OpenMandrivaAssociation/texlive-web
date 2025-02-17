Name:		texlive-web
Version:	70015
Release:	1
Summary:	original web programs tangle and weave
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/web
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/web.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/web.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/man/man1/tangle.man1.pdf
%doc %{_mandir}/man1/weave.1*
%doc %{_texmfdistdir}/doc/man/man1/weave.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
