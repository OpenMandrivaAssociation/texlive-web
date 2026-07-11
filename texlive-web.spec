%global tl_name web
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.5
Release:	%{tl_revision}.1
Summary:	The original literate programming system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/web
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/web.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/web.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(web.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The system processes 'web' files in two ways: firstly to rearrange them
to produce compilable code (using the program tangle), and secondly to
produce a TeX source (using the program weave) that may be typeset for
comfortable reading.

