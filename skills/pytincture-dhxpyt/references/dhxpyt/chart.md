# dhxpyt.chart

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### AreaChartConfig
Configuration for Area chart.

```python
AreaChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### BarChartConfig
Configuration for Bar chart.

```python
BarChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### CalendarHeatMapChartConfig
Configuration for Calendar Heatmap chart.

```python
CalendarHeatMapChartConfig(
    series: List[Dict[str, Any]],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### ChartConfig
Base configuration class for DHTMLX Chart.

```python
ChartConfig(
    type: str,
    series: List[Dict[str, Any]],
    scales: Optional[Dict[str, Any]] = None,
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### ControlConfig
Base class for control configurations.

_No keyword parameters._

### DonutChartConfig
Configuration for Donut chart.

```python
DonutChartConfig(
    series: List[Dict[str, Any]],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### LineChartConfig
Configuration for Line chart.

```python
LineChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### Pie3DChartConfig
Configuration for Pie 3D chart.

```python
Pie3DChartConfig(
    series: List[Dict[str, Any]],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### PieChartConfig
Configuration for Pie chart.

```python
PieChartConfig(
    series: List[Dict[str, Any]],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### RadarChartConfig
Configuration for Radar chart.

```python
RadarChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### ScatterChartConfig
Configuration for Scatter chart.

```python
ScatterChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### SplineAreaChartConfig
Configuration for SplineArea chart.

```python
SplineAreaChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### SplineChartConfig
Configuration for Spline chart.

```python
SplineChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### TreeMapChartConfig
Configuration for Treemap chart.

```python
TreeMapChartConfig(
    series: List[Dict[str, Any]],
    legend: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    css: Optional[str] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

### XBarChartConfig
Configuration for X-Bar (horizontal Bar) chart.

```python
XBarChartConfig(
    series: List[Dict[str, Any]],
    scales: Dict[str, Any],
    data: Optional[List[Dict[str, Any]]] = None,
    legend: Optional[Dict[str, Any]] = None,
    css: Optional[str] = None,
    max_points: Optional[int] = None,
    export_styles: Union[bool, List[str]] = False,
)
```

## Widget classes

### Chart
Python wrapper for DHTMLX Chart.

```python
destructor() -> None
each_series(handler: Callable[[List[Dict[str, Any]]], Any]) -> List[Any]
get_series(id: str) -> Dict[str, Any]
paint() -> None
set_config(config: Dict[str, Any]) -> None
png(config: Dict[str, Any] = {}) -> None
pdf(config: Dict[str, Any] = {}) -> None
add_event_handler(event_name: str, handler: Callable) -> None
resize(handler: Callable[[int, int], None]) -> None
serie_click(handler: Callable[[str, str], None]) -> None
toggle_series(handler: Callable[[str, Union[Dict[str, Any], None]], None]) -> None
css() -> str
css(value: str) -> None
data() -> List[Dict[str, Any]]
data(value: List[Dict[str, Any]]) -> None
export_styles() -> Union[bool, List[str]]
export_styles(value: Union[bool, List[str]]) -> None
legend() -> Dict[str, Any]
legend(value: Dict[str, Any]) -> None
max_points() -> int
max_points(value: int) -> None
scales() -> Dict[str, Any]
scales(value: Dict[str, Any]) -> None
series() -> List[Dict[str, Any]]
series(value: List[Dict[str, Any]]) -> None
type() -> str
type(value: str) -> None
```
