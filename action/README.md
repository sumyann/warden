# Warden MCP Scan (GitHub Action)

Composite action wrapping the `warden` CLI. Installs `warden-mcp` from PyPI,
scans a path, writes a SARIF file, and fails the job if any finding meets
the configured severity threshold.

## Usage

```yaml
name: Warden MCP Scan
on: [push, pull_request]

permissions:
  contents: read
  security-events: write   # needed to upload SARIF to the Security tab

jobs:
  warden:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: sumyann/warden/action@main
        id: warden
        with:
          path: "."
          fail-on: high

      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: ${{ steps.warden.outputs.sarif-file }}
```

## Inputs

| Input          | Default              | Description                                                              |
|----------------|-----------------------|----------------------------------------------------------------------------|
| `path`         | `.`                   | Path to scan, relative to the repo root.                                 |
| `fail-on`      | `high`                | Minimum severity that fails the job: `critical`, `high`, `medium`, `low`, `none`. |
| `sarif-output` | `warden-results.sarif`| Where to write the SARIF file.                                           |
| `server-name`  | `${{ github.repository }}` | Label shown in scan output.                                        |

## Outputs

| Output       | Description                     |
|--------------|----------------------------------|
| `sarif-file` | Path to the generated SARIF file. |
