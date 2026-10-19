# Notice on the bundled workbook

This repository bundles an Excel file under `tests/fixtures/`:

- `tests/fixtures/workbook.xlsm` — the IMF–World Bank LIC-DSF IDA21 template
  (2025-08-12 vintage), retained as `.xlsm` so the differential harness can
  round-trip VBA.

That file is the **Low-Income Country Debt Sustainability Framework (LIC-DSF)
template**, a joint work of the **International Monetary Fund** and the **World
Bank**. It is published by those institutions and distributed to country
authorities. It is included here **unmodified**, so Python parity work can be
reproduced against the exact bytes.

The workbook is the same source workbook the extraction pipeline fetches. Its
upstream name is `LIC-DSF-IDA21-Template-08-12-2025-vf.xlsm`; provenance,
source URL, and checksum are recorded in the extraction repository's
`data/README.md`.

Copyright in the workbook rests with the IMF and the World Bank. Including it
here is not a claim of ownership and does not transfer any rights in it. If you
intend to reuse the template itself, obtain it from, and follow the terms of,
the official sources listed in the extraction repository's `data/README.md`.

The **MIT license** in `LICENSE` covers only the Python source code in this
repository, not the workbook.
