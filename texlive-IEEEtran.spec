# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/IEEEtran
# catalog-date 2008-09-30 18:04:42 +0200
# catalog-license lppl
# catalog-version 1.7a
Name:		texlive-IEEEtran
Version:	1.7a
Release:	3
Summary:	Document class for IEEE Transactions journals and conferences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEtran
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEtran.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/IEEEtran.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class and its BibTeX style enable authors to produce
officially-correct output for the Institute of Electrical and
Electronics Engineers (IEEE) transactions, journals and
conferences.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/IEEEtran/IEEEabrv.bib
%{_texmfdistdir}/bibtex/bib/IEEEtran/IEEEexample.bib
%{_texmfdistdir}/bibtex/bib/IEEEtran/IEEEfull.bib
%{_texmfdistdir}/bibtex/bst/IEEEtran/IEEEtran.bst
%{_texmfdistdir}/bibtex/bst/IEEEtran/IEEEtranN.bst
%{_texmfdistdir}/bibtex/bst/IEEEtran/IEEEtranS.bst
%{_texmfdistdir}/bibtex/bst/IEEEtran/IEEEtranSA.bst
%{_texmfdistdir}/bibtex/bst/IEEEtran/IEEEtranSN.bst
%{_texmfdistdir}/tex/latex/IEEEtran/IEEEtran.cls
%{_texmfdistdir}/tex/latex/IEEEtran/IEEEtrantools.sty
%doc %{_texmfdistdir}/doc/latex/IEEEtran/IEEEtran_HOWTO.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEtran/IEEEtran_bst_HOWTO.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEtran/IEEEtrantools_doc.txt
%doc %{_texmfdistdir}/doc/latex/IEEEtran/README
%doc %{_texmfdistdir}/doc/latex/IEEEtran/README.bibtex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/README.extras
%doc %{_texmfdistdir}/doc/latex/IEEEtran/README.testflow
%doc %{_texmfdistdir}/doc/latex/IEEEtran/README.tools
%doc %{_texmfdistdir}/doc/latex/IEEEtran/bare_adv.tex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/bare_conf.tex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/bare_jrnl.tex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/bare_jrnl_compsoc.tex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/changelog.txt
%doc %{_texmfdistdir}/doc/latex/IEEEtran/font_install_how.txt
%doc %{_texmfdistdir}/doc/latex/IEEEtran/testflow.tex
%doc %{_texmfdistdir}/doc/latex/IEEEtran/testflow_ctl_A4.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEtran/testflow_ctl_LTR.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEtran/testflow_doc.pdf
%doc %{_texmfdistdir}/doc/latex/IEEEtran/tux.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7a-2
+ Revision: 752689
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7a-1
+ Revision: 718696
- texlive-IEEEtran
- texlive-IEEEtran
- texlive-IEEEtran
- texlive-IEEEtran
- texlive-IEEEtran

