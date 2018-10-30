Name:		texlive-IEEEtran
Version:	1.8b
Release:	2
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
%{_texmfdistdir}/bibtex/bib/IEEEtran
%{_texmfdistdir}/bibtex/bst/IEEEtran
%{_texmfdistdir}/tex/latex/IEEEtran
%doc %{_texmfdistdir}/doc/latex/IEEEtran

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
