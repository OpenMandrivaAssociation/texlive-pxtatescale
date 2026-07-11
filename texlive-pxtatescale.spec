%global tl_name pxtatescale
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Patch to graphics driver for scaling in vertical direction of pTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxtatescale
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtatescale.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtatescale.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Patch for graphics driver 'dvipdfmx' to support correct scaling in
vertical direction of Japanese pTeX/upTeX.

