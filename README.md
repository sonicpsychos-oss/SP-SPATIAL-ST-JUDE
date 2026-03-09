# SP-SPATIAL-ST-JUDE · Visual Prototype Build

## Build visual frames + metadata

```bash
make build
```

Outputs:
- `dist/frame1_donor_reveal.svg`
- `dist/frame2_trauma_informed_pivot.svg`
- `dist/frame3_feasibility_triptych.svg`
- `dist/asset_manifest.json`
- `schemas/asset_manifest.schema.json`
- `assets/blockout_library.json`

## Run ingestion skeleton

```bash
make ingest
```

Creates `dist/ingest_report.json` and demonstrates mock decimation + Draco compression stages from 1M -> 10k triangle target.

## Launch board-demo wrapper

```bash
make serve
# then open http://localhost:8000/web/
```

The page includes a slider and **Simulate Stress Mode** button to transition from exploration view (Frame 1) to focus view (Frame 2).

## Brand/performance guardrails represented
- Red pathing avoided; red reserved for logo marker only.
- Navigation path uses Pantone 108C approximation (`#F4D000`).
- Metadata includes `physical_properties` for sensory-ready geometry.
- Asset kit-bash library includes Window Unit A, Wall Segment B, Sky-bridge C.
