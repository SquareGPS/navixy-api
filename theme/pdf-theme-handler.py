def get_stylesheet() -> str:
    return """
    .navixy-hide-in-pdf {
        visibility: hidden;
    }
    @page {
        size: a4 portrait;
        margin: 25mm 10mm 25mm 10mm;
        counter-increment: page;
        font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
        white-space: pre;
        color: grey;
        @top-left {
            content: "Copyright © 2020 Navixy";
        }
        @top-center {
            content: string(chapter);
        }
    }
    """


# download link manually added to header
def modify_html(html: str, href: str) -> str:
    return html
