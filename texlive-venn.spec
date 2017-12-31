# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/venn/venn.mp
# catalog-date 2007-12-04 22:25:23 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-venn
Version:	20170414
Release:	1
Summary:	Creating Venn diagrams with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/venn/venn.mp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/venn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MetaPost macros for venn diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/venn/venn.mp
%doc %{_texmfdistdir}/doc/metapost/venn/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071204-2
+ Revision: 757411
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071204-1
+ Revision: 719878
- texlive-venn
- texlive-venn
- texlive-venn

