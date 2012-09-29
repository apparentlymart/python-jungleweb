
import publicsuffix


_psl = None


class Page(object):
    title = None
    description = None
    url = None
    image_url = None
    ogp_type = None
    fetch_url = None
    site_name = None

    @property
    def url_domain(self):
        url = self.url
        if url is None:
            url = self.fetch_url
        parts = urlparse(url)
        return parts.hostname

    @property
    def url_public_suffix(self):
        global _psl
        if _psl is None:
            _psl = publicsuffix.PublicSuffixList()
        return _psl.get_public_suffix(self.url_domain)
