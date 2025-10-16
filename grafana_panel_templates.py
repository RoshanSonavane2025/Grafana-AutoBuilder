aliases={
    "bar": "bar",
    "bargraph": "bar",
    "barchart": "bar",
    "grouped bar": "grouped_bar",
    "groupedbar": "grouped_bar",
    "grouped bar chart": "grouped_bar",
    "groupedbarchart": "grouped_bar",
       
    "timeseries": "timeseries",
    "linechart": "line",
    "statdisplay": "stat",
    "value": "stat",
    "number": "stat",
    "tabular": "table",
    "tableview": "table",
    "pie": "piechart",
    "donut": "piechart",
    "piechart": "piechart",
    "histogram": "histogram",
    "line": "line",
    "html": "htmlgraphics",
    "htmlgraphic": "htmlgraphics",
    "htmlpanel": "htmlgraphics",
    "textwithhtml": "htmlgraphics",
    "gauge": "gauge",
    "guage": "gauge",
    "echarts": "htmlgraphics",
    "echart": "htmlgraphics",
    "volkov": "htmlgraphics",
    "volkovlabs": "htmlgraphics",
    "echarts panel": "htmlgraphics",
    "volkovlabs echarts panel": "htmlgraphics",
    "volkovlabsechartspanel": "htmlgraphics",
    "text": "htmlgraphics",
    "volkovlabs echarts panel": "htmlgraphics",
    "volkovlabsechartspanel": "htmlgraphics",
    
}



colorPalette= ['#053f73', '#009ac7', '#58eae8', '#1f78b4', '#a6cee3']
PANEL_TEMPLATES =  {
"stat": 
{
"type": "stat",
"title": "{{ Title }}",
"description": "{{ Description }}",
"gridPos": {
            "x": 0,
            "y": 0,
            "h": 5,
            "w": 4
            },
"fieldConfig": {
"defaults": {
    "mappings": [],
    "thresholds": {
        "mode": "absolute",
        "steps": [
            {
                "color": "#053f73",
                "value": None
            }
        ]
    },
    "color": {
        "mode": "thresholds"
    },
    "links": []
},
"overrides": []
},
"pluginVersion": "11.5.2",
"targets": [
{
    "editorMode": "code",
    "format": "table",
    "rawQuery": True,
    "rawSql": "{{ SQL }}",
    "refId": "A",
}
],
"datasource": {"type": "grafana-postgresql-datasource", "uid": "default"},
"options": {
"reduceOptions": {
    "values": False,
    "calcs": [
        "lastNotNull"
    ],
    "fields": ""
},
"orientation": "auto",
"textMode": "auto",
"wideLayout": True,
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"showPercentChange": False,
"percentChangeColorMode": "standard",
"text": {
    "valueSize": 60
}
}
}
,   
"table": 
{
      "type": "table",
      "title": "Table Panel",
      "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8},
      "pluginVersion": "11.5.2",
      "targets": [{"refId": "A", "format": "table", "rawSql": ""}],
      "datasource": {"type": "grafana-postgresql-datasource", "uid": "default"}
    }
,
"grouped_bar":
  {
  "type": "barchart",
  "title": "{{Title}}",
  "description": "{{Description}}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 8,
    "w": 12
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "lineWidth": 1,
        "fillOpacity": 80,
        "gradientMode": "none",
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": False,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "continuous-blues",
        "fixedColor": "text"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "value": None,
            "color": "green"
          },
          {
            "value": 80,
            "color": "red"
          }
        ]
      }
    },
    "overrides": []
  },
  "pluginVersion": "11.5.2",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{rawSQL}}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "orientation": "auto",
    "xTickLabelRotation": 0,
    "xTickLabelSpacing": 0,
    "showValue": "auto",
    "stacking": "none",
    "groupWidth": 0.7,
    "barWidth": 0.97,
    "barRadius": 0,
    "fullHighlight": False,
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": False
    },
    "legend": {
      "showLegend": True,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
},

"bar": 
{
"type": "volkovlabs-echarts-panel",
"title": "{{ Title }}",
"description": "{{ Description }}",
"gridPos": {
"x": 0,
"y": 0,
"h": 8,
"w": 12
},
"pluginVersion": "11.5.2",
"targets": [
{
    "editorMode": "code",
    "format": "table",
    "rawQuery": True,
    "rawSql": "{{ SQL }}",
    "refId": "A",
}
],
"datasource": {"type": "grafana-postgresql-datasource", "uid": "default"},
"options": {
"renderer": "canvas",
"map": "none",
"themeEditor": {"name": "default", "config": "{}"},
"baidu": {"key": "", "callback": "bmapReady"},
"gaode": {"key": "", "plugin": "AMap.Scale,AMap.ToolBar"},
"google": {"key": "", "callback": "gmapReady"},
"editorMode": "visual",
"editor": {"format": "auto"},
"visualEditor": {
    "dataset": [],
    "series": [],
    "code": """
let categories = [];
let values = [];
let colors = {}; // Define your color mapping here, e.g., { "Frontend Team": "#053f73", "Backend Team": "#58eae8" }

if (context.panel.data.series.length > 0) {
const series = context.panel.data.series[0];
const categoryField = series.fields.find(f => f.type === 'string');
const valueField = series.fields.find(f => f.type === 'number');

if (categoryField && valueField) {
for (let i = 0; i < categoryField.values.length; i++) {
categories.push(categoryField.values[i]);
values.push(valueField.values[i]);
}
}
}

return {
backgroundColor: 'transparent',
color: ['#053f73', '#009ac7', '#58eae8', '#1f78b4', '#a6cee3'],
tooltip: {
trigger: 'axis',
axisPointer: {
type: 'shadow'
},
formatter: function (params) {
const index = params[0].dataIndex;
return `<strong>${categories[index]}</strong><br/>Value: ${values[index]}%`;
}
},
grid: {
left: '3%',
right: '4%',
bottom: '3%',
containLabel: true
},
xAxis: {
type: 'category',
data: categories,
axisTick: {
alignWithLabel: true
},
    axisLabel: {
      interval: 0,
      rotate: 30,
      formatter: function (value) {
        return value.length > 15 ? value.substring(0, 15) + '…' : value;
      }
    }
},
yAxis: {
type: 'value',
min: 0,
axisLabel: { formatter: '{value}' }
},
series: [
{
name: 'Value',
type: 'bar',
data: values.map((value, index) => ({
value: value,
itemStyle: {
  color: colors[categories[index]] || '#053f73',
  borderRadius: [6, 6, 0, 0]
}
})),
label: {
show: true,
position: 'top',
formatter: '{c}'
}
}
]
};
""",
},
"getOption": """
return {};
""",
},
},
"horizontal_bar": 
{
  "id": 3,
  "type": "volkovlabs-echarts-panel",
  "title": "{{Title}}",
  "description": "{{Description}}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 10,
    "w": 10
  },
  "fieldConfig": {
    "defaults": {},
    "overrides": []
  },
  "pluginVersion": "6.6.0",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{rawSQL}}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "renderer": "canvas",
    "map": "none",
    "themeEditor": {
      "name": "default",
      "config": "{}"
    },
    "baidu": {
      "key": "",
      "callback": "bmapReady"
    },
    "gaode": {
      "key": "",
      "plugin": "AMap.Scale,AMap.ToolBar"
    },
    "google": {
      "key": "",
      "callback": "gmapReady"
    },
    "editorMode": "visual",
    "editor": {
      "format": "auto"
    },
    "visualEditor": {
      "dataset": [],
      "series": [],
      "code": "const yAxisFieldName = `${context.panel.data.series[0].fields[1].name}`;\nconst xAxisFieldName = `${context.panel.data.series[0].fields[0].name}`;\nlet colors = ['#053f73', '#58eae8', '#009ac7', '#00B2CC', '#4682B4'];\n\nlet xAxisData = context.panel.data.series[0].fields[1].values.toArray();\nlet yAxisData = context.panel.data.series[0].fields[0].values.toArray();\n\nreturn {\n  tooltip: {\n    trigger: 'axis',\n    axisPointer: { type: 'shadow' },\n    formatter: '{b}: {c}'\n  },\n  grid: {\n    left: '5%',\n    right: '5%',\n    bottom: '10%',\n    top: '15%',\n    containLabel: true\n  },\n  xAxis: {\n    type: 'value',\n    min: 0,\n    axisLabel: {\n      formatter: '{value}'\n    }\n  },\n  yAxis: {\n    type: 'category',\n    data: yAxisData,\n    axisLabel: {\n      fontSize: 12\n    }\n  },\n  series: [\n    {\n      name: 'Backup Coverage',\n      type: 'bar',\n      data: xAxisData.map((value, index) => ({\n        value: value,\n        itemStyle: {\n          color: colors[index % colors.length],\n          borderRadius: [0, 8, 8, 0]\n        }\n      })),\n      barWidth: 20,\n      label: {\n        show: true,\n        position: 'right',\n        formatter: '{c}'\n      }\n    }\n  ]\n};"
    },
    "getOption": "const series = context.panel.data.series.map((s) => {\n  const sData = s.fields.find((f) => f.type === 'number').values.buffer || s.fields.find((f) => f.type === 'number').values;\n  const sTime = s.fields.find((f) => f.type === 'time').values.buffer || s.fields.find((f) => f.type === 'time').values;\n  \n  return {\n    name: s.refId,\n    type: 'line',\n    showSymbol: false,\n    areaStyle: {\n      opacity: 0.1,\n    },\n    lineStyle: {\n      width: 1,\n    },\n    data: sData.map((d, i) => [sTime[i], d.toFixed(2)]),\n  };\n});\n\n/**\n * Enable Data Zoom by default\n */\nsetTimeout(() => context.panel.chart.dispatchAction({\n  type: 'takeGlobalCursor',\n  key: 'dataZoomSelect',\n  dataZoomSelectActive: true,\n}), 500);\n\n/**\n * Update Time Range on Zoom\n */\ncontext.panel.chart.on('datazoom', function (params) {\n  const startValue = params.batch[0]?.startValue;\n  const endValue = params.batch[0]?.endValue;\n  locationService.partial({ from: startValue, to: endValue });\n});\n\nreturn {\n  backgroundColor: 'transparent',\n  tooltip: {\n    trigger: 'axis',\n  },\n  legend: {\n    left: '0',\n    bottom: '0',\n    data: context.panel.data.series.map((s) => s.refId),\n    textStyle: {\n      color: 'rgba(128, 128, 128, .9)',\n    },\n  },\n  toolbox: {\n    feature: {\n      dataZoom: {\n        yAxisIndex: 'none',\n        icon: {\n          zoom: 'path://',\n          back: 'path://',\n        },\n      },\n      saveAsImage: {},\n    }\n  },\n  xAxis: {\n    type: 'time',\n  },\n  yAxis: {\n    type: 'value',\n    min: 'dataMin',\n  },\n  grid: {\n    left: '2%',\n    right: '2%',\n    top: '2%',\n    bottom: 24,\n    containLabel: true,\n  },\n  series,\n};"
  }
},
"piechart": 
{
  "type": "volkovlabs-echarts-panel",
  "title": "{{ Title }}",
  "description": "{{ Description }}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 11,
    "w": 11
  },
  "fieldConfig": {
    "defaults": {},
    "overrides": []
  },
  "pluginVersion": "6.6.0",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{ SQL }}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "renderer": "canvas",
    "map": "none",
    "themeEditor": {
      "name": "default",
      "config": "{}"
    },
    "baidu": {
      "key": "",
      "callback": "bmapReady"
    },
    "gaode": {
      "key": "",
      "plugin": "AMap.Scale,AMap.ToolBar"
    },
    "google": {
      "key": "",
      "callback": "gmapReady"
    },
    "editorMode": "visual",
    "editor": {
      "format": "auto"
    },
    "visualEditor": {
      "dataset": [],
      "series": [],
      "code": "const seriesData = [];\nconst colors = { \"Completed Training\": \"#053f73\", \"Pending Training\": \"#58eae8\" }; // Define your color map\n\nif (context.panel.data.series.length > 0) {\n  context.panel.data.series.forEach(series => {\n    const categoryField = series.fields.find(f => f.type === 'string');\n    const valueField = series.fields.find(f => f.type === 'number');\n\n    if (categoryField && valueField) {\n      for (let i = 0; i < categoryField.values.length; i++) {\n        seriesData.push({\n          name: categoryField.values[i],\n          value: valueField.values[i],\n          itemStyle: {\n            color: colors[categoryField.values[i]] || null // Use mapped color\n          }\n        });\n      }\n    }\n  });\n}\nreturn {\n\n  tooltip: {\n\n    trigger: 'item',\n\n    formatter: '{b} : {c} ({d}%)'\n\n  },\n\n  legend: {\n\n    orient: \"horizontal\",\n\n    bottom: \"bottom\",\n\n    data: seriesData.map(item => item.name)\n\n  },\n\n  series: [\n\n    {\n\n      name: 'Compliance',\n\n      type: 'pie',\n\n      radius: '65%',\n\n      data: seriesData,\n      itemStyle: {\n        borderRadius: 3,\n        borderColor: '#fff',\n        borderWidth: 2,\n      },\n      emphasis: {\n\n        itemStyle: {\n          borderRadius: 3,\n          borderColor: '#fff',\n          borderWidth: 2,\n\n\n          shadowBlur: 10,\n\n          shadowOffsetX: 0,\n\n          shadowColor: 'rgba(0, 0, 0, 0.5)'\n\n        }\n\n      },\n\n      label: {\n\n        show: true,\n\n        position: 'outside',\n\n        formatter: '{box|{b} : {c} ({d}%)}',\n\n        rich: {\n\n          box: {\n\n            backgroundColor: '#eef6ff',\n\n            borderColor: '#0055aa',\n\n            borderWidth: 1,\n\n            borderRadius: 6,\n\n            padding: [4, 6],\n\n            fontSize: 13,\n\n            fontWeight: 'bold',\n\n            color: '#0055aa',\n\n            lineHeight: 18,\n\n            align: 'center'\n\n          }\n\n        }\n\n      },\n\n      labelLine: {\n\n        show: true,\n\n        length: 15,\n\n        length2: 10\n\n      },\n\n      color: ['#053f73', '#58eae8', '#009ac7', '#A7C7E7', '#4682B4']\n\n    }\n\n  ]\n\n};\n\n"
    },
    "getOption": "\nreturn {};\n"
  }

},
"line":{
  "id": 23,
  "type": "volkovlabs-echarts-panel",
  "title": "{{Title}}",
  "description": "{{Description}}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 10,
    "w": 10
  },
  "fieldConfig": {
    "defaults": {},
    "overrides": []
  },
  "pluginVersion": "6.6.0",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{rawSQL}}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "renderer": "canvas",
    "map": "none",
    "themeEditor": {
      "name": "default",
      "config": "{}"
    },
    "baidu": {
      "key": "",
      "callback": "bmapReady"
    },
    "gaode": {
      "key": "",
      "plugin": "AMap.Scale,AMap.ToolBar"
    },
    "google": {
      "key": "",
      "callback": "gmapReady"
    },
    "editorMode": "visual",
    "editor": {
      "format": "auto"
    },
    "visualEditor": {
      "dataset": [],
      "series": [],
      "code": "const xAxisFieldName = `${context.panel.data.series[0].fields[0].name}`;\nconst yAxisFieldName = `${context.panel.data.series[0].fields[1].name}`;\n\nlet xAxisData = [];\nlet yAxisData = [];\n\n\n// Extract data from the Grafana series. Assumes data is in the first series.\nif (context.panel.data.series.length > 0) {\n  const series = context.panel.data.series[0];\n  const xAxisField = series.fields.find(f => f.name.toLowerCase().includes(xAxisFieldName.toLowerCase()));\n  const yAxisField = series.fields.find(f => f.name.toLowerCase().includes(yAxisFieldName.toLowerCase()));\n\n  if (xAxisField && yAxisField) {\n    for (let i = 0; i < xAxisField.values.length; i++) {\n      let xValue = xAxisField.values[i];\n      let yValue = yAxisField.values[i];\n\n      if (typeof xValue === 'number') {\n        xValue = parseFloat(xValue.toFixed(2));\n      }\n      if (typeof yValue === 'number') {\n        yValue = parseFloat(yValue.toFixed(2));\n      }\n\n      xAxisData.push(xValue);\n      yAxisData.push(yValue);\n    }\n  } else {\n    console.warn('ECharts Panel: X or Y axis field not found. Check field names in SQL query and panel parameters.');\n  }\n} else {\n  console.warn('ECharts Panel: No data series found.');\n}\n\n// Configure the series based on the chart type.\nconst seriesConfig = {\n  type: 'line', // Apply smoothing only for line charts\n  data: yAxisData,\n  lineStyle: { color: '#009ac7', width: 3 }, // Line style for line charts\n  itemStyle: { color: '#009ac7' }, // Item style for points/bars\n  label: { show: true, position: 'top', formatter: '{c}' }\n};\n\nseriesConfig.areaStyle = {\n  color: '',\n};\n\nreturn {\n  grid: {\n    left: '10%',\n    right: '5%',\n    top: '10%',\n    bottom: '15%'\n  },\n  backgroundColor: 'transparent',\n  tooltip: {\n    trigger: 'axis',\n    formatter: function (params) {\n      const index = params[0].dataIndex;\n      return `<strong> ${xAxisFieldName}:</strong> ${xAxisData[index]}<br/>\n      <strong>${yAxisFieldName}:</strong> ${yAxisData[index]}`;\n    }\n  },\n  xAxis: {\n    type: 'category',\n    data: xAxisData,\n    nameLocation: 'middle',\n    nameGap: 45,\n    axisLabel: {\n      fontSize: 12\n    }\n  },\n  yAxis: {\n    type: 'value',\n    min: 0,\n    axisLabel: {\n      formatter: '{value}'\n    }\n  },\n  series: [\n    {\n      name: 'Title',\n      type: 'line',\n      data: yAxisData,\n      smooth: true,\n      lineStyle: {\n        color: '#009ac7',\n        width: 3\n      },\n      itemStyle: {\n        color: '#053f73'\n      },\n      label: {\n        show: true,\n        position: 'top',\n        formatter: '{c}'\n      },\n      areaStyle: {\n        color: {\n          type: 'linear',\n          x: 0,\n          y: 0,\n          x2: 0,\n          y2: 1,\n          colorStops: [\n            { offset: 0, color: 'rgba(88,234,232,0.6)' },\n            { offset: 1, color: 'rgba(5,63,115,0.1)' }\n          ]\n        }\n      }\n    }\n  ]\n};"
    },
    "getOption": "const series = context.panel.data.series.map((s) => {\n  const sData = s.fields.find((f) => f.type === 'number').values.buffer || s.fields.find((f) => f.type === 'number').values;\n  const sTime = s.fields.find((f) => f.type === 'time').values.buffer || s.fields.find((f) => f.type === 'time').values;\n  \n  return {\n    name: s.refId,\n    type: 'line',\n    showSymbol: false,\n    areaStyle: {\n      opacity: 0.1,\n    },\n    lineStyle: {\n      width: 1,\n    },\n    data: sData.map((d, i) => [sTime[i], d.toFixed(2)]),\n  };\n});\n\n/**\n * Enable Data Zoom by default\n */\nsetTimeout(() => context.panel.chart.dispatchAction({\n  type: 'takeGlobalCursor',\n  key: 'dataZoomSelect',\n  dataZoomSelectActive: true,\n}), 500);\n\n/**\n * Update Time Range on Zoom\n */\ncontext.panel.chart.on('datazoom', function (params) {\n  const startValue = params.batch[0]?.startValue;\n  const endValue = params.batch[0]?.endValue;\n  locationService.partial({ from: startValue, to: endValue });\n});\n\nreturn {\n  backgroundColor: 'transparent',\n  tooltip: {\n    trigger: 'axis',\n  },\n  legend: {\n    left: '0',\n    bottom: '0',\n    data: context.panel.data.series.map((s) => s.refId),\n    textStyle: {\n      color: 'rgba(128, 128, 128, .9)',\n    },\n  },\n  toolbox: {\n    feature: {\n      dataZoom: {\n        yAxisIndex: 'none',\n        icon: {\n          zoom: 'path://',\n          back: 'path://',\n        },\n      },\n      saveAsImage: {},\n    }\n  },\n  xAxis: {\n    type: 'time',\n  },\n  yAxis: {\n    type: 'value',\n    min: 'dataMin',\n  },\n  grid: {\n    left: '2%',\n    right: '2%',\n    top: '2%',\n    bottom: 24,\n    containLabel: true,\n  },\n  series,\n};"
  }
},
"histogram": 
{
"type": "histogram",
"title": "{{ Title }}",
"description": "{{ Description }}",
  "gridPos": {
"x": 0,
"y": 0,
"h": 8,
"w": 12
},
"pluginVersion": "11.5.2",
"targets": [{"refId": "A", "format": "table", "rawSql": "{{ SQL }}", "exemplar": True}],
"datasource": {"type": "grafana-postgresql-datasource", "uid": "default"},
"fieldConfig": {
    "defaults": {
        "color": {"mode": "palette-classic"},
        "unit": "{{ Unit }}",
        "decimals": "{{ Decimals }}"
    },
    "overrides": []
},
"options": {
    "legend": {"displayMode": "list", "placement": "bottom", "showValues": False},
    "tooltip": {"mode": "single"}
}
},

"timeseries": 
{
  "id": 26,
  "type": "timeseries",
  "title": "{{Title}}",
  "description": "{{Description}}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 8,
    "w": 11
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "barWidthFactor": 0.6,
        "lineWidth": 1,
        "fillOpacity": 50,
        "gradientMode": "opacity",
        "spanNulls": False,
        "insertNulls": False,
        "showPoints": "auto",
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": False,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": False,
        "hideFrom": {
          "tooltip": False,
          "viz": False,
          "legend": False
        },
        "thresholdsStyle": {
          "mode": "off"
        }
      },
      "color": {
        "mode": "fixed",
        "fixedColor": "#053f73"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "blue",
            "value": None
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      }
    },
    "overrides": []
  },
  "pluginVersion": "11.5.2",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{rawSQL}}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": False
    },
    "legend": {
      "showLegend": True,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
}
,
 "htmlgraphics":  {
  "type": "gapit-htmlgraphics-panel",
  "title": "{{ Title }}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 7,
    "w": 24
  },
  "fieldConfig": {
    "defaults": {
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          { "color": "green", "value": None },
          { "color": "red", "value": 80 }
        ]
      },
      "color": {
        "mode": "thresholds"
      }
    },
    "overrides": []
  },
  "transparent": True,
  "pluginVersion": "11.5.2",
  "targets": [
    {
      "datasource": { "type": "grafana-postgresql-datasource", "uid": "default" },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{ SQL }}",
      "refId": "A"
    }
  ],
  "options": {
    "calcsMutation": "standard",
    "reduceOptions": {
      "calcs": ["lastNotNull"],
      "values": False,
      "fields": ""
    },
    "add100Percentage": True,
    "centerAlignContent": True,
    "overflow": "visible",
    "useGrafanaScrollbar": True,
    "SVGBaseFix": True,
    "rootCSS": "body{\n  background-color: white;\n}",
    "css": "body {\n    background-color: #f8fafc;\n    margin: 0;\n    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;\n    padding: 24px;\n}\n\n.metrics-container {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n    gap: 24px;\n    margin: 0 auto;\n    \n}\n\n.metric-card {\n    background: white;\n    border-radius: 16px;\n    padding: 24px;\n    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);\n    transition: all 0.3s ease;\n    border: 1px solid #e2e8f0;\n    display: flex;\n    flex-direction: column;\n    height: 80px;\n}\n\n.metric-card:hover {\n    transform: translateY(-4px);\n    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);\n}\n\n.metric-header {\n    display: flex;\n    align-items: center;\n    justify-content: space-between;\n}\n\n.metric-icon {\n    width: 40px;\n    height: 40px;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    border-radius: 12px;\n    background-color: #f8fafc;\n    padding: 8px;\n}\n\n.metric-icon svg {\n    width: 24px;\n    height: 24px;\n    transition: all 0.3s ease;\n}\n\n.metric-title {\n    font-size: 0.9rem;\n    color: #64748b;\n    font-weight: 600;\n    text-transform: uppercase;\n    letter-spacing: 0.5px;\n    flex: 1;\n    margin-right: 16px;\n}\n\n.metric-value {\n    font-size: 2.5rem;\n    font-weight: 700;\n    margin: 2px 0;\n    line-height: 1;\n    transition: color 0.3s ease;\n}\n\n.metric-description {\n    font-size: 0.875rem;\n    color: #64748b;\n    line-height: 1.5;\n    margin-top: auto;\n}\n\n/* Color schemes with improved contrast */\n.total {\n    border-bottom: 4px solid #3b82f6;  /* Changed to blue */\n}\n.total .metric-icon {\n    background-color: #eff6ff;\n}\n.total .metric-icon svg {\n    color: #3b82f6;\n}\n.total .metric-value {\n    color: #2563eb;\n}\n\n.critical {  /* This is \"healthy status\" */\n    border-bottom: 4px solid #ef4444;  /* Changed to green */\n}\n.critical .metric-icon {\n    background-color: #fef2f2;\n}\n.critical .metric-icon svg {\n    color: #ef4444;\n}\n.critical .metric-value {\n    color: #dc2626;\n}\n\n.patched {  /* This is \"up to date\" */\n    border-bottom: 4px solid #22c55e;  /* Changed to orange */\n}\n.patched .metric-icon {\n    background-color: #f0fdf4;\n}\n.patched .metric-icon svg {\n    color: #22c55e;\n}\n.patched .metric-value {\n    color: #16a34a;\n}\n\n.open-state {  /* user action */\n    border-bottom: 4px solid #f97316;  /* Changed to red */\n}\n.open-state .metric-icon {\n    background-color: #fff7ed;\n}\n.open-state .metric-icon svg {\n    color: #f97316;\n}\n.open-state .metric-value {\n    color: #ea580c;\n}\n\n/* Responsive Design */\n@media (max-width: 768px) {\n    body {\n        padding: 16px;\n    }\n    \n    .metrics-container {\n        grid-template-columns: 1fr;\n        gap: 16px;\n    }\n\n    .metric-value {\n        font-size: 2rem;\n    }\n    \n    .metric-card {\n        padding: 20px;\n    }\n}\n\n@media (min-width: 1024px) {\n    .metrics-container {\n        grid-template-columns: repeat(4, 1fr);\n    }\n}",
    "html": "<div class=\"metrics-container\" id=\"metricsContainer\"></div>",
    "renderOnMount": True,
    "onRender": "// Extract field names and values safely\nif (!data.series.length) return;\n\nconst fields = data.series[0].fields;\nconst fieldNames = fields.map(f => f.name);\nconst fieldValues = fields.map(f => f.values.get(0));\n\n// Format numbers\nfunction formatNumber(n) {\n  return typeof n === \"number\" ? new Intl.NumberFormat().format(n) : n;\n}\n\n// Description logic\nfunction getDescription(name) {\n  const lower = name.toLowerCase();\n  if (lower.includes(\"user\")) return \"Total number of users\";\n  if (lower.includes(\"employee\")) return \"Total number of employees\";\n  if (lower.includes(\"department\")) return \"Total number of departments\";\n  return \"Metric: \" + name.replace(/_/g, \" \");\n}\n\n// Color classes (cycle through for style variation)\nconst colorClasses = [\"total\", \"critical\", \"patched\", \"open-state\"];\n\nlet html = \"\";\n\nfor (let i = 0; i < fieldNames.length; i++) {\n  const name = fieldNames[i];\n  const value = fieldValues[i];\n  const className = colorClasses[i % colorClasses.length];\n\n  html += `\n    <div class=\"metric-card ${className}\">\n      <div class=\"metric-header\">\n        <div class=\"metric-title\">${name.replace(/_/g, \" \").toUpperCase()}</div>\n      </div>\n      <div class=\"metric-value\">${formatNumber(value)}</div>\n      <div class=\"metric-description\">${getDescription(name)}</div>\n    </div>\n  `;\n}\n\n// Inject HTML into container\nconst container = htmlNode.querySelector(\"#metricsContainer\");\nif (container) {\n  container.innerHTML = html;\n}",
    "panelupdateOnMount": True,
    "dynamicHtmlGraphics": False,
    "dynamicData": False,
    "dynamicFieldDisplayValues": False,
    "dynamicProps": False,
    "onInitOnResize": False,
    "onInit": "// Sets the text from customProperties\nconst htmlgraphicsText = htmlNode.getElementById('htmlgraphics-text');\nif (htmlgraphicsText) {\n  htmlgraphicsText.textContent = customProperties.text;\n  if (theme.isDark) {\n    htmlgraphicsText.style.color = 'green';\n  } else {\n    htmlgraphicsText.style.color = 'red';\n  }\n}"
  }


}
,
"gauge":{
  "type": "gauge",
  "title": "{{ Title }}",
  "description": "",
  "gridPos": {
    "x": 0,
    "y": 8,
    "h": 8,
    "w": 12
  },
  "fieldConfig": {
    "defaults": {
      "mappings": [],
      "thresholds": {
        "mode": "percentage",
        "steps": [
          {
            "color": "#bf2f08",
            "value": None
          },
          {
            "color": "semi-dark-yellow",
            "value": 85
          },
          {
            "color": "#37872D",
            "value": 95
          }
        ]
      },
      "color": {
        "mode": "thresholds"
      },
      "links": [],
      "max": 100,
      "min": 0,
      "unit": "percent"
    },
    "overrides": []
  },
  "pluginVersion": "11.5.2",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "refId": "A",
      "format": "table",
      "rawSql": "{{ rawSQL }}",
      "editorMode": "code",
      "sql": {
        "columns": [
          {
            "type": "function",
            "parameters": []
          }
        ],
        "groupBy": [
          {
            "type": "groupBy",
            "property": {
              "type": "string"
            }
          }
        ],
        "limit": 50
      },
      "rawQuery": True
    }
  ],
  "datasource": {
    "uid": "default",
    "type": "grafana-postgresql-datasource"
  },
  "options": {
    "reduceOptions": {
      "values": True,
      "calcs": [
        "lastNotNull"
      ],
      "fields": ""
    },
    "orientation": "auto",
    "showThresholdLabels": False,
    "showThresholdMarkers": False,
    "sizing": "auto",
    "minVizWidth": 75,
    "minVizHeight": 75,
    "text": {
      "valueSize": 35
    }
  }
},
"volkovlabs-echarts-panel": {
"type": "volkovlabs-echarts-panel",
"title": "{{ Title }}",
"description": "{{ Description }}",
  "gridPos": {
"x": 0,
"y": 0,
"h": 8,
"w": 12
},
"pluginVersion": "11.5.2",
"targets": [{"refId": "A", "format": "table", "rawSql": "{{ SQL }}"}],
"datasource": {"type": "grafana-postgresql-datasource", "uid": "default"},
"options": {
    "echarts": {}
}
}
,
"donutchart":{
    "type": "volkovlabs-echarts-panel",
    "title": "{{ Title }}",
    "description": "{{ Description }}",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 11,
    "w": 9
  },
  "fieldConfig": {
    "defaults": {},
    "overrides": []
  },
  "pluginVersion": "6.6.0",
  "targets": [
    {
      "datasource": {
        "type": "grafana-postgresql-datasource",
        "uid": "default"
      },
      "editorMode": "code",
      "format": "table",
      "rawQuery": True,
      "rawSql": "{{ SQL }}",
      "refId": "A",
      "sql": {
        "columns": [
          {
            "parameters": [],
            "type": "function"
          }
        ],
        "groupBy": [
          {
            "property": {
              "type": "string"
            },
            "type": "groupBy"
          }
        ],
        "limit": 50
      }
    }
  ],
  "datasource": {
    "type": "grafana-postgresql-datasource",
    "uid": "default"
  },
  "options": {
    "renderer": "canvas",
    "map": "none",
    "themeEditor": {
      "name": "default",
      "config": "{}"
    },
    "baidu": {
      "key": "",
      "callback": "bmapReady"
    },
    "gaode": {
      "key": "",
      "plugin": "AMap.Scale,AMap.ToolBar"
    },
    "google": {
      "key": "",
      "callback": "gmapReady"
    },
    "editorMode": "visual",
    "editor": {
      "format": "auto"
    },
    "visualEditor": {
      "dataset": [],
      "series": [],
      "code": "const seriesData = [];\nconst colorPalette = ['#053f73', '#009ac7', '#58eae8', '#1f78b4', '#a6cee3'];\nconst colors = {};\nconst Title = context.panel.data.series[0].fields[0].name;\nif (context.panel.data.series.length > 0) {\n  const categoryField = context.panel.data.series[0].fields.find(f => f.type === 'string');\n  if (categoryField) {\n    for (let i = 0; i < categoryField.values.length; i++) {\n      const key = categoryField.values[i];\n      if (!(key in colors)) {\n        colors[key] = colorPalette[i % colorPalette.length];\n      }\n    }\n  }\n\n  context.panel.data.series.forEach(series => {\n    const categoryField = series.fields.find(f => f.type === 'string');\n    const valueField = series.fields.find(f => f.type === 'number');\n\n    if (categoryField && valueField) {\n      for (let i = 0; i < categoryField.values.length; i++) {\n        seriesData.push({\n          name: categoryField.values[i],\n          value: valueField.values[i],\n          itemStyle: {\n            color: colors[categoryField.values[i]] || null\n          }\n        });\n      }\n    }\n  });\n}\n\nreturn {\n  title: {\n    left: 'center'\n  },\n  color: colorPalette,\n  tooltip: {\n    trigger: 'item',\n    formatter: '{b}: {c} ({d}%)'\n  },\n  legend: {\n    orient: 'vertical',\n    left: 'left',\n    top: 'center',\n    data: seriesData.map(item => item.name),\n    textStyle: {\n      fontSize: 12\n    },\n    show: true\n  },\n  series: [\n    {\n      name: 'Data',\n      type: 'pie',\n      radius: ['50%', '70%'],\n      avoidLabelOverlap: false,\n      label: {\n        show: true,\n        position: 'outside',\n        formatter: '{b}: {c}'\n      },\n      emphasis: {\n        label: {\n          show: true,\n          fontSize: 16,\n          fontWeight: 'bold',\n          formatter: '{b}: {c} ({d}%)'\n        }\n      },\n      labelLine: {\n        show: true\n      },\n\n\n      data: seriesData\n    }\n  ], graphic: {\n    type: 'text',\n    left: 'center',\n    top: 'center',\n    style: {\n      text: `${Title}`,\n      textAlign: 'center',\n      fill: colorPalette,   // Keeping the applied color\n      fontSize: 22,\n      fontWeight: 'bold'\n    }\n  }\n};\n\n",
      "getOption": "return {};"
    },
    "getOption": "const series = context.panel.data.series.map((s) => {\n  const sData = s.fields.find((f) => f.type === 'number').values.buffer || s.fields.find((f) => f.type === 'number').values;\n  const sTime = s.fields.find((f) => f.type === 'time').values.buffer || s.fields.find((f) => f.type === 'time').values;\n  \n  return {\n    name: s.refId,\n    type: 'line',\n    showSymbol: false,\n    areaStyle: {\n      opacity: 0.1,\n    },\n    lineStyle: {\n      width: 1,\n    },\n    data: sData.map((d, i) => [sTime[i], d.toFixed(2)]),\n  };\n});\n\n/**\n * Enable Data Zoom by default\n */\nsetTimeout(() => context.panel.chart.dispatchAction({\n  type: 'takeGlobalCursor',\n  key: 'dataZoomSelect',\n  dataZoomSelectActive: true,\n}), 500);\n\n/**\n * Update Time Range on Zoom\n */\ncontext.panel.chart.on('datazoom', function (params) {\n  const startValue = params.batch[0]?.startValue;\n  const endValue = params.batch[0]?.endValue;\n  locationService.partial({ from: startValue, to: endValue });\n});\n\nreturn {\n  backgroundColor: 'transparent',\n  tooltip: {\n    trigger: 'axis',\n  },\n  legend: {\n    left: '0',\n    bottom: '0',\n    data: context.panel.data.series.map((s) => s.refId),\n    textStyle: {\n      color: 'rgba(128, 128, 128, .9)',\n    },\n  },\n  toolbox: {\n    feature: {\n      dataZoom: {\n        yAxisIndex: 'none',\n        icon: {\n          zoom: 'path://',\n          back: 'path://',\n        },\n      },\n      saveAsImage: {},\n    }\n  },\n  xAxis: {\n    type: 'time',\n  },\n  yAxis: {\n    type: 'value',\n    min: 'dataMin',\n  },\n  grid: {\n    left: '2%',\n    right: '2%',\n    top: '2%',\n    bottom: 24,\n    containLabel: true,\n  },\n  series,\n};"
  }
}
}