# Next Sprints Implementation Status

This repository now includes starter implementation for the four requested sprint tracks.

## 1) Revit-to-Mesh ingestion prototype
- Added `scripts/ingest_aec.py` skeleton.
- Includes staged logic for:
  - source detection (`.rvt/.ifc/.lwo/.lws`)
  - hidden-detail culling pass
  - diorama LOD pass (1,000,000 -> 10,000 target)
  - Draco compression metadata handoff
- Emits `dist/ingest_report.json`.

## 2) Acoustic metadata tagging
- Build now emits `dist/asset_manifest.json`.
- Added `schemas/asset_manifest.schema.json` requiring `physical_properties` on every asset:
  - material
  - acoustic_absorption
  - reverb_profile

## 3) WebGL wrapper deployment hook
- Added `web/index.html` with a board-demo transition wrapper.
- Includes slider + "Simulate Stress Mode" button for exploration -> focus blend.
- Host locally with `make serve`.

## 4) Block-out asset library
- Added `assets/blockout_library.json` with:
  - `window_unit_A`
  - `wall_segment_B`
  - `skybridge_C`
- Each module has poly budget, chamfer target, dimensions, and material slots.
