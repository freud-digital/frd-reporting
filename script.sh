# bin/bash
echo "download signatures"
python dl_work_signatures.py
echo "download manifestation_info"
python dl_stats.py
echo "create some data"
python umschrift_stats.py