# revision 15878
# category Package
# catalog-ctan /macros/generic/mathdots
# catalog-date 2007-06-01 10:48:38 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-mathdots
Version:	0.8
Release:	8
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

%description
Redefines \ddots and \vdots, and defines \iddots. The dots
produced by \iddots slant in the opposite direction to \ddots.
All the commands are designed to change size appropriately in
scripts, as well as in response to LaTeX size changing
commands. The commands may also be used in plain TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8-2
+ Revision: 753775
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.8-1
+ Revision: 718970
- texlive-mathdots
- texlive-mathdots
- texlive-mathdots
- texlive-mathdots

