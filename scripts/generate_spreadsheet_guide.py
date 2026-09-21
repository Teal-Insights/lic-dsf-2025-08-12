"""Generate spreadsheet reference pages from the extraction bindings."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
if (ROOT / "tests" / "bindings" / "inputs.bindings.yaml").exists():
    BINDINGS = ROOT / "tests" / "bindings"
    DOCS = ROOT / "user_guide" if (ROOT / "user_guide").is_dir() else ROOT / "docs"
    BINDINGS_LABEL = "tests/bindings"
elif (ROOT / "lic-dsf-2025-08-12" / "tests" / "bindings" / "inputs.bindings.yaml").exists():
    BINDINGS = ROOT / "lic-dsf-2025-08-12" / "tests" / "bindings"
    DOCS = ROOT / "docs"
    BINDINGS_LABEL = "lic-dsf-2025-08-12/tests/bindings"
else:
    raise SystemExit(f"Could not find inputs.bindings.yaml relative to {ROOT}")

SHEET_ORDER = [
    "Input 1 - Basics",
    "Input 2 - Debt Coverage",
    "Input 3 - Macro-Debt data(DMX)",
    "Input 6 - Tailored Tests",
    "Input 6(optional)-Standard Test",
    "Input 8 - SDR",
    "Chart Data",
    "Customized Scenario - public",
    "Customized Scenario-External",
    "BLEND floating calculations WB",
]

YELLOW_SHEETS = {
    "Input 1 - Basics",
    "Input 2 - Debt Coverage",
    "Input 3 - Macro-Debt data(DMX)",
    "Input 6 - Tailored Tests",
    "Input 6(optional)-Standard Test",
    "Input 8 - SDR",
}

_ID_PREFIXES = (
    "input3_input_3_macro_",
    "input3_input_3_external_debt_",
    "input3_input_3_",
    "in3_macro_",
    "input3_",
    "input6_",
    "input8_",
    "input_1_",
    "chart_output_chart_data_",
    "chart_",
    "customized_public_",
    "customized_external_",
    "blend_",
)

_ACRONYMS = {
    "dsa",
    "pv",
    "gdp",
    "sdr",
    "ppp",
    "soe",
    "ida",
    "mlt",
    "st",
    "fx",
    "mx",
    "rer",
    "ppg",
}
_SMALL_WORDS = {"of", "to", "and", "or"}


def _load(name: str) -> list[dict[str, Any]]:
    document = yaml.safe_load((BINDINGS / name).read_text(encoding="utf-8"))
    return document["series"]


def _escape(value: object) -> str:
    text = str(value).replace("\n", " ").replace("|", r"\|")
    return " ".join(text.split())


def _pretty_id(ident: str) -> str:
    for prefix in _ID_PREFIXES:
        if ident.startswith(prefix):
            ident = ident[len(prefix):]
            break
    words = ident.replace("_", " ").replace(".", " ").split()
    pretty = []
    for index, word in enumerate(words):
        lower = word.lower()
        if lower in _ACRONYMS or re.fullmatch(r"r\d+", lower):
            pretty.append(word.upper())
        elif lower in _SMALL_WORDS and index:
            pretty.append(lower)
        else:
            pretty.append(word.capitalize())
    return " ".join(pretty)


def _display_name(series: dict[str, Any]) -> str:
    context = series.get("series_context") or {}
    indicator = context.get("INDICATOR")
    if (
        isinstance(indicator, str)
        and re.search(r"[\s/%]", indicator)
        and not re.match(r"^(chart_|input\d)", indicator, re.IGNORECASE)
    ):
        return indicator.strip()
    return _pretty_id(series["id"])


def _table_title(table: str) -> str:
    return _pretty_id(table.split(".")[-1])


def _ranges(series: dict[str, Any]) -> str:
    ranges = series.get("data_range", "")
    if not isinstance(ranges, list):
        ranges = [ranges]
    return "<br>".join(f"`{_escape(item)}`" for item in ranges if item)


def _dimensions(series: dict[str, Any]) -> str:
    dimensions = series.get("structure", {}).get("dimensions", [])
    names = [item.get("concept") or item.get("id") for item in dimensions]
    return ", ".join(f"`{_escape(name)}`" for name in names if name) or "—"


def _domain(series: dict[str, Any]) -> str:
    domain = (series.get("input") or {}).get("domain") or {}
    if not domain:
        return "Workbook-defined"
    if "enum" in domain:
        values = domain["enum"]
        if len(values) <= 8:
            return ", ".join(f"`{_escape(value)}`" for value in values)
        sample = ", ".join(f"`{_escape(value)}`" for value in values[:5])
        return f"{sample}, … ({len(values)} allowed values)"
    for key in ("between", "real_between"):
        if key in domain:
            bounds = domain[key]
            return f"{_escape(bounds['min'])} to {_escape(bounds['max'])}"
    return _escape(domain)


def _dtype(series: dict[str, Any]) -> str:
    return _escape(
        series.get("structure", {}).get("measure", {}).get("dtype", "value")
    )


def _kind(sheet: str) -> str:
    return "Yellow input" if sheet in YELLOW_SHEETS else "Advanced control"


def _interpretation(series: dict[str, Any]) -> str:
    ident = series["id"]
    dtype = _dtype(series)
    if "applicable" in ident or ident.endswith("_breach"):
        return "`0` = no, `1` = yes"
    if ident.endswith("_numeric"):
        return "`1` Low, `2` Moderate, `3` High"
    if ident == "fiscal_space_moderate_risk_signal":
        return "`Limited space`, `Some space`, or `Substantial space`"
    if ident.endswith("_signal"):
        return "`Low`, `Moderate`, or `High`"
    if "mx_shock" in ident and dtype == "string":
        return "Most-extreme shock label"
    if series.get("layout") == "series":
        return "Path by named dimensions"
    return "—"


def _ordered_groups(
    series: list[dict[str, Any]], key, preferred: list[str]
) -> list[tuple[str, list[dict[str, Any]]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in series:
        grouped[key(item)].append(item)
    seen: set[str] = set()
    ordered: list[tuple[str, list[dict[str, Any]]]] = []
    for name in preferred:
        if name in grouped:
            ordered.append((name, grouped[name]))
            seen.add(name)
    for name, items in grouped.items():
        if name not in seen:
            ordered.append((name, items))
    return ordered


def _write(path: Path, content: str, *, check: bool) -> bool:
    content = content.rstrip() + "\n"
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return False
    if check:
        raise SystemExit(f"{path.relative_to(ROOT)} is out of date")
    path.write_text(content, encoding="utf-8")
    return True


def render_inputs(series: list[dict[str, Any]]) -> str:
    lines = [
        "---",
        'title: "Spreadsheet inputs"',
        'guide-section: "Spreadsheet Guide"',
        "---",
        "",
        "<!-- Generated by scripts/generate_spreadsheet_guide.py. Do not edit by hand. -->",
        "",
        "This reference is generated from",
        f"`{BINDINGS_LABEL}/inputs.bindings.yaml`.",
        "It maps published calculation inputs to workbook cells. Use the",
        "spreadsheet's yellow cells and built-in instructions as the primary",
        "workflow; rows marked **Advanced control** are calculation-sheet or",
        "customized-scenario settings, not a normal country-file starting point.",
        "",
        "Values must use the workbook's units, signs, labels, and year ordering.",
        "A range is one named series, not a set of interchangeable cells.",
        "Input 4 (external financing) and Input 5 (local-currency financing)",
        "remain yellow-cell inputs in the workbook even though they are stored",
        "in separate binding files and are not listed here.",
        "",
    ]

    for sheet, items in _ordered_groups(
        series, lambda item: item["sheet"], SHEET_ORDER
    ):
        lines.extend(
            [
                f"## {_escape(sheet)}",
                "",
                "| Input | Cell or range | Type | Dimensions | Allowed values | Kind | Purpose |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        for item in items:
            lines.append(
                "| {name} | {ranges} | `{dtype}` ({layout}) | {dimensions} | "
                "{domain} | {kind} | {notes} |".format(
                    name=_escape(_display_name(item)),
                    ranges=_ranges(item),
                    dtype=_dtype(item),
                    layout=_escape(item.get("layout", "scalar")),
                    dimensions=_dimensions(item),
                    domain=_domain(item),
                    kind=_kind(item["sheet"]),
                    notes=_escape(item.get("notes", "—")),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Scope",
            "",
            "This is the public input surface of the extracted calculation graph.",
            "It does not replace the workbook's validation messages, comments, or",
            "IMF/World Bank economic guidance, and it does not imply that every",
            "listed advanced control should be edited for a normal country DSA.",
            "",
            "---",
            "",
            "**Back to:** [Using the spreadsheet](08-spreadsheet-guide.qmd)",
        ]
    )
    return "\n".join(lines)


def render_outputs(series: list[dict[str, Any]]) -> str:
    lines = [
        "---",
        'title: "Spreadsheet outputs"',
        'guide-section: "Spreadsheet Guide"',
        "---",
        "",
        "<!-- Generated by scripts/generate_spreadsheet_guide.py. Do not edit by hand. -->",
        "",
        "This reference is generated from",
        f"`{BINDINGS_LABEL}/outputs.bindings.yaml`.",
        "It covers the published **Chart Data** calculation surface: mechanical",
        "risk signals and the scenario paths behind the standard debt-stress",
        "figures. These are selected Chart Data results, not every formatted",
        "cell on Outputs 1–7.",
        "",
        "A scalar is one cell. A series is identified by its named dimensions,",
        "commonly scenario and projection year.",
        "",
    ]

    for table, items in _ordered_groups(
        series,
        lambda item: (item.get("series_context") or {}).get("TABLE", item["sheet"]),
        [],
    ):
        lines.extend(
            [
                f"## {_escape(_table_title(table))}",
                "",
                "| Output | Cell or range | Type | Dimensions | Values | Meaning |",
                "|---|---|---|---|---|---|",
            ]
        )
        for item in items:
            lines.append(
                "| {name} | {ranges} | `{dtype}` ({layout}) | {dimensions} | "
                "{values} | {notes} |".format(
                    name=_escape(_display_name(item)),
                    ranges=_ranges(item),
                    dtype=_dtype(item),
                    layout=_escape(item.get("layout", "scalar")),
                    dimensions=_dimensions(item),
                    values=_escape(_interpretation(item)),
                    notes=_escape(item.get("notes", "—")),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Scope",
            "",
            "Realism diagnostics (Output 4), the probability approach (Output 6),",
            "narrative judgement, chart formatting, and workbook macros remain",
            "separate spreadsheet surfaces. Realism and probability do not feed",
            "the mechanical risk rating.",
            "",
            "---",
            "",
            "**Back to:** [Using the spreadsheet](08-spreadsheet-guide.qmd)",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if committed guide pages differ from the bindings.",
    )
    args = parser.parse_args()

    changed = [
        _write(
            DOCS / "09-spreadsheet-inputs.qmd",
            render_inputs(_load("inputs.bindings.yaml")),
            check=args.check,
        ),
        _write(
            DOCS / "10-spreadsheet-outputs.qmd",
            render_outputs(_load("outputs.bindings.yaml")),
            check=args.check,
        ),
    ]
    if any(changed):
        print("Updated spreadsheet input/output guide pages.")
    elif not args.check:
        print("Spreadsheet guide pages are already current.")


if __name__ == "__main__":
    main()
