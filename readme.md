## img2table

### 接口

```
http://ip:port/api/img2table
```

### **post请求**

```json
{
    "content": "XXX.png"
}    //图片的存储路径

```

### **响应格式**

```json
{
    "content": [
        {
            "colspan": [1,1],
            "rowspan": [1,1],
            "text": "井号"
        },
        {
            "colspan": [2,2],
            "rowspan": [1,1],
            "text": "安C19-18"
        },
        ...
        ]
}

```

