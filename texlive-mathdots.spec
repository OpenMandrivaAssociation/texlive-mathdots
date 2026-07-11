%global tl_name mathdots
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Commands to produce dots in math that respect font size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/mathdots
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathdots.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Redefines \ddots and \vdots, and defines \iddots. The dots produced by
\iddots slant in the opposite direction to \ddots. All the commands are
designed to change size appropriately in scripts, as well as in response
to LaTeX size changing commands. The commands may also be used in plain
TeX.

