import os

FULL_MANIFEST = "228361d0-4cda-4805-a2f8-a05ee58119b6"
HISTORISCHE_AUSGABE = "5b8d9c77-99d0-4a80-92d8-4a9de06ac7ca"
FRD_USER = os.environ.get('FRD_USER')
FRD_PW = os.environ.get('FRD_PW')

MANIFEST_DEFAULT_FILTER = {
    "field_doc_component.id": FULL_MANIFEST,
    "field_manifestation_typ.id": HISTORISCHE_AUSGABE,
    "field_status_umschrift": 2
}

MAN_CSV = "./html/data/manifestations.csv"
UMSCHRIFT_DATA = "./html/data/umschrift.json"

DIPL_UMSCHRIFT_MAPPING = {
    0: "Umschrift fehlt",
    2: "Umschrift vorhanden"
}