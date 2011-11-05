# revision 15878
# category Package
# catalog-ctan /macros/generic/mathdots
# catalog-date 2007-06-01 10:48:38 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-mathdots
Version:	0.8
Release:	1
Summary:	Commands to produce dots in math that respect font size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/mathdots
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Redefines \ddots and \vdots, and defines \iddots. The dots
produced by \iddots slant in the opposite direction to \ddots.
All the commands are designed to change size appropriately in
scripts, as well as in response to LaTeX size changing
commands. The commands may also be used in plain TeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/mathdots/mathdots.sty
%{_texmfdistdir}/tex/generic/mathdots/mathdots.tex
%doc %{_texmfdistdir}/doc/generic/mathdots/README
%doc %{_texmfdistdir}/doc/generic/mathdots/mathdots.pdf
%doc %{_texmfdistdir}/doc/generic/mathdots/mdtest.tex
#- source
%doc %{_texmfdistdir}/source/generic/mathdots/mathdots.dtx
%doc %{_texmfdistdir}/source/generic/mathdots/mathdots.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
