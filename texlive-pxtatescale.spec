Name:		texlive-pxtatescale
Version:	63967
Release:	2
Summary:	Patch to graphics driver for scaling in vertical direction of pTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pxtatescale
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtatescale.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxtatescale.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Patch for graphics driver 'dvipdfmx' to support correct scaling
in vertical direction of Japanese pTeX/upTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pxtatescale
%doc %{_texmfdistdir}/doc/latex/pxtatescale

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
