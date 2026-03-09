#!/usr/bin/env python3
"""Skeleton ingestion pipeline for Revit/Lightwave -> Diorama mesh assets.

Sprint-1 objective:
- Document decimation and compression flow.
- Mock a 1,000,000 -> 10,000 triangle reduction target.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json


@dataclass
class IngestConfig:
    input_path: Path
    output_path: Path
    target_tris: int = 10_000
    source_tris: int = 1_000_000
    draco_level: int = 7


def detect_aec_source(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".rvt", ".ifc"}:
        return "revit"
    if suffix in {".lwo", ".lws"}:
        return "lightwave"
    return "unknown"


def strip_nonvisible_detail(source_tris: int) -> int:
    """Mock decimation phase 1: remove hidden screws/plumbing/interior micro-detail."""
    # Placeholder heuristic: keep 18% after culling tiny/invisible components.
    return int(source_tris * 0.18)


def create_diorama_lod(intermediate_tris: int, target_tris: int) -> int:
    """Mock decimation phase 2: preserve silhouette + wayfinding geometry."""
    # Placeholder: clamp to requested budget.
    return min(intermediate_tris, target_tris)


def draco_compress(mesh_name: str, draco_level: int) -> dict:
    """Mock Draco compression stage metadata."""
    return {
        "mesh": mesh_name,
        "codec": "draco",
        "compression_level": draco_level,
        "status": "simulated",
    }


def run_ingest(config: IngestConfig) -> dict:
    source_type = detect_aec_source(config.input_path)
    phase1_tris = strip_nonvisible_detail(config.source_tris)
    final_tris = create_diorama_lod(phase1_tris, config.target_tris)
    compression = draco_compress(config.input_path.stem, config.draco_level)

    report = {
        "input": str(config.input_path),
        "source_type": source_type,
        "triangle_counts": {
            "source": config.source_tris,
            "after_hidden_detail_cull": phase1_tris,
            "final_diorama_lod": final_tris,
            "target": config.target_tris,
        },
        "compression": compression,
        "next_steps": [
            "Integrate meshopt + quadric decimation for real geometry",
            "Add visibility sets by room/department",
            "Emit glb + draco payloads for WebGL wrapper",
        ],
    }

    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    config.output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    config = IngestConfig(
        input_path=Path("source/clinical_tower_mock.rvt"),
        output_path=Path("dist/ingest_report.json"),
    )
    report = run_ingest(config)
    print(
        f"Ingest skeleton complete: {report['triangle_counts']['source']} -> "
        f"{report['triangle_counts']['final_diorama_lod']} triangles"
    )


if __name__ == "__main__":
    main()
