---
name: audiences-known-layer-pattern-aug25
description: "Aug 25 2026: the 0-credit way to pull every Salesforce-known contact at an account from Clay Audiences is to match people on the SF Account ID field audf_0timw68Jf4dTsQQqq38, never email domain (domain matching missed 88/88 Cleveland Clinic contacts); Inger's 12 pulled to motions/back_office_expansion/inger_known_layer_*.csv"
metadata:
  type: reference
---

Pattern (all free reads, no workflow exists for it): `clay audiences records search-ids --entity-type companies --filter <org_name Contain>` then `records get` and read the SF Account ID out of `fields.external_source_sync_status_v3`; then `search-ids --entity-type people` filtered on `audf_0timw68Jf4dTsQQqq38 Equal <SF Account ID>` (paginate on cursor, `records get` in batches of 100). Write raw JSON per batch to files before parsing; piping clay into python inside a bash while-read loop hangs.

Inger's 12 result (Aug 25): 3,909 known people; Cleveland Clinic 88, Cox 621, DIRECTV 257, Guardian 137, Goldman 236, MetLife 615, Prudential 531, Rogers 541, Travelers 345, McKesson 417, Zurich NA 61, Assurant ~60 across three divisional accounts. Owner ID 005V500000GElNdIAL inferred (not verified) to be Inger. Data flags: McKesson and Zurich NA carry Account Type = Prospect in SF; Assurant has no single Customer-tagged account; Cox Automotive, Cox Enterprises, Vibrant Emotional Health sit under the same owner but were not on her 12.

**How to apply:** reuse for every AM's known layer; the known layer is gate 1 (known_to_intradiem) for the Back Office Account Maps. Related: [[inger-12-accounts-aug24]], [[clay-audiences-live-cli-capability-aug20]].
