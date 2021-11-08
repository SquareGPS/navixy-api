def get_stylesheet() -> str:
    return """
    h1, h2, h3 {
         string-set: chapter content();
    }
    
    .md-container {
        display: block;
        padding-top: 0;
    }
    
    .md-main {
        display: block;
        height: inherit;
    }
    
    .md-main__inner {
        height: inherit;
        padding-top: 0;
    }
    
    .md-typeset .codehilitetable .linenos {
        display: none;
    }
    
    .md-typeset .footnote-ref {
        display: inline-block;
    }
    
    .md-typeset a.footnote-backref {
        transform: translateX(0);
        opacity: 1;
    }
    .md-typeset .admonition {
        display: block;
        border-top: .1rem solid rgba(0,0,0,.07);
        border-right: .1rem solid rgba(0,0,0,.07);
        border-bottom: .1rem solid rgba(0,0,0,.07);
        page-break-inside: avoid;
    }
    
    .md-typeset a::after {
        color: inherit;
        content: none;
    }
    
    .md-typeset table:not([class]) th {
        min-width: 0;
    }
    
    .md-typeset table {
        border: .1rem solid rgba(0,0,0,.07);
    }
    """

# download link manually added to header
def modify_html(html: str, href: str) -> str:
    return html
