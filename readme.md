# Markdown inline SVG

Simple way for build-in SVG image in your Markdown file.

[![Build Status](https://travis-ci.org/vitalibo/markdown-inline-svg.svg?branch=master)](https://travis-ci.org/vitalibo/markdown-inline-svg)

## Usage

To insert inline image in your markdown follow steps:

1. Create vector diagram or picture using for example [draw.io](https://draw.io) and save as SVG file.
2. Insert link to image in your markdown file.
    ```
    ![alt text](https://fwtbbmf399.execute-api.us-east-1.amazonaws.com/Prod/svg?source=https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md&name=sample.svg)
    ```
    where 
    - `source` - is link to itself markdown file;
    - `name` - marker for specify the picture;
    - `token` - (optional) github personal access token for private projects (required `repo` scope).
    > **_NOTE:_**  Api Gateway deployed in my own AWS account, and I do not guarantee that host `https://
    .execute-api.us-east-1.amazonaws.com` will always work.
3. Now you need include SVG file into markdown file, and insert at beginning and end marker name that start with `@` symbol.
    ```
    @sample.svg
    ... insert your svg here ...
    @sample.svg
    ```
4. Also, github support html tag `details`, that you can specify for open or close SVG code on demand that improve readability.

Full code look like follow sample:


    ![alt text](https://fwtbbmf399.execute-api.us-east-1.amazonaws.com/Prod/svg?source=https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md&name=sample.svg)
    
    <details> 
    <summary>SVG code</summary>
    
    ```
    @sample.svg
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="121px" height="81px" viewBox="-0.5 -0.5 121 81" style="background-color: rgb(255, 255, 255);">
        <defs/>
        <g>
            <ellipse cx="60" cy="40" rx="60" ry="40" fill="#ffffff" stroke="#000000" pointer-events="all"/>
        </g>
    </svg>
    @sample.svg
    ```
    
    </details>

### Example

![AwsDiagram](https://fwtbbmf399.execute-api.us-east-1.amazonaws.com/Prod/svg?source=https://raw.githubusercontent.com/vitalibo/markdown-inline-svg/master/readme.md&name=aws.svg)

<details> 
<summary>SVG code</summary>

```
@aws.svg
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="2261px" height="1442px" viewBox="-0.5 -0.5 2261 1442"
     content="&lt;mxfile host=&quot;app.diagrams.net&quot; modified=&quot;2020-12-07T02:57:59.505Z&quot; agent=&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36&quot; etag=&quot;oHpB2tbWbspc0QVncWxG&quot; version=&quot;13.10.9&quot; type=&quot;device&quot;&gt;&lt;diagram name=&quot;Page-1&quot; id=&quot;aaaa8250-4180-3840-79b5-4cada1eebb92&quot;&gt;7V1bc9o6EP41eSxjSb7pMRDSPrQznclM+3hG2AI8MRZjm1zOrz8WvmBdktDUwoIDPATLQnL0fbvaXa3EDZptXr7mZLv+wWKa3kAnfrlBdzcQAhf61R9e8lqXYODWBas8iZtKh4KH5F/aFDpN6S6JaSFULBlLy2QrFkYsy2hUCmUkz9mzWG3JUrHXLVlRpeAhIqla+juJy3VdGnrOofwbTVbrtmfgNHcWJHpc5WyXNf3dQLTcv+rbG9K21dQv1iRmz70iNL9Bs5yxsv60eZnRlI9tO2z19+7fuNs9d06z8pgvxB6JgBsuaLQInEX0JagbeCLpjrb/wf45y9d2bJ5oXibVUH0nC5r+ZEVSJiyrbi1YWbLNDZquy01aXYPqY1v3Nk1WvE7JtlVpUebssRtYXi8mxZryR3L47TXZ8r42LyvOrgl5LlA8WaakvGO7RUrnMQdvukzSdMZSlu8fCzn7V1VOim1NiWXywtuc7uHYtw7q1usR53Ujtkmi5vOSZeU92SQp5+wvmsckI01xQ1AA+XWabH81bamj3QDA/2/60itqRv8rZRta5q9Vlfau7zRD3IgKQDCsC54PzPPCRn7WPdYhhBrGN2xfda0fEK8+NKC/wRgSVjhSRPxoGS+h8wWFVwqclgI4EBmAMVQI4LcaVSCAFxggALwS4MQEqNAVCBAEWNUAAKoEgC1ThtUAH+NPq+F/aC6TYt9nEs0PhVOaxbd8Hq7uZyyjIiNSzpppN1O2ADYVRWZ4x6LyFgw0FqZ6FYT+IDvqGHdTe04r9iVPooWgG/imi58sqR6lAxl5sp53QrGNgu3yiDZf68/ZUksyXYDjSy2VJF/RUmmpQoS89qpteYXinUeWpybYPPKBWXWTB5514/o56rnWqp74NSMbdrdQlc58xt9du7073py//1IdfczwPzA2wlACFKu2BgjBxNPomtY2H1TXeDboGt0McqFayIWyFkKf1EKy1QKQZ0YL+aHckWtYC/nWaqEK/KJq6zsj8ZSkJIuSbDWiRhrE+kFAxBe7qk5q7Zy+SIThBJiwf+11gZ9Z/rhM2fMDzZ+SSGP/ntFU5AEgoB6EupkITqDTe2lYANxw4hpggb1OUJSyXbzMGR/6MyaALPY+0BDAQZNQg7mPJwHuvUIDBMDWEqCaHWme0fIrKekzn/dG1P/cE/7WfKn1ip1h5oVAmvdRoCEI8CeBzlqCExOcaE3gKynGIkUl+q7AihAGo7MCXFkxLivUSAXwwOi0gNbSIqdxsU6WGgNiNhP83z5TfP62yIAAADkfm5BaZxqbCGWAI+KmI+FdJJttSu8W8KwtxsAXVb+HPY3LoA1eAQwnvgnM7Q1YFhnZFmumkXEXhn7kaSEPbuFdaBHk3PsTFTsKfAV0XXTANyLiR4QrR4KbbLdp1RTv7J+C5lXLZy3rwGmFu5vRW23fl3aINLIOTcQDgL1BwYuDHsrQB+NCb29E8NKgB75l0NsbBrw06BWF3y04jgS9vQHAZhVoSklWlCR9PG/g1cSINq9NXArQAO+aMPKgvUG+d/w4x3FnGOsQx3g2u7+3CXFfTmABUE14OrEn14JsIeoxKcmM8kieCnuTXHwegh76AuxdBsGHCt6FJhC3N17Tm9s1oh768xDd6jCfOvcoQDZh7rbGc4e5GrNptUEfcs9EajO02H3nCUxrSuK/Aa9Hkya/6dh81upalwQ1cJ4rcsU1/0rtq1F6hFU2QCNssNit+z+wwXUkNug2PpyMDfau4RU02uWVlt/vdNr3+GbauzIhdOaBLRMCdJAIepe73E+A9CdYeKkcQCZcPmivy1dX4Vmv9f6Hd0hwXnsfXCQu6mCoev2hZtXWM+H6IXtdv4slgB9igQBBoCZ0nI4AFvsE3CZ4mI+H+xDCLnkDuhX7UJPwZwZre9dua6x/nzfWSAzyuJr0PaRz/aBjIqsbWe77jSfZA3j5UIrdY6xGcD2NDjezgdnildpx5XoApD0oSjVur/sxPKyL2xrZPoYs9+HPGmsYiPHaCkJNwhXQeGfyftRhsLbXO7sADe7JeVZtapuwHUMXqR0Aa/kUEnuDMeePtOeI/hZwPU3arKtZhgnf2W36WaShtUiPlj95ChLgdkWtI4Fz3KbLIdIqZQ7Y63PncfGDFNqFV8MZFqcggbIM72oOntEvyA5huMs0uLrj5qAOsAy1TukHQIUaD+CMy0hfXXFzSIdS2KUy5DQb5JDmOLFggLQaGemrK24MaejIMg3b5fUe0tDVnBs2SN6cDLW9mbJ1lf0RMSktiuboMMvhDV3RIfN8jT/WxVhFM92AINvre58lup4ku4EusnI6dC3e166Hd6ylz9Nkxsjs0Mk+dHUHY7gGXHSL9zGPIPvDH/7oQCklRnfQBXQ1YVZDebHWwn1RmVBYOgDpcH7a6TOhFJE/whe/HgH654fvyQEXJC+UHHv4nnpqtG/oDFAsd+R5w56+p3DP8ujAxafluvJ05Kk77k2l5SpksDeAcFGTEfDaY0AVfWJ8NqouD793UCuQw49KoPl/&lt;/diagram&gt;&lt;/mxfile&gt;"
     style="background-color: rgb(255, 255, 255);">
    <defs/>
    <g>
        <path d="M 1458.3 1011.9 L 1473.8 1003.2 L 1458.4 994.2 L 1443 1003.2 L 1458.4 958.8 L 1535.1 950 L 1519.5 958.8 L 1535.1 967.7 L 1550.4 958.8 L 2011.7 1221.1 L 1996.2 1229.8 L 2011.6 1238.8 L 2027 1229.8 L 2011.6 1274.2 L 1934.9 1283 L 1950.5 1274.2 L 1934.9 1265.3 L 1919.6 1274.2"
              fill="#f4b934" stroke="none" transform="translate(0,1116.5)scale(1,-1)translate(0,-1116.5)"
              pointer-events="all"/>
        <path d="M 828.3 675.9 L 843.8 667.2 L 828.4 658.2 L 813 667.2 L 828.4 622.8 L 905.1 614 L 889.5 622.8 L 905.1 631.7 L 920.4 622.8 L 1423.7 909.1 L 1408.2 917.8 L 1423.6 926.8 L 1439 917.8 L 1423.6 962.2 L 1346.9 971 L 1362.5 962.2 L 1346.9 953.3 L 1331.6 962.2"
              fill="#f4b934" stroke="none" transform="translate(0,792.5)scale(1,-1)translate(0,-792.5)"
              pointer-events="all"/>
        <path d="M 118.3 462.9 L 133.8 454.2 L 118.4 445.2 L 103 454.2 L 118.4 409.8 L 195.1 401 L 179.5 409.8 L 195.1 418.7 L 210.4 409.8 L 599.7 631.1 L 584.2 639.8 L 599.6 648.8 L 615 639.8 L 599.6 684.2 L 522.9 693 L 538.5 684.2 L 522.9 675.3 L 507.6 684.2"
              fill="#f4b934" stroke="none" transform="translate(0,547)scale(1,-1)translate(0,-547)"
              pointer-events="all"/>
        <path d="M 193 930 L 245.94 899.43 Q 254.6 894.43 245.94 889.43 L 151.66 835 Q 143 830 134.34 825 L 10.42 753.45 Q 1.76 748.45 10.42 743.45 L 103 690"
              fill="none" stroke="#000000" stroke-width="5" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 29 1094.99 L 29 955.01 L 89.49 920.29 L 119.5 955.01 L 149.5 920 L 210.5 955.49 L 210.5 1094.99 L 150.01 1130 L 120 1112.4 L 89.49 1130 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 59.49 989.99 L 29 989.99 L 89.49 1025 L 89.49 1130 L 29 1094.99 L 29 955.99 Z M 119.5 955.01 L 150.01 920 L 210.5 955.49 L 180.01 990.31 L 210.5 989.99 L 150.01 1025 L 120 1025 L 180.01 990.31"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 89.49 1025 L 119.5 1025 L 119.5 1112.4 L 89.49 1130 Z M 150.01 1130 L 150.01 1025 L 210.5 989.99 L 180.01 990.31 L 210.5 955.49 L 210.5 1094.51 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 59.49 989.99 L 29 989.99 L 89.49 1025 L 89.49 1130 L 29 1094.99 L 29 955.99 Z M 119.5 955.01 L 150.01 920 L 210.5 955.49 L 180.01 990.31 L 210.5 989.99 L 150.01 1025 L 120 1025 L 180.01 990.31 Z M 89.49 1025 L 119.5 1025 L 119.5 1112.4 L 89.49 1130 Z M 150.01 1130 L 150.01 1025 L 210.5 989.99 L 210.5 1094.51 Z M 59.49 989.99 L 119.75 955.01 M 59.49 989.99 L 120 1025"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 117.5 967.5 C 122.37 968.53 127.08 970.21 131.49 972.5 C 136.44 974.85 141.14 977.7 145.5 981 C 147.97 982.87 150.28 984.94 152.4 987.2 C 153.09 987.79 153.07 988.62 152.35 989.2 C 151.63 989.77 150.41 989.94 149.41 989.59 C 145.29 988.69 141.3 987.32 137.5 985.5 C 131.71 982.99 126.24 979.8 121.2 976.01 C 118.78 973.94 116.54 971.66 114.5 969.2 C 114.43 968.68 114.74 968.17 115.33 967.83 C 115.93 967.49 116.74 967.37 117.5 967.5 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 122 1007 C 119.29 1007.21 116.57 1006.87 114 1006 C 108.59 1004.19 103.4 1001.81 98.5 998.9 C 94.44 996.54 90.59 993.82 87.01 990.79 C 84.78 989.09 83.87 986.86 84.5 984.7 L 112.71 968.99 C 113.04 970.64 113.86 972.19 115.1 973.51 C 118.2 976.35 121.58 978.87 125.2 981 C 130.3 984.35 135.77 987.1 141.49 989.19 C 144.09 990.27 146.89 990.78 149.7 990.71 Z M 120.69 997.99 C 120.71 996.94 121.26 995.94 122.2 995.2 C 123.39 994.63 124.75 994.56 125.99 994.99 L 127.1 992.89 C 125.94 992.47 125.11 991.79 124.8 991 C 124.65 990.09 125.3 989.21 126.5 988.69 L 125.3 986.91 C 123.65 987.3 121.9 986.97 120.49 986 C 119.54 985.35 119.1 984.47 119.3 983.61 L 115.7 982.89 C 114.88 983.37 113.95 983.65 113 983.69 C 111.54 983.73 110.12 983.24 109.01 982.31 L 104.99 983 C 105.36 983.44 105.46 984 105.27 984.52 C 105.07 985.03 104.6 985.43 104 985.6 C 102.92 985.9 101.79 985.94 100.69 985.71 L 99.29 987.7 C 100.4 987.98 101.25 988.87 101.49 989.99 C 101.39 990.96 100.73 991.78 99.8 992.09 L 101.49 993.79 C 102.87 993.56 104.29 993.81 105.5 994.51 C 106.57 995.01 107.16 996 107.01 997.01 L 110.49 997.99 C 111.64 997.13 113.07 996.7 114.5 996.8 C 115.69 996.94 116.8 997.43 117.7 998.2 Z M 119.5 993.71 C 118.47 994.24 117.34 994.54 116.19 994.59 C 113.87 994.56 111.57 994.11 109.4 993.29 L 109.1 994.11 L 105.99 990.79 C 107.72 991.69 109.58 992.34 111.49 992.7 C 112.98 992.97 114.49 993.07 115.99 993 C 117.19 993.06 118.39 992.86 119.5 992.41 Z M 120.29 990.33 C 118.81 989.31 117.2 988.49 115.5 987.89 C 114.11 987.45 112.66 987.22 111.2 987.2 C 109.93 987.23 108.67 987.5 107.5 988 L 106.5 987.1 C 108.17 986.53 109.93 986.26 111.69 986.3 C 113.56 986.48 115.38 987.02 117.05 987.87 L 117.5 986.8 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 29 1094.99 L 29 955.01 L 89.49 920.29 L 119.5 955.01 L 149.5 920 L 210.5 955.49 L 210.5 1094.99 L 150.01 1130 L 120 1112.4 L 89.49 1130 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 263 960 L 375.68 894.94 Q 384.34 889.94 393 894.94 L 514.34 965 Q 523 970 531.66 975 L 668 1053.72 Q 676.66 1058.72 685.32 1053.72 L 813 980"
              fill="none" stroke="#000000" stroke-width="5" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 153 640.5 L 153 587.5 L 183.5 570 L 214.5 570 L 245 587.5 L 245 640.5 L 214.5 658.17 L 183.5 658.17 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 153 605.5 L 183.5 623 L 214.5 623 L 214.5 658.17 L 183.5 658.17 L 153 640.5 Z" fill-opacity="0.1"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 214.5 623 L 245 605.5 L 245 640.5 L 214.5 658.17 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 153 605.5 L 183.5 623 L 214.5 623 L 214.5 658.17 L 183.5 658.17 L 153 640.5 Z" fill="none"
              stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 214.5 623 L 245 605.5 L 245 640.5 L 214.5 658.17 Z M 183.5 623 L 183.5 658.17" fill="none"
              stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 184 582.3 C 188.63 580.87 193.82 580.24 199 580.5 C 204.9 580.78 210.5 582.18 215 584.5 C 222.22 587.59 226.97 592.52 228 598 C 228.71 601.76 226.57 605.5 222 608.5 C 217.91 610.99 213.28 612.46 208.5 612.8 C 203.29 613.38 197.95 613.04 193 611.8 C 187.7 610.78 182.93 608.81 179.2 606.1 C 175.65 603.53 173.17 600.4 172 597 C 170.81 593.56 172.05 590.03 175.5 587 C 177.69 585.06 180.6 583.45 184 582.3"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 179 602.8 L 186.3 598.5 L 190.3 600.7 L 194 593.4 L 191.5 593.3 L 196.5 588.8 L 193 587 L 200.3 582.7 L 206.7 586.6 L 199.4 590.7 L 197.6 589.6 L 198.7 593.7 L 195.6 593.5 L 192.6 599.5 L 198.5 596 L 196.8 595.2 L 203.7 593.2 L 201.4 591.8 L 208.6 587.6 L 215.2 591.2 L 208 595.5 L 205 593.8 L 201.7 598.2 L 199.8 596.9 L 194.8 599.9 L 204.8 598.4 L 204.5 596.6 L 211.2 597.3 L 209.7 596.4 L 217 592.3 L 223.6 595.9 L 216.2 600.2 L 212.7 598.3 L 205.5 601.2 L 205.2 599.7 L 192.5 601.9 L 195.7 603.8 L 188.5 607.9 Z"
              fill="#ececec" stroke="none" pointer-events="all"/>
        <path d="M 153 640.5 L 153 587.5 L 183.5 570 L 214.5 570 L 245 587.5 L 245 640.5 L 214.5 658.17 L 183.5 658.17 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 352 505.81 L 397.2 410 L 488.6 410 L 534.2 505.81 L 442.81 558.4 Z" fill="#ececec" stroke="#292929"
              stroke-width="1.41" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 352 505.81 L 397.29 410 L 397.29 462.4 L 442.81 558.4 Z M 488.6 462.4 L 488.6 410 L 534.2 505.81 Z"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 442.81 558.4 L 488.39 462.4 L 534.2 505.81 L 442.5 558.4 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" pointer-events="all"/>
        <path d="M 488.6 462.4 L 488.6 410 L 534.2 505.81 Z M 352 505.81 L 397.29 410 L 397.29 462.4 L 442.81 558.4 L 488.39 462.4 L 534.2 505.81 L 442.5 558.4 Z M 397.29 462.4 L 488.8 462.4 M 397.33 462.39 L 352 506.25"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <ellipse cx="442.79" cy="436.3" rx="37.49676000000001" ry="21.7035" fill="#5e5e5e" stroke="none"
                 pointer-events="all"/>
        <path d="M 447.69 416.9 L 459.01 423.4 L 451.9 427.41 L 440.8 420.8 Z M 441.21 426.8 L 443.19 435.3 L 428.2 434.2 L 427.1 425.7 Z M 417.3 434.2 L 428.6 440.6 L 421.69 444.61 L 410.3 438.2 Z M 435.7 444.7 L 447 451.3 L 440.09 455.31 L 428.8 448.7 Z M 446.51 423.99 L 440.9 427.1 M 428.71 434.1 L 422.97 437.39 M 443.1 435.2 L 453.19 441 L 441 448.09"
              fill="none" stroke="#ececec" stroke-width="1.41" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 352 505.81 L 397.2 410 L 488.6 410 L 534.2 505.81 L 442.81 558.4 Z Z" fill="none" stroke="#292929"
              stroke-width="1.41" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 153 374.4 L 153 367.2 L 159.1 363.6 L 159.1 257.59 L 189.6 240 L 250.8 275.2 L 250.8 381.21 L 256.8 384.99 L 256.8 391.8 L 225.79 409.8 L 214 409.8 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 159.1 258 L 220.2 292.99 L 220.2 398.8 L 226.2 409.8 L 214.4 409.8 L 153 374.4 L 153 367.2 L 159.1 363.6 Z"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 220.2 292.99 L 250.8 275.2 L 250.8 382 L 256.8 384.99 L 256.8 391.8 L 225.79 409.8 L 220.2 398 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 153 374.4 L 158.8 363.8 L 220.2 399 L 214.2 409.8 M 220.4 399 L 250.7 381.49 L 256.8 391.8"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 159.1 258 L 220.2 292.99 L 220.2 398.8 L 226.2 409.8 L 214.4 409.8 L 153 374.4 L 153 367.2 L 159.1 363.6 Z"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 220.2 292.99 L 250.8 275.2 L 250.8 382 L 256.8 384.99 L 256.8 391.8 L 225.79 409.8 L 220.2 398 Z"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 187.6 352.8 C 183.53 350.14 180.06 346.67 177.4 342.59 C 174.5 338.38 172.3 333.72 170.9 328.81 L 178.2 336.4 L 178.19 340.1 L 181.7 341.8 Z M 169.6 323.8 C 168.47 319.42 168.2 314.87 168.8 310.4 C 169.2 305.76 171.31 301.62 174.5 299.19 L 173.89 311.1 L 172.3 310.4 L 172.3 315.8 L 172.79 316.29 Z M 176.2 298.5 C 181.25 296.45 186.64 297.46 191.2 301.3 C 195.39 304.48 198.92 308.45 201.58 313 L 191.2 308.5 L 191.2 306.9 L 186.8 304.51 L 186.8 306 Z M 203.39 316.39 C 206.07 321.08 207.77 326.25 208.4 331.61 C 209.36 336.7 209.33 341.93 208.3 347.01 L 204.4 334.9 L 205.1 335 L 205.1 329.4 L 203.39 328.19 Z M 207.4 349.61 C 206.44 352.47 204.24 354.75 201.4 355.8 C 197.87 356.78 194.1 356.42 190.8 354.8 L 197 350.79 L 200.4 352.8 L 200.4 348.89 Z M 189.4 353.21 L 182.8 340.5 L 195.8 348.09 Z M 179.6 335 L 171.2 326.39 L 174.3 318.01 Z M 175.2 311.81 L 175.8 299.91 L 186.8 308.4 L 176.7 312.2 Z M 176.5 315 L 186.4 310.4 L 187.8 310.99 L 187.8 324.41 L 186.3 323.41 L 186.3 324.31 L 176.5 316.1 Z M 180.99 335.39 L 176.3 318.7 L 177.2 317.9 L 186.8 326.8 L 186.6 328.99 Z M 182.6 337.8 L 182.6 336 L 188.2 329.99 L 189.5 330.79 L 195.9 345.5 Z M 191.2 327.29 L 191.2 326.39 L 189.6 325.39 L 189.6 311.89 L 190.6 312.61 L 200.2 327.91 L 200.3 329.6 Z M 191.1 310.81 L 201.7 314.9 L 202 328.3 Z M 191.2 329.2 L 200.4 331 L 200.4 332.59 L 201.4 332.8 L 198 345.29 L 196.8 344.6 L 191.2 331.51 Z M 202.8 334.8 L 206.8 346.8 L 200.3 347.19 L 200.3 345.9 L 199.4 345.7 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 153 374.4 L 153 367.2 L 159.1 363.6 L 159.1 257.59 L 189.6 240 L 250.8 275.2 L 250.8 381.21 L 256.8 384.99 L 256.8 391.8 L 225.79 409.8 L 214 409.8 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 672 56 L 672 3.6 L 727.4 0 L 739.7 7.1 L 739.7 42.5 L 702.5 74.5 Z" fill="#ececec" stroke="#292929"
              stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 672 56 L 672 3.6 L 702.8 21.3 L 702.8 74.5 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 702.8 21.3 L 739.7 7.1 L 739.7 42.5 L 702.8 74.5 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 672 56 L 672 3.6 L 702.8 21.3 L 702.8 74.5 Z" fill="none" stroke="#5e5e5e" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 702.8 21.3 L 739.7 7.1 L 739.7 42.5 L 702.8 74.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 672 56 L 672 3.6 L 727.4 0 L 739.7 7.1 L 739.7 42.5 L 702.5 74.5 Z" fill="none" stroke="#292929"
              stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 623 95.5 L 623 60.3 L 660.01 10.6 L 690.5 28.3 L 690.5 81.5 L 635.3 102.8 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 623 95.5 L 623 60.3 L 635.3 67.2 L 635.3 102.8 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 635.3 102.8 L 635.3 67.2 L 690.5 28.3 L 690.5 81.5 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 623 95.5 L 623 60.3 L 635.3 67.2 L 635.3 102.8 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 635.3 102.8 L 635.3 67.2 L 690.5 28.3 L 690.5 81.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 623 95.5 L 623 60.3 L 660.01 10.6 L 690.5 28.3 L 690.5 81.5 L 635.3 102.8 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)" pointer-events="all"/>
        <path d="M 714.6 51.8 C 712.99 52.5 711.27 51.51 710.3 49.3 C 709.46 46.11 710.24 42.7 712.4 40.21 C 711.78 38.31 711.99 36.23 713 34.5 C 713.54 33.47 714.63 32.84 715.8 32.9 C 715.93 30.18 716.79 27.56 718.3 25.3 C 719.69 23.64 721.49 22.81 723.3 23.01 C 725.03 23.67 726.49 25.57 727.29 28.2 C 729.09 28.01 730.81 29.38 731.8 31.8 C 732.54 33.91 732.35 36.23 731.3 38.2 C 730.52 39.91 729.27 41.37 727.7 42.4 Z"
              fill="#5e5e5e" stroke="none" transform="translate(681.35,0)scale(-1,1)translate(-681.35,0)"
              pointer-events="all"/>
        <path d="M 1584 505 L 1584 452.6 L 1639.4 449 L 1651.7 456.1 L 1651.7 491.5 L 1614.5 523.5 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1584 505 L 1584 452.6 L 1614.8 470.3 L 1614.8 523.5 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1614.8 470.3 L 1651.7 456.1 L 1651.7 491.5 L 1614.8 523.5 Z" fill-opacity="0.1" fill="#000000"
              stroke="none" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1584 505 L 1584 452.6 L 1614.8 470.3 L 1614.8 523.5 Z" fill="none" stroke="#5e5e5e"
              stroke-miterlimit="10" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)"
              pointer-events="all"/>
        <path d="M 1614.8 470.3 L 1651.7 456.1 L 1651.7 491.5 L 1614.8 523.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1584 505 L 1584 452.6 L 1639.4 449 L 1651.7 456.1 L 1651.7 491.5 L 1614.5 523.5 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1535 544.5 L 1535 509.3 L 1572.01 459.6 L 1602.5 477.3 L 1602.5 530.5 L 1547.3 551.8 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1535 544.5 L 1535 509.3 L 1547.3 516.2 L 1547.3 551.8 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1547.3 551.8 L 1547.3 516.2 L 1602.5 477.3 L 1602.5 530.5 Z" fill-opacity="0.1" fill="#000000"
              stroke="none" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1535 544.5 L 1535 509.3 L 1547.3 516.2 L 1547.3 551.8 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1547.3 551.8 L 1547.3 516.2 L 1602.5 477.3 L 1602.5 530.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1535 544.5 L 1535 509.3 L 1572.01 459.6 L 1602.5 477.3 L 1602.5 530.5 L 1547.3 551.8 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)" pointer-events="all"/>
        <path d="M 1626.6 500.8 C 1624.99 501.5 1623.27 500.51 1622.3 498.3 C 1621.46 495.11 1622.24 491.7 1624.4 489.21 C 1623.78 487.31 1623.99 485.23 1625 483.5 C 1625.54 482.47 1626.63 481.84 1627.8 481.9 C 1627.93 479.18 1628.79 476.56 1630.3 474.3 C 1631.69 472.64 1633.49 471.81 1635.3 472.01 C 1637.03 472.67 1638.49 474.57 1639.29 477.2 C 1641.09 477.01 1642.81 478.38 1643.8 480.8 C 1644.54 482.91 1644.35 485.23 1643.3 487.2 C 1642.52 488.91 1641.27 490.37 1639.7 491.4 Z"
              fill="#5e5e5e" stroke="none" transform="translate(1593.35,0)scale(-1,1)translate(-1593.35,0)"
              pointer-events="all"/>
        <path d="M 2192 829 L 2192 776.6 L 2247.4 773 L 2259.7 780.1 L 2259.7 815.5 L 2222.5 847.5 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2192 829 L 2192 776.6 L 2222.8 794.3 L 2222.8 847.5 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2222.8 794.3 L 2259.7 780.1 L 2259.7 815.5 L 2222.8 847.5 Z" fill-opacity="0.1" fill="#000000"
              stroke="none" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2192 829 L 2192 776.6 L 2222.8 794.3 L 2222.8 847.5 Z" fill="none" stroke="#5e5e5e"
              stroke-miterlimit="10" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)"
              pointer-events="all"/>
        <path d="M 2222.8 794.3 L 2259.7 780.1 L 2259.7 815.5 L 2222.8 847.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2192 829 L 2192 776.6 L 2247.4 773 L 2259.7 780.1 L 2259.7 815.5 L 2222.5 847.5 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2143 868.5 L 2143 833.3 L 2180.01 783.6 L 2210.5 801.3 L 2210.5 854.5 L 2155.3 875.8 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2143 868.5 L 2143 833.3 L 2155.3 840.2 L 2155.3 875.8 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2155.3 875.8 L 2155.3 840.2 L 2210.5 801.3 L 2210.5 854.5 Z" fill-opacity="0.1" fill="#000000"
              stroke="none" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2143 868.5 L 2143 833.3 L 2155.3 840.2 L 2155.3 875.8 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2155.3 875.8 L 2155.3 840.2 L 2210.5 801.3 L 2210.5 854.5 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2143 868.5 L 2143 833.3 L 2180.01 783.6 L 2210.5 801.3 L 2210.5 854.5 L 2155.3 875.8 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)" pointer-events="all"/>
        <path d="M 2234.6 824.8 C 2232.99 825.5 2231.27 824.51 2230.3 822.3 C 2229.46 819.11 2230.24 815.7 2232.4 813.21 C 2231.78 811.31 2231.99 809.23 2233 807.5 C 2233.54 806.47 2234.63 805.84 2235.8 805.9 C 2235.93 803.18 2236.79 800.56 2238.3 798.3 C 2239.69 796.64 2241.49 795.81 2243.3 796.01 C 2245.03 796.67 2246.49 798.57 2247.29 801.2 C 2249.09 801.01 2250.81 802.38 2251.8 804.8 C 2252.54 806.91 2252.35 809.23 2251.3 811.2 C 2250.52 812.91 2249.27 814.37 2247.7 815.4 Z"
              fill="#5e5e5e" stroke="none" transform="translate(2201.35,0)scale(-1,1)translate(-2201.35,0)"
              pointer-events="all"/>
        <path d="M 971 533.82 L 971 427.33 L 976.52 412.94 L 1001.71 410 L 1021.67 421.76 L 1021.67 427.33 L 1028.29 423.17 L 1063.31 423.17 L 1098.53 443.74 L 1098.53 468.58 L 1101.23 468.16 L 1121 479.62 L 1121 582.88 L 1116.08 597.36 L 1089.89 600 L 1070.43 588.45 L 1070.43 582.88 L 1063.51 587.02 L 1028.19 587.02 L 993.17 566.16 L 993.17 544.77 L 991.48 546.1 Z"
              fill="#cc0000" stroke="#292929" stroke-width="2.01" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 971 534.28 L 971 427.73 L 991.57 439.89 L 991.57 545.98 Z M 993.27 566.16 L 993.27 464.42 L 1028.69 484.88 L 1028.69 587.02 Z M 1070.63 588.45 L 1070.63 486.21 L 1090.4 497.34 L 1090.4 600 Z"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 991.57 545.98 L 991.57 439.79 L 1001.4 438.98 L 993.47 443.65 L 993.47 544.16 Z M 1028.69 484.88 L 1063.1 484.88 L 1073.13 479.01 L 1070.63 486 L 1070.63 582.27 L 1063.87 587.02 L 1028.49 587.02 Z M 1090.4 497.55 L 1115.59 494.91 L 1121 480.13 L 1121 582.46 L 1116.29 597.26 L 1090.4 600 Z M 1021.67 421.55 L 1021.67 427.23 L 1018.96 429.15 Z M 1098.53 464.02 L 1098.53 468.58 L 1090.1 469.58 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 971 534.28 L 971 427.73 L 991.57 439.89 L 991.57 545.98 Z M 993.27 566.16 L 993.27 464.42 L 1028.69 484.88 L 1028.69 587.02 Z M 1070.63 588.45 L 1070.63 486.21 L 1090.4 497.34 L 1090.4 600 Z M 991.57 545.98 L 991.57 439.79 L 1001.4 438.98 L 993.47 443.65 L 993.47 544.16 Z M 1028.69 484.88 L 1063.1 484.88 L 1073.13 479.01 L 1070.63 486 L 1070.63 582.27 L 1063.87 587.02 L 1028.49 587.02 Z M 1090.4 497.55 L 1115.59 494.91 L 1121 480.13 L 1121 582.46 L 1116.29 597.26 L 1090.4 600 Z M 1021.67 421.55 L 1021.67 427.23 L 1018.96 429.15 Z M 1098.53 464.02 L 1098.53 468.58 L 1090.1 469.58 Z M 1063.51 484.88 L 1063.51 587.02 M 1115.78 494.51 L 1115.78 597.17"
              fill="none" stroke="#e6e6e6" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1044.55 433.92 C 1044.59 433.49 1044.81 433.1 1045.15 432.85 C 1045.5 432.6 1045.93 432.5 1046.35 432.59 C 1049.55 433 1052.67 433.92 1055.59 435.33 C 1063.75 438.45 1071.42 442.75 1078.36 448.1 C 1080.66 449.76 1082.72 451.74 1084.47 453.99 C 1084.68 454.52 1084.57 455.13 1084.19 455.55 C 1083.81 455.98 1083.22 456.15 1082.67 456 C 1079.03 455.42 1075.48 454.33 1072.13 452.77 C 1063.82 449.45 1056.05 444.9 1049.06 439.28 C 1047.26 437.77 1045.73 435.96 1044.55 433.92 Z M 1042.84 434.23 C 1042.78 435.52 1043.22 436.78 1044.05 437.76 C 1045.62 439.72 1047.48 441.43 1049.56 442.83 C 1055.93 447.59 1062.84 451.57 1070.13 454.69 C 1073.18 456.03 1076.38 456.98 1079.66 457.52 C 1080.53 457.74 1081.44 457.56 1082.16 457.02 L 1051.78 474.75 C 1050.45 474.95 1049.1 474.88 1047.8 474.54 C 1044.84 473.93 1041.97 472.98 1039.22 471.71 C 1031.38 468.34 1024.01 463.98 1017.26 458.74 C 1015.51 457.3 1013.95 455.63 1012.64 453.78 C 1012.13 453.2 1012.13 452.32 1012.64 451.74 Z"
              fill="#e6e6e6" stroke="none" pointer-events="all"/>
        <path d="M 1021.97 456 L 1042.54 444.14 L 1066.12 457.73 L 1045.04 469.79" fill="#cc0000" stroke="none"
              pointer-events="all"/>
        <path d="M 1036.01 446.88 L 1064.11 463.41 M 1051.07 447.9 L 1028.99 461.07 M 1059.1 452.47 L 1036.01 466.14"
              fill="none" stroke="#e6e6e6" stroke-linejoin="round" stroke-linecap="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 971 533.82 L 971 427.33 L 976.52 412.94 L 1001.71 410 L 1021.67 421.76 L 1021.67 427.33 L 1028.29 423.17 L 1063.31 423.17 L 1098.53 443.74 L 1098.53 468.58 L 1101.23 468.16 L 1121 479.62 L 1121 582.88 L 1116.08 597.36 L 1089.89 600 L 1070.43 588.45 L 1070.43 582.88 L 1063.51 587.02 L 1028.19 587.02 L 993.17 566.16 L 993.17 544.77 L 991.48 546.1 Z"
              fill="none" stroke="#292929" stroke-width="2.01" stroke-linejoin="round" stroke-linecap="round"
              stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 605 374.6 L 605 252.59 L 666.09 217 L 719.22 217.4 L 786.5 252.3 L 786.5 374.6 L 726.5 409.6 L 695.5 392.09 L 665.49 409.6 Z"
              fill="#ececec" stroke="#292929" stroke-width="1.83" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 605 252.59 L 635.49 252.3 L 605 287.3 L 665.49 322.29 L 665.49 409.6 L 605 374.6 Z M 695.5 391.84 L 695.5 287.4 L 726.01 322.1 L 726.01 409.6 Z"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 665.49 322.29 L 695.5 287.4 L 695.5 391.8 L 665.49 409.6 Z M 755.5 252.09 L 786.5 252.59 L 786.5 374.6 L 726.01 409.6 L 726.01 321.79 L 786.5 287.61 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 605 252.59 L 635.49 252.3 L 605 287.3 L 665.49 322.29 L 665.49 409.6 L 605 374.6 Z M 695.5 391.84 L 695.5 287.4 L 726.01 322.1 L 726.01 409.6 Z M 665.49 322.29 L 695.5 287.4 L 695.5 391.8 L 665.49 409.6 Z M 755.5 252.09 L 786.5 252.59 L 786.5 374.6 L 726.01 409.6 L 726.01 321.79 L 786.5 287.61 Z M 635.29 252.21 L 695.5 287.4 L 755.9 252.3 L 695.5 217.6 Z"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 652.81 252.3 L 695.8 227.3 L 739.2 252.3 L 695.8 277.4 Z" fill="#5e5e5e" stroke="none"
              pointer-events="all"/>
        <path d="M 659.5 257.6 L 707.4 230.1 M 685.39 230.35 L 733.12 257.85 M 726.01 264.34 L 677.13 236.11 M 668.51 241.6 L 715.5 268.96 M 659.61 246.97 L 704.75 273.1"
              fill="none" stroke="#ececec" stroke-width="2.75" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 605 374.6 L 605 252.59 L 666.09 217 L 719.22 217.4 L 786.5 252.3 L 786.5 374.6 L 726.5 409.6 L 695.5 392.09 L 665.49 409.6 Z"
              fill="none" stroke="#292929" stroke-width="1.83" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1933 1036.9 L 1926.71 1022.8 L 1884 998 L 1871.5 998 L 1846.9 1012.2 L 1841 1025.9 L 1896.2 1058 Z"
              fill="#4286c5" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1933 1037 L 1927 1029.2 L 1902.4 1044 L 1890.1 1044 L 1896.2 1058 Z" fill-opacity="0.3"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1896.2 1058 L 1890.3 1044.2 L 1847.2 1019.3 L 1847.01 1012.4 L 1841 1026 Z" fill-opacity="0.1"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1933 1037 L 1927 1029.2 L 1902.4 1044 L 1890.1 1044 L 1896.2 1058 Z" fill="none" stroke="#57a2d8"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1896.2 1058 L 1890.3 1044.2 L 1847.2 1019.3 L 1847.01 1012.4 L 1841 1026 Z" fill="none"
              stroke="#57a2d8" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1927 1023.2 L 1927 1029.2 M 1902.3 1044 L 1896.2 1058 M 1847 1019.3 L 1841 1026.4" fill="none"
              stroke="#57a2d8" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1933 1036.9 L 1926.71 1022.8 L 1884 998 L 1871.5 998 L 1846.9 1012.2 L 1841 1025.9 L 1896.2 1058 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 936 841.73 L 936 787.5 L 997.5 752 L 1059 787.5 L 1059 841.73 L 997.5 876 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 936 787.5 L 997.5 823 L 997.5 876 L 936 840.99 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1059 787.5 L 997.5 823 L 997.5 876 L 1059 840.99 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 936 787.5 L 997.5 823 L 997.5 876 L 936 840.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1059 787.5 L 997.5 823 L 997.5 876 L 1059 840.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 982 806.99 C 980.49 806.02 980.49 804.47 982 803.5 L 995 796 C 996.46 795.41 998.54 795.41 1000 796 L 1013 803.5 C 1014.23 804.42 1014.23 805.77 1013 806.7 L 1000 814.2 C 998.54 814.78 996.46 814.78 995 814.2 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 936 841.73 L 936 787.5 L 997.5 752 L 1059 787.5 L 1059 841.73 L 997.5 876 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 866 881.73 L 866 827.5 L 927.5 792 L 989 827.5 L 989 881.73 L 927.5 916 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 866 827.5 L 927.5 863 L 927.5 916 L 866 880.99 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 989 827.5 L 927.5 863 L 927.5 916 L 989 880.99 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 866 827.5 L 927.5 863 L 927.5 916 L 866 880.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 989 827.5 L 927.5 863 L 927.5 916 L 989 880.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 912 846.99 C 910.49 846.02 910.49 844.47 912 843.5 L 925 836 C 926.46 835.41 928.54 835.41 930 836 L 943 843.5 C 944.23 844.42 944.23 845.77 943 846.7 L 930 854.2 C 928.54 854.78 926.46 854.78 925 854.2 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 866 881.73 L 866 827.5 L 927.5 792 L 989 827.5 L 989 881.73 L 927.5 916 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1006 881.73 L 1006 827.5 L 1067.5 792 L 1129 827.5 L 1129 881.73 L 1067.5 916 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1006 827.5 L 1067.5 863 L 1067.5 916 L 1006 880.99 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1129 827.5 L 1067.5 863 L 1067.5 916 L 1129 880.99 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1006 827.5 L 1067.5 863 L 1067.5 916 L 1006 880.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1129 827.5 L 1067.5 863 L 1067.5 916 L 1129 880.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1052 846.99 C 1050.49 846.02 1050.49 844.47 1052 843.5 L 1065 836 C 1066.46 835.41 1068.54 835.41 1070 836 L 1083 843.5 C 1084.23 844.42 1084.23 845.77 1083 846.7 L 1070 854.2 C 1068.54 854.78 1066.46 854.78 1065 854.2 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 1006 881.73 L 1006 827.5 L 1067.5 792 L 1129 827.5 L 1129 881.73 L 1067.5 916 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 936 921.73 L 936 867.5 L 997.5 832 L 1059 867.5 L 1059 921.73 L 997.5 956 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 936 867.5 L 997.5 903 L 997.5 956 L 936 920.99 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1059 867.5 L 997.5 903 L 997.5 956 L 1059 920.99 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 936 867.5 L 997.5 903 L 997.5 956 L 936 920.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1059 867.5 L 997.5 903 L 997.5 956 L 1059 920.99 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 982 886.99 C 980.49 886.02 980.49 884.47 982 883.5 L 995 876 C 996.46 875.41 998.54 875.41 1000 876 L 1013 883.5 C 1014.23 884.42 1014.23 885.77 1013 886.7 L 1000 894.2 C 998.54 894.78 996.46 894.78 995 894.2 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 936 921.73 L 936 867.5 L 997.5 832 L 1059 867.5 L 1059 921.73 L 997.5 956 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1193 1042.35 L 1193 1007.56 L 1284 955 L 1375 1007.56 L 1375 1042.35 L 1284 1095 Z" fill="#ececec"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1193 1007.56 L 1284 1060.2 L 1284 1095 L 1193 1042.35 Z" fill-opacity="0.1" fill="#000000"
              stroke="none" pointer-events="all"/>
        <path d="M 1284 1060.2 L 1375 1007.56 L 1375 1042.35 L 1284 1095 Z" fill-opacity="0.3" fill="#000000"
              stroke="none" pointer-events="all"/>
        <path d="M 1193 1007.56 L 1284 1060.2 L 1284 1095 L 1193 1042.35 Z M 1284 1060.2 L 1375 1007.56 L 1375 1042.35 L 1284 1095 Z M 1238.23 981.18 L 1329.37 1033.72 L 1329.37 1068.72"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1334.29 983.88 L 1243.03 1036.44 L 1243.03 1071.33 L 1233.11 1065.52 L 1233.11 1030.52 L 1323.77 977.67 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 1224.18 1031.02 C 1226.24 1032.16 1228.17 1033.53 1229.91 1035.12 C 1231.64 1036.68 1233.19 1038.43 1234.51 1040.34 C 1235.46 1041.84 1236.2 1043.46 1236.72 1045.16 C 1237.12 1047.04 1237.26 1048.96 1237.12 1050.87 C 1235.41 1049.93 1233.8 1048.82 1232.31 1047.57 C 1230.5 1046.02 1228.88 1044.27 1227.49 1042.35 C 1226.11 1040.6 1225.02 1038.64 1224.29 1036.54 C 1223.91 1034.72 1223.87 1032.85 1224.18 1031.02 Z M 1238.63 1064.12 C 1238.67 1062.36 1238.88 1060.61 1239.23 1058.89 C 1239.79 1057.73 1240.87 1056.92 1242.14 1056.7 C 1243.89 1056.4 1245.69 1056.57 1247.35 1057.2 C 1248.91 1057.81 1250.42 1058.54 1251.86 1059.4 C 1251.9 1061.07 1251.8 1062.75 1251.57 1064.41 C 1250.94 1065.86 1249.52 1066.8 1247.95 1066.82 C 1245.97 1066.9 1244 1066.6 1242.14 1065.92 C 1240.93 1065.4 1239.76 1064.79 1238.63 1064.12 Z M 1243.94 1028.71 C 1245.12 1028.05 1246.37 1027.51 1247.65 1027.1 C 1249.54 1026.73 1251.48 1026.73 1253.37 1027.1 C 1256.24 1027.47 1259.04 1028.24 1261.69 1029.41 C 1263.33 1030.07 1264.9 1030.88 1266.4 1031.82 C 1265.68 1032.39 1264.9 1032.9 1264.09 1033.33 C 1261.65 1034.06 1259.06 1034.16 1256.57 1033.62 C 1253.9 1033.17 1251.31 1032.36 1248.86 1031.22 C 1247.14 1030.53 1245.5 1029.69 1243.94 1028.71 Z M 1245.54 1010.06 C 1247.16 1010.89 1248.7 1011.86 1250.15 1012.96 C 1251.34 1014.04 1252.45 1015.22 1253.46 1016.47 C 1254.57 1017.65 1254.73 1019.43 1253.86 1020.79 C 1253.09 1021.64 1252.18 1022.35 1251.17 1022.9 C 1249.16 1021.91 1247.28 1020.7 1245.54 1019.29 C 1244.2 1017.95 1243.06 1016.43 1242.14 1014.77 C 1241.75 1013.75 1241.94 1012.6 1242.63 1011.76 C 1243.5 1011.03 1244.48 1010.46 1245.54 1010.06 Z M 1276.96 991.68 C 1278.58 992.5 1280.13 993.47 1281.58 994.58 C 1282.78 995.66 1283.88 996.83 1284.89 998.09 C 1286 999.27 1286.17 1001.05 1285.29 1002.4 C 1284.52 1003.26 1283.6 1003.97 1282.58 1004.52 C 1280.58 1003.53 1278.69 1002.32 1276.96 1000.91 C 1275.61 999.57 1274.47 998.04 1273.55 996.38 C 1273.16 995.37 1273.35 994.21 1274.04 993.37 C 1274.91 992.65 1275.9 992.08 1276.96 991.68 Z M 1275.36 1010.33 C 1276.54 1009.67 1277.78 1009.13 1279.07 1008.72 C 1280.96 1008.35 1282.9 1008.35 1284.78 1008.72 C 1287.65 1009.08 1290.45 1009.86 1293.1 1011.03 C 1294.74 1011.69 1296.32 1012.5 1297.81 1013.44 C 1297.1 1014.01 1296.33 1014.52 1295.52 1014.95 C 1293.07 1015.68 1290.48 1015.79 1287.99 1015.24 C 1285.18 1014.64 1282.58 1013.83 1280.27 1012.83 C 1278.56 1012.15 1276.91 1011.31 1275.36 1010.33 Z M 1306.15 974.96 C 1307.77 975.79 1309.32 976.76 1310.77 977.86 C 1311.96 978.94 1313.06 980.12 1314.07 981.38 C 1315.17 982.55 1315.34 984.33 1314.47 985.69 C 1313.7 986.54 1312.78 987.25 1311.77 987.79 C 1309.77 986.8 1307.88 985.59 1306.15 984.19 C 1304.81 982.85 1303.66 981.33 1302.75 979.67 C 1302.35 978.65 1302.54 977.5 1303.24 976.66 C 1304.11 975.93 1305.09 975.36 1306.15 974.96 Z M 1304.55 993.61 C 1305.73 992.95 1306.97 992.41 1308.26 992 C 1310.15 991.51 1312.09 991.51 1313.98 992 C 1316.84 992.37 1319.65 993.15 1322.29 994.31 C 1323.93 994.97 1325.51 995.78 1327.01 996.72 C 1327.01 996.72 1327.01 996.72 1327.01 996.72 C 1324.03 998.43 1320.56 999.06 1317.18 998.53 C 1314.51 998.07 1311.91 997.26 1309.46 996.12 C 1307.75 995.43 1306.11 994.6 1304.55 993.61 Z"
              fill="#ececec" stroke="#5e5e5e" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1193 1042.35 L 1193 1007.56 L 1284 955 L 1375 1007.56 L 1375 1042.35 L 1284 1095 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1503 908.6 L 1503 786.59 L 1564.09 751 L 1617.22 751.4 L 1684.5 786.3 L 1684.5 908.6 L 1624.5 943.6 L 1593.5 926.09 L 1563.49 943.6 Z"
              fill="#004c99" stroke="#292929" stroke-width="1.83" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1503 786.59 L 1533.49 786.3 L 1503 821.3 L 1563.49 856.29 L 1563.49 943.6 L 1503 908.6 Z M 1593.5 925.84 L 1593.5 821.4 L 1624.01 856.1 L 1624.01 943.6 Z"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1563.49 856.29 L 1593.5 821.4 L 1593.5 925.8 L 1563.49 943.6 Z M 1653.5 786.09 L 1684.5 786.59 L 1684.5 908.6 L 1624.01 943.6 L 1624.01 855.79 L 1684.5 821.61 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1503 786.59 L 1533.49 786.3 L 1503 821.3 L 1563.49 856.29 L 1563.49 943.6 L 1503 908.6 Z M 1593.5 925.84 L 1593.5 821.4 L 1624.01 856.1 L 1624.01 943.6 Z M 1563.49 856.29 L 1593.5 821.4 L 1593.5 925.8 L 1563.49 943.6 Z M 1653.5 786.09 L 1684.5 786.59 L 1684.5 908.6 L 1624.01 943.6 L 1624.01 855.79 L 1684.5 821.61 Z M 1533.29 786.21 L 1593.5 821.4 L 1653.9 786.3 L 1593.5 751.6 Z"
              fill="none" stroke="#99ccff" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1550.81 786.3 L 1593.8 761.3 L 1637.2 786.3 L 1593.8 811.4 Z" fill="#99ccff" stroke="none"
              pointer-events="all"/>
        <path d="M 1557.5 791.6 L 1605.4 764.1 M 1583.39 764.35 L 1631.12 791.85 M 1624.01 798.34 L 1575.13 770.11 M 1566.51 775.6 L 1613.5 802.96 M 1557.61 780.97 L 1602.75 807.1"
              fill="none" stroke="#004c99" stroke-width="2.75" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1503 908.6 L 1503 786.59 L 1564.09 751 L 1617.22 751.4 L 1684.5 786.3 L 1684.5 908.6 L 1624.5 943.6 L 1593.5 926.09 L 1563.49 943.6 Z"
              fill="none" stroke="#292929" stroke-width="1.83" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1227 700 L 1227 629.5 L 1288.5 594 L 1350 629.5 L 1350 700 L 1288.5 736 Z" fill="#ffffff"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1227 700 L 1227 629.5 L 1288.5 665 L 1288.5 736 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1350 700 L 1350 629.5 L 1288.5 665 L 1288.5 736 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1227 700 L 1227 629.5 L 1288.5 665 L 1288.5 736 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1350 700 L 1350 629.5 L 1288.5 665 L 1288.5 736 Z" fill="none" stroke="#5e5e5e"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1238 648.5 L 1278.5 672 M 1238 655.5 L 1278.5 679 M 1238 662.5 L 1278.5 686 M 1299 672 L 1339.5 648.5 M 1299 679 L 1339.5 655.5 M 1299 686 L 1339.5 662.5"
              fill="none" stroke="#5e5e5e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"
              stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1227 700 L 1227 629.5 L 1288.5 594 L 1350 629.5 L 1350 700 L 1288.5 736 Z" fill="none"
              stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1258 632.86 L 1258 614.34 L 1289 597 L 1320 614.34 L 1320 632.86 L 1289 650 Z" fill="#86e83a"
              stroke="#292929" stroke-width="1.98" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1258 614.34 L 1289 631.18 L 1289 650 L 1258 632.86 Z" fill-opacity="0.1" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1289 631.18 L 1320 614.34 L 1320 632.86 L 1289 650 Z" fill-opacity="0.3" fill="#000000" stroke="none"
              pointer-events="all"/>
        <path d="M 1258 614.34 L 1289 631.18 L 1289 650 L 1258 632.86 Z" fill="none" stroke="#b0f373"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1289 631.18 L 1320 614.34 L 1320 632.86 L 1289 650 Z" fill="none" stroke="#b0f373"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1268.8 630.68 L 1268.8 620.28 L 1299.7 602.94 L 1305.5 606.21 L 1274.5 623.45 L 1274.5 633.65 Z M 1275.8 634.55 L 1275.8 624.24 L 1306.5 606.91 L 1311.5 609.58 L 1281.5 626.82 L 1281.5 637.32 Z"
              fill="#b0f373" stroke="none" pointer-events="all"/>
        <path d="M 1258 632.86 L 1258 614.34 L 1289 597 L 1320 614.34 L 1320 632.86 L 1289 650 Z" fill="none"
              stroke="#292929" stroke-width="1.98" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 182 913 L 221 924.5 L 201.5 936 Z" fill="#292929" stroke="none"
              transform="translate(0,924.5)scale(1,-1)translate(0,-924.5)" pointer-events="all"/>
        <path d="M 242 950 L 281 961.5 L 261.5 973 Z" fill="#292929" stroke="none"
              transform="translate(0,961.5)scale(1,-1)translate(0,-961.5)" pointer-events="all"/>
        <path d="M 44.33 703.22 C 44.86 700.52 46.3 698.07 48.41 696.31 C 52.3 693.47 56.81 691.61 61.56 690.89 C 67.9 689.99 74.36 690.34 80.58 691.9 C 86.17 693.27 91.39 695.83 95.9 699.42 C 98.63 701.74 100.44 704.98 101 708.53 C 101.01 711.48 99.94 714.34 98 716.55 C 94.35 719.83 89.81 721.96 84.96 722.66 C 77.07 724.01 68.97 723.42 61.36 720.95 C 56.33 719.34 51.74 716.6 47.92 712.94 C 45.32 710.41 44.01 706.84 44.33 703.22 Z"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 59.17 707.23 L 72.51 714.94 L 81.77 709.63 L 80.87 708.83 L 83.66 707.33 C 84.82 706.51 85.58 705.24 85.75 703.82 C 85.39 702.49 84.49 701.36 83.27 700.72 C 81.66 699.59 79.75 698.96 77.79 698.91 C 76.13 698.85 74.5 699.3 73.11 700.22 L 69.42 702.42 L 68.33 701.82 Z M 72.21 704.23 L 75.3 702.32 C 76.72 701.73 78.29 701.62 79.78 702.02 C 80.71 702.33 81.51 702.85 82.07 703.53 C 82.22 703.75 82.27 704.03 82.21 704.29 C 82.16 704.55 82 704.78 81.77 704.93 L 77.79 707.23 Z"
              fill="#ffffff" stroke="none" pointer-events="all"/>
        <path d="M 296 547.5 L 275 542 L 284.7 554.2" fill="#2d6195" stroke="none"
              transform="translate(0,567)scale(1,-1)translate(0,-567)" pointer-events="all"/>
        <path d="M 341 586.5 L 362 592 L 352.3 579.8" fill="#2d6195" stroke="none"
              transform="translate(0,567)scale(1,-1)translate(0,-567)" pointer-events="all"/>
        <path d="M 282.68 546.42 L 354.32 587.58" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12" transform="translate(0,567)scale(1,-1)translate(0,-567)"
              pointer-events="all"/>
        <path d="M 551 404.5 L 530 399 L 539.7 411.2" fill="#2d6195" stroke="none"
              transform="translate(0,424)scale(1,-1)translate(0,-424)" pointer-events="all"/>
        <path d="M 596 443.5 L 617 449 L 607.3 436.8" fill="#2d6195" stroke="none"
              transform="translate(0,424)scale(1,-1)translate(0,-424)" pointer-events="all"/>
        <path d="M 537.67 403.43 L 609.33 444.57" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12" transform="translate(0,424)scale(1,-1)translate(0,-424)"
              pointer-events="all"/>
        <path d="M 329 452 L 325 454.5 L 346 460 L 336.3 447.8 L 332.1 450.2 L 267.7 413.5 C 268.64 412.48 268.37 411.29 267 410.4 C 265.77 409.81 264.14 409.58 262.58 409.78 C 261.02 409.97 259.7 410.57 259 411.4 C 258.06 412.05 257.75 412.84 258.13 413.6 C 258.51 414.36 259.55 415.01 261 415.4 C 262.23 415.62 263.56 415.55 264.7 415.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 290 299 L 294 301.5 L 273 307 L 282.7 294.8 L 286.9 297.2 L 625.3 103.5 C 624.36 102.48 624.63 101.29 626 100.4 C 627.23 99.81 628.86 99.58 630.42 99.78 C 631.98 99.97 633.3 100.57 634 101.4 C 634.94 102.05 635.25 102.84 634.87 103.6 C 634.49 104.36 633.45 105.01 632 105.4 C 630.77 105.62 629.44 105.55 628.3 105.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1176 640 L 1172 642.5 L 1193 648 L 1183.3 635.8 L 1179.1 638.2 L 1145.7 618.5 C 1146.64 617.48 1146.37 616.29 1145 615.4 C 1143.77 614.81 1142.14 614.58 1140.58 614.78 C 1139.02 614.97 1137.7 615.57 1137 616.4 C 1136.06 617.05 1135.75 617.84 1136.13 618.6 C 1136.51 619.36 1137.55 620.01 1139 620.4 C 1140.23 620.62 1141.56 620.55 1142.7 620.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1380 646 L 1384 648.5 L 1363 654 L 1372.7 641.8 L 1376.9 644.2 L 1548.3 547.5 C 1547.36 546.48 1547.63 545.29 1549 544.4 C 1550.23 543.81 1551.86 543.58 1553.42 543.78 C 1554.98 543.97 1556.3 544.57 1557 545.4 C 1557.94 546.05 1558.25 546.84 1557.87 547.6 C 1557.49 548.36 1556.45 549.01 1555 549.4 C 1553.77 549.62 1552.44 549.55 1551.3 549.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1134 787 L 1138 789.5 L 1117 795 L 1126.7 782.8 L 1130.9 785.2 L 1226.3 730.5 C 1225.36 729.48 1225.63 728.29 1227 727.4 C 1228.23 726.81 1229.86 726.58 1231.42 726.78 C 1232.98 726.97 1234.3 727.57 1235 728.4 C 1235.94 729.05 1236.25 729.84 1235.87 730.6 C 1235.49 731.36 1234.45 732.01 1233 732.4 C 1231.77 732.62 1230.44 732.55 1229.3 732.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1176 986 L 1172 988.5 L 1193 994 L 1183.3 981.8 L 1179.1 984.2 L 1100.7 939.5 C 1101.64 938.48 1101.37 937.29 1100 936.4 C 1098.77 935.81 1097.14 935.58 1095.58 935.78 C 1094.02 935.97 1092.7 936.57 1092 937.4 C 1091.06 938.05 1090.75 938.84 1091.13 939.6 C 1091.51 940.36 1092.55 941.01 1094 941.4 C 1095.23 941.62 1096.56 941.55 1097.7 941.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1476 1153 L 1472 1155.5 L 1493 1161 L 1483.3 1148.8 L 1479.1 1151.2 L 1359.7 1083.5 C 1360.64 1082.48 1360.37 1081.29 1359 1080.4 C 1357.77 1079.81 1356.14 1079.58 1354.58 1079.78 C 1353.02 1079.97 1351.7 1080.57 1351 1081.4 C 1350.06 1082.05 1349.75 1082.84 1350.13 1083.6 C 1350.51 1084.36 1351.55 1085.01 1353 1085.4 C 1354.23 1085.62 1355.56 1085.55 1356.7 1085.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1875 1068.9 L 1868.71 1054.8 L 1826 1030 L 1813.5 1030 L 1788.9 1044.2 L 1783 1057.9 L 1838.2 1090 Z"
              fill="#4286c5" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1875 1069 L 1869 1061.2 L 1844.4 1076 L 1832.1 1076 L 1838.2 1090 Z" fill-opacity="0.3"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1838.2 1090 L 1832.3 1076.2 L 1789.2 1051.3 L 1789.01 1044.4 L 1783 1058 Z" fill-opacity="0.1"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1875 1069 L 1869 1061.2 L 1844.4 1076 L 1832.1 1076 L 1838.2 1090 Z" fill="none" stroke="#57a2d8"
              stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1838.2 1090 L 1832.3 1076.2 L 1789.2 1051.3 L 1789.01 1044.4 L 1783 1058 Z" fill="none"
              stroke="#57a2d8" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1869 1055.2 L 1869 1061.2 M 1844.3 1076 L 1838.2 1090 M 1789 1051.3 L 1783 1058.4" fill="none"
              stroke="#57a2d8" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1875 1068.9 L 1868.71 1054.8 L 1826 1030 L 1813.5 1030 L 1788.9 1044.2 L 1783 1057.9 L 1838.2 1090 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1503 1211.5 L 1503 1158.5 L 1518.5 1131.5 L 1549 1114 L 1580 1114 L 1610.5 1131.5 L 1626 1158.5 L 1626 1211.5 L 1564.5 1247 Z"
              fill="#ececec" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1518.5 1131.5 L 1518.5 1149.51 L 1549.49 1167.51 L 1564.5 1194 L 1564.5 1247 L 1503 1211.5 L 1503 1158.5 Z M 1610.5 1149.51 L 1610.5 1131.5 L 1626 1158"
              fill-opacity="0.1" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1564.5 1247 L 1564.5 1194 L 1579.51 1167.51 L 1610.5 1149.51 L 1626 1158 L 1626 1211.5 Z"
              fill-opacity="0.3" fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1526.1 1139.7 L 1562.7 1119.51 L 1575.4 1126.5 L 1557.8 1144.7 L 1590.6 1135 L 1603.5 1141.9 L 1566.8 1162.11 L 1558.81 1157.8 L 1589.3 1141.3 L 1550.4 1153.2 L 1542.2 1148.61 L 1564 1127.19 L 1533.8 1144 Z"
              fill="#5e5e5e" stroke="none" pointer-events="all"/>
        <path d="M 1518.5 1131.5 L 1518.5 1149.51 L 1549.49 1167.51 L 1564.5 1194 L 1579.51 1167.51 L 1610.5 1149.51 L 1610.5 1131.5 M 1503 1158.5 L 1518.5 1149.51 M 1564.5 1194 L 1564.5 1247 M 1626 1158.5 L 1610.01 1149.51 M 1549.49 1167.51 L 1579.51 1167.51"
              fill="none" stroke="#5e5e5e" stroke-linejoin="round" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1503 1211.5 L 1503 1158.5 L 1518.5 1131.5 L 1549 1114 L 1580 1114 L 1610.5 1131.5 L 1626 1158.5 L 1626 1211.5 L 1564.5 1247 Z"
              fill="none" stroke="#292929" stroke-width="2" stroke-linejoin="round" stroke-miterlimit="10"
              pointer-events="all"/>
        <path d="M 1650 1169 L 1654 1171.5 L 1633 1177 L 1642.7 1164.8 L 1646.9 1167.2 L 1794.3 1083.5 C 1793.36 1082.48 1793.63 1081.29 1795 1080.4 C 1796.23 1079.81 1797.86 1079.58 1799.42 1079.78 C 1800.98 1079.97 1802.3 1080.57 1803 1081.4 C 1803.94 1082.05 1804.25 1082.84 1803.87 1083.6 C 1803.49 1084.36 1802.45 1085.01 1801 1085.4 C 1799.77 1085.62 1798.44 1085.55 1797.3 1085.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1790 1007 L 1786 1009.5 L 1807 1015 L 1797.3 1002.8 L 1793.1 1005.2 L 1682.7 942.5 C 1683.64 941.48 1683.37 940.29 1682 939.4 C 1680.77 938.81 1679.14 938.58 1677.58 938.78 C 1676.02 938.97 1674.7 939.57 1674 940.4 C 1673.06 941.05 1672.75 941.84 1673.13 942.6 C 1673.51 943.36 1674.55 944.01 1676 944.4 C 1677.23 944.62 1678.56 944.55 1679.7 944.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 1950 995 L 1954 997.5 L 1933 1003 L 1942.7 990.8 L 1946.9 993.2 L 2169.3 866.5 C 2168.36 865.48 2168.63 864.29 2170 863.4 C 2171.23 862.81 2172.86 862.58 2174.42 862.78 C 2175.98 862.97 2177.3 863.57 2178 864.4 C 2178.94 865.05 2179.25 865.84 2178.87 866.6 C 2178.49 867.36 2177.45 868.01 2176 868.4 C 2174.77 868.62 2173.44 868.55 2172.3 868.2 Z"
              fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="all"/>
        <path d="M 681 186 L 2113 1002" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12" pointer-events="all"/>
        <path d="M 433 327 L 1865 1143" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12" pointer-events="all"/>
        <path d="M 433 186 L 681 327" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12"
              transform="translate(0,256.5)scale(1,-1)translate(0,-256.5)" pointer-events="all"/>
        <path d="M 1864 1000 L 2113 1142" fill="none" stroke="#2d6195" stroke-width="4" stroke-linecap="round"
              stroke-miterlimit="10" stroke-dasharray="12 12" transform="translate(0,1071)scale(1,-1)translate(0,-1071)"
              pointer-events="all"/>
        <path d="M 752.33 993.22 C 752.86 990.52 754.3 988.07 756.41 986.31 C 760.3 983.47 764.81 981.61 769.56 980.89 C 775.9 979.99 782.36 980.34 788.58 981.9 C 794.17 983.27 799.39 985.83 803.9 989.42 C 806.63 991.74 808.44 994.98 809 998.53 C 809.01 1001.48 807.94 1004.34 806 1006.55 C 802.35 1009.83 797.81 1011.96 792.96 1012.66 C 785.07 1014.01 776.97 1013.42 769.36 1010.95 C 764.33 1009.34 759.74 1006.6 755.92 1002.94 C 753.32 1000.41 752.01 996.84 752.33 993.22 Z"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 767.17 997.23 L 780.51 1004.94 L 789.77 999.63 L 788.87 998.83 L 791.66 997.33 C 792.82 996.51 793.58 995.24 793.75 993.82 C 793.39 992.49 792.49 991.36 791.27 990.72 C 789.66 989.59 787.75 988.96 785.79 988.91 C 784.13 988.85 782.5 989.3 781.11 990.22 L 777.42 992.42 L 776.33 991.82 Z M 780.21 994.23 L 783.3 992.32 C 784.72 991.73 786.29 991.62 787.78 992.02 C 788.71 992.33 789.51 992.85 790.07 993.53 C 790.22 993.75 790.27 994.03 790.21 994.29 C 790.16 994.55 790 994.78 789.77 994.93 L 785.79 997.23 Z"
              fill="#ffffff" stroke="none" pointer-events="all"/>
        <path d="M 303 990 L 349.79 962.98 Q 358.46 957.98 367.12 962.98 L 734.34 1175 Q 743 1180 751.66 1185 L 1179.6 1432.07 Q 1188.26 1437.07 1196.92 1432.07 L 1443 1290"
              fill="none" stroke="#000000" stroke-width="5" stroke-miterlimit="10" pointer-events="stroke"/>
        <path d="M 284 978 L 323 989.5 L 303.5 1001 Z" fill="#292929" stroke="none"
              transform="translate(0,989.5)scale(1,-1)translate(0,-989.5)" pointer-events="all"/>
        <path d="M 1379.33 1303.22 C 1379.86 1300.52 1381.3 1298.07 1383.41 1296.31 C 1387.3 1293.47 1391.81 1291.61 1396.56 1290.89 C 1402.9 1289.99 1409.36 1290.34 1415.58 1291.9 C 1421.17 1293.27 1426.39 1295.83 1430.9 1299.42 C 1433.63 1301.74 1435.44 1304.98 1436 1308.53 C 1436.01 1311.48 1434.94 1314.34 1433 1316.55 C 1429.35 1319.83 1424.81 1321.96 1419.96 1322.66 C 1412.07 1324.01 1403.97 1323.42 1396.36 1320.95 C 1391.33 1319.34 1386.74 1316.6 1382.92 1312.94 C 1380.32 1310.41 1379.01 1306.84 1379.33 1303.22 Z"
              fill="#000000" stroke="none" pointer-events="all"/>
        <path d="M 1394.17 1307.23 L 1407.51 1314.94 L 1416.77 1309.63 L 1415.87 1308.83 L 1418.66 1307.33 C 1419.82 1306.51 1420.58 1305.24 1420.75 1303.82 C 1420.39 1302.49 1419.49 1301.36 1418.27 1300.72 C 1416.66 1299.59 1414.75 1298.96 1412.79 1298.91 C 1411.13 1298.85 1409.5 1299.3 1408.11 1300.22 L 1404.42 1302.42 L 1403.33 1301.82 Z M 1407.21 1304.23 L 1410.3 1302.32 C 1411.72 1301.73 1413.29 1301.62 1414.78 1302.02 C 1415.71 1302.33 1416.51 1302.85 1417.07 1303.53 C 1417.22 1303.75 1417.27 1304.03 1417.21 1304.29 C 1417.16 1304.55 1417 1304.78 1416.77 1304.93 L 1412.79 1307.23 Z"
              fill="#ffffff" stroke="none" pointer-events="all"/>
    </g>
</svg>
@aws.svg
```

</details>

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container --template infrastructure/template.yaml
sam deploy --guided --config-file infrastructure/samconfig.toml
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
$ sam build --use-container
```

The SAM CLI installs dependencies defined in `src/main/python/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `src/test/resources` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
$ sam local invoke Function --event src/test/resources/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
$ sam local start-api
$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
Events:
  HttpRequest:
    Type: Api
    Properties:
      Path: /svg
      Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
$ sam logs -n Function --stack-name markdown-inline-svg --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Unit tests

Tests are defined in the `src/test/python/` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
$ pip install pytest pytest-mock --user
$ python -m pytest src/test/python/ -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name markdown-inline-svg
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.
