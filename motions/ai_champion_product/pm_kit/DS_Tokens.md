# Design system tokens for prototypes

**DS v1 per the Skills Editor PRD v2.0 (May 2026). Replace with design's current sheet.** When design provides the current token sheet, attach that file to the Project instead of this one; the builder uses whichever sheet is attached.

## Colour
| Token | Value | Use |
|---|---|---|
| primary | `#5AB274` | Primary buttons, active tab underline, active row left border, links |
| primary dark | `#158235` | Hover and emphasis on primary |
| primary tint | `rgba(90,178,116,0.12)` | Selected row background |
| page background | `#F8F8F8` | Page and sidebar background, table header rows |
| surface | `#FFFFFF` | Cards, panels, dialogs |
| border | `#E5E5E5` | Borders, dividers, sidebar right edge |
| input border | `rgba(0,0,0,0.23)` | Inputs and selects |
| text | `#202020` | Body text |
| secondary text | `#757575` | Labels, hints, metadata |
| status green / amber / red | `#5AB274` / `#F5A623` / `#D0021B` | Health and status indicators only |

Not for product chrome: `#014637`, `#2DB56E`, `#F58220` (marketing brand colours).

## Type
| Role | Face | Size |
|---|---|---|
| Body | Open Sans (fallback system-ui, Segoe UI, Arial) | 14px |
| Panel titles | Open Sans | 16px |
| Page titles | Open Sans | 20px |
| Labels, selects, table headers | Roboto (same fallback) | 11px to 13px |

Fonts are declared, never embedded or fetched.

## Shape and elevation
| Element | Spec |
|---|---|
| Button | 36px tall, 4px radius, 700 weight, 14px, letter-spacing 0.03em; primary `#5AB274` fill white text; secondary white fill, 1px `rgba(0,0,0,0.23)` border |
| Input, select | 36px tall, 4px radius, 1px `rgba(0,0,0,0.23)` border, Roboto 14px |
| Card, panel | 5px radius, shadow `0 4px 10px rgba(0,0,0,0.1)` |
| Dialog | 2px radius, shadow `0 19px 38px rgba(0,0,0,0.3)`, scrim `rgba(0,0,0,0.4)` |
| Table | header `#F8F8F8`, dividers `#E5E5E5`, rows 48px (40px in dense lists) |
| Sidebar | 256px, `#F8F8F8`, 1px `#E5E5E5` right border, inline SVG icons 24x24 filled |
| Toast | bottom-centre, `#202020`, white text, 4px radius, 3 seconds |

## Source
Skills Editor PRD, PRD-ICC-S2-001 v2.0, section 2 "Design system compliance", SharePoint engineering / Aldus Documents / Proof of Concepts / Aldus Modules Proof of Concepts / Intradiem Skills Editor. Token names there: `--id-green #5AB274`, `--id-dark-green #158235`, `--id-radius 5px`, `--id-radius-sm 4px`, `--id-radius-dialog 2px`, `--id-bg #F8F8F8`, `--id-border #E5E5E5`, `--id-text2 #757575`.
