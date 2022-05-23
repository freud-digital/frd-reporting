import requests
import time
import pandas as pd
from freud_api_crawler import freud_api_crawler as frd
from freud_api_crawler.string_utils import always_https


def yield_manifestation():
    """ yields jsonapi output from manifestations indcluding

        :param url: The API-endpoint
        :param type: string

        :param simple: If True a processed dict is returned, otherwise the full data object
        :param type: bool

        :return: Yields a dict
        """
    next_page = True
    url = f"{frd.FRD_API}node/manifestation?filter[field_doc_component.id]={frd.FULL_MANIFEST}&filter[field_manifestation_typ.id]={frd.HISTORISCHE_AUSGABE}&include=field_werk"  # noqa: E501
    while next_page:
        print(url)
        response = None
        result = None
        x = None
        time.sleep(0.05)
        response = requests.get(
            url,
            cookies=frd.AUTH_ITEMS['cookie'],
            allow_redirects=True,
        )
        result = response.json()
        links = result['links']
        if links.get('next', False):
            orig_url = links['next']['href']
            url = always_https(orig_url)
        else:
            next_page = False
        mans = []
        works = []
        for x in result['data']:
            try:
                if x['attributes']['field_status_umschrift']:
                    umschrift = x['attributes']['field_status_umschrift']
                else:
                    umschrift = 0
                man = {
                    'man_id': x['id'],
                    'man_title': x['attributes']['title'],
                    'man_field_status_umschrift': umschrift,
                    'man_sig': x['attributes']['field_signatur_sfe_type'],
                    'man_created': x['attributes']['created'],
                    'man_changed': x['attributes']['changed'],
                    'work_id': x['relationships']['field_werk']['data']['id']
                }
                mans.append(man)
            except:  # noqa: E722
                continue
        for x in result['included']:
            try:
                work = {
                    'work_id': x['id'],
                    'work_title': x['attributes']['title'],
                    'work_created': x['attributes']['created'],
                    'work_changed': x['attributes']['changed'],
                    'werk_signatur_id': x['relationships']['field_signatur_sfe']['data']['id']
                }
                works.append(work)
            except:  # noqa: E722
                continue
        man_df = pd.DataFrame(mans)
        work_df = pd.DataFrame(works)
        merged = pd.merge(man_df, work_df, on='work_id')
        for record in merged.to_dict(orient='records'):
            yield(record)


def yield_werk_signaturs():
    """ yields jsonapi output from manifestations indcluding

        :param url: The API-endpoint
        :param type: string

        :param simple: If True a processed dict is returned, otherwise the full data object
        :param type: bool

        :return: Yields a dict
        """
    next_page = True
    url = f"{frd.FRD_API}taxonomy_term/signatur_fe?fields[taxonomy_term--signatur_fe]=name"
    while next_page:
        print(url)
        response = None
        result = None
        x = None
        time.sleep(0.3)
        response = requests.get(
            url,
            cookies=frd.AUTH_ITEMS['cookie'],
            allow_redirects=True,
        )
        result = response.json()
        links = result['links']
        if links.get('next', False):
            orig_url = links['next']['href']
            url = always_https(orig_url)
        else:
            next_page = False
        for x in result['data']:
            item = {
                'werk_signatur_id': x['id'],
                'werk_signatur': x['attributes']['name']
            }
            yield(item)
