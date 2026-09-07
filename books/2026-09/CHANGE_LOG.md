# Cover and index reconciliation

Editorial revision: 7 September 2026. Original evidence dates and statuses preserved.

## Page changes

| Book | Changed PDF pages | Operation |
| --- | --- | --- |
| Selected Exhibits — Foundations | 1 | Cover replaced; title metadata reconciled |
| Selected Exhibits — Systems and Applications | 1–18 | Cover replaced; editorial navigation corrected; title metadata reconciled |
| Public Record — Chronology | 1–18 | Cover replaced; editorial navigation corrected; title metadata reconciled |
| The Evidence Arc | 1–23 | Cover replaced; editorial navigation corrected; title metadata reconciled |
| The Control Plane | 1–23 | Cover replaced; editorial navigation corrected; title metadata reconciled |
| Before Reality Resolved — DI Weather Station | None | Original cover preserved; title metadata reconciled |
| MathWise / Erdős — Mathematical Record | 1–23 | Cover replaced; editorial navigation corrected; title metadata reconciled |
| Law Firm Decision and Evidence | 1 | Cover replaced; title metadata reconciled |
| BriefWise — Harvey Benchmark Audit | None | Original cover preserved; title metadata reconciled; first bookmark title updated |

## Verification

- All nine input PDF SHA-256 values match the supplied Record_Index.csv.
- Nine book counts preserved: 18, 18, 18, 23, 23, 55, 23, 59, and 23 pages (260 total).
- Seven covers replaced in place; Weather RC1 and Harvey covers preserved.
- 100 interior pages contain narrow editorial label/navigation edits. No exhibit images were edited.
- All 153 untouched pages: exact extracted-text and rendered-pixel comparisons PASS using PyMuPDF at 72 DPI.
- All 100 changed interior pages: rendered pixels outside the edited text bands match the originals. Edited bands were visually inspected at 108 DPI; covers and all five catalog pages were visually inspected.
- Page dimensions, rotation, and link destinations preserved across all 260 book pages. Existing bookmarks preserved, except Harvey’s first bookmark now uses its canonical title; its destination remains page 1.
- PDF title metadata reconciled for all nine files. Even Weather and Harvey have changed file hashes because their metadata was updated; no revised PDF is described as a byte-identical original.
- All PDFs remain searchable/vector documents. Titles and replacement text use embedded fonts.
- The standalone revised catalog and the catalog inside the ZIP are identical final bytes.
- Final ZIP was reopened to verify CRCs, manifest entries, index hashes/paths, page counts, and catalog identity.
- Originals remain unchanged. No substantive evidence re-audit or status promotion was performed.

## Preservation boundaries

Running editorial headers, footers, reading-guide references, and index headings were reconciled. Historical exhibit titles, screenshot content, source paths, dates, and evidence qualifications remain source material. References to source manifests in historical interior text remain preserved; this update does not fabricate missing historical companions.

## Original input identities

- Grounded_DI_Book_Collection_2026-09(1).zip: `ff3b2994ff3e8fa2f154b9f369df75657d11f7ae6cac2e0ef5805b0a304ced85`
- Grounded_DI_Master_Book_Catalog(1).pdf: `1e6f064a365e1ffd799e1e30b5b7c9676e2e3ba6a01d5c48ff27dfde4edd5495`

No unresolved cover, navigation, pagination, or packaging defect was identified in this revision.
